import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.stats import levy_stable
from numpy.linalg import lstsq

#mcculloch look up tables DOI:10.1080/03610918608812563
nu_alpha_grid = np.array([
    2.439, 2.5, 2.6, 2.7, 2.8,
    3.0, 3.2, 3.5, 4.0, 5.0,
    6.0, 8.0, 10.0, 15.0, 25.0
])

nu_beta_grid = np.array([0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0])
alpha_table = np.array([
    [2.000,2.000,2.000,2.000,2.000,2.000,2.000],
    [1.916,1.924,1.924,1.924,1.924,1.924,1.924],
    [1.808,1.813,1.829,1.829,1.829,1.829,1.829],
    [1.729,1.730,1.737,1.745,1.745,1.745,1.745],
    [1.664,1.663,1.663,1.668,1.676,1.676,1.676],
    [1.563,1.560,1.553,1.548,1.547,1.547,1.547],
    [1.484,1.480,1.471,1.460,1.448,1.438,1.438],
    [1.391,1.386,1.378,1.364,1.337,1.318,1.318],
    [1.279,1.273,1.266,1.250,1.210,1.184,1.150],
    [1.128,1.121,1.114,1.101,1.067,1.027,0.973],
    [1.029,1.021,1.014,1.004,0.974,0.935,0.874],
    [0.896,0.892,0.887,0.883,0.855,0.823,0.769],
    [0.820,0.815,0.810,0.805,0.780,0.750,0.700],
    [0.700,0.695,0.690,0.685,0.660,0.630,0.590],
    [0.600,0.595,0.590,0.585,0.560,0.530,0.500],
])

beta_table = np.array([
    [0.0, 2.160, 1.000, 1.000, 1.000, 1.000, 1.000],
    [0.0, 1.592, 3.390, 1.000, 1.000, 1.000, 1.000],
    [0.0, 0.759, 1.800, 1.000, 1.000, 1.000, 1.000],
    [0.0, 0.482, 1.048, 1.694, 1.000, 1.000, 1.000],
    [0.0, 0.360, 0.760, 1.232, 2.229, 1.000, 1.000],

    [0.0, 0.253, 0.518, 0.823, 1.575, 1.000, 1.000],
    [0.0, 0.203, 0.410, 0.632, 1.244, 1.906, 1.000],
    [0.0, 0.165, 0.332, 0.499, 0.943, 1.560, 1.000],
    [0.0, 0.136, 0.271, 0.404, 0.689, 1.230, 2.195],
    [0.0, 0.109, 0.216, 0.323, 0.539, 0.827, 1.917],

    [0.0, 0.096, 0.190, 0.284, 0.472, 0.693, 1.759],
    [0.0, 0.082, 0.163, 0.243, 0.412, 0.601, 1.596],
    [0.0, 0.074, 0.147, 0.220, 0.377, 0.546, 1.482],
    [0.0, 0.064, 0.128, 0.191, 0.330, 0.478, 1.362],
    [0.0, 0.056, 0.112, 0.167, 0.285, 0.428, 1.274],
])

# Interpolation between table entries
alpha_interp = RegularGridInterpolator(
    (nu_alpha_grid, nu_beta_grid),
    alpha_table,
    bounds_error=False,
    fill_value=None
)

beta_interp = RegularGridInterpolator(
    (nu_alpha_grid, nu_beta_grid),
    beta_table,
    bounds_error=False,
    fill_value=None
)


def mcculloch_estimator(x):
    # x = np.sort(np.asarray(x)) Instead of this, I made changes below:
    x = np.asarray(x, dtype=float)
    x = x[x > 0]    # remove resting steps (zeros / near-zeros)
    x = np.log(x)   # log-space: turns positive skew into roughly symmetric

    q05, q25, q50, q75, q95 = np.quantile(
        x, [0.05, 0.25, 0.5, 0.75, 0.95]
    )

    # IQR guard added to return clean NaN instead of propagating division-by-zero
    iqr = q75 - q25
    if iqr < 1e-10:
        return np.nan, np.nan, np.nan, np.nan

    # empirical ratios
    nu_a = (q95 - q05) / iqr
    nu_b = (q95 + q05 - 2*q50) / (q95 - q05)

    nu_a = np.clip(nu_a, nu_alpha_grid.min(), nu_alpha_grid.max())
    nu_b_abs = np.clip(abs(nu_b), nu_beta_grid.min(), nu_beta_grid.max())

    alpha = alpha_interp([[nu_a, nu_b_abs]])[0]

    beta_raw = beta_interp([[nu_a, nu_b_abs]])[0]
    beta = np.clip(np.sign(nu_b) * beta_raw, -1, 1)

    # sigma = (q75 - q25) / 2
    sigma = iqr / 2     # IQR of log(step_m), dimensionless and stable
    mu = q50            # median of log(step_m)

    return alpha, beta, sigma, mu


def koutrouvelis_estimator(x, n_points=20):
    x = np.asarray(x, dtype=float)
    x = x[x > 0]    # remove resting steps (zeros / near-zeros)
    x = np.log(x)   # log-space: stabilises the characteristic function

    # scale_est guards against degenerate (all-identical) input
    scale_est = (np.percentile(x, 75) - np.percentile(x, 25)) / 2
    if scale_est < 1e-10:
        return np.nan, np.nan, np.nan, np.nan

    # t = np.linspace(0.1, 1.0, n_points)
    # Instead of a fixed grid (only correct for unit-scale data), scale by
    # 1/scale_est so that t*x stays in a numerically well-behaved range.
    t = np.linspace(0.1 / scale_est, 1.0 / scale_est, n_points)

    # empirical CF
    phi = np.array([np.mean(np.exp(1j * ti * x)) for ti in t])

    # First regression: log(-log|phi(t)|^2) = log(2*sigma^alpha) + alpha*log|t|
    y = np.log(-np.log(np.abs(phi) ** 2 + 1e-12))   # 1e-12 avoids log(0)
    X = np.vstack([np.log(t), np.ones_like(t)]).T

    slope, intercept = lstsq(X, y, rcond=None)[0]

    alpha = slope
    sigma = np.exp(intercept / alpha) if alpha != 0 else np.nan

    phase = np.unwrap(np.angle(phi))

    y2 = phase
    X2 = np.vstack([t, t * np.log(t)]).T

    coeffs = lstsq(X2, y2, rcond=None)[0]

    mu   = coeffs[0]
    # With log-transformed data, sigma is O(1) so sigma**alpha is well-behaved
    beta = coeffs[1] / (sigma ** alpha) if sigma > 0 else np.nan
    beta = np.clip(beta, -1, 1)

    return alpha, beta, sigma, mu


def scipy_mle(x):
    '''
    SciPy maximum likelihood estimator for alpha-stable parameters.
    Returns (alpha, beta, sigma, mu).

    Parameterisation note:
      levy_stable.fit returns (alpha, beta, loc, scale) in scipy convention.
      We reorder to (alpha, beta, sigma=scale, mu=loc) to match the convention
      used by mcculloch_estimator and koutrouvelis_estimator.

      For raw GPS step lengths, MLE can return extreme negative mu values
      (e.g. -55,000 m) because the symmetric stable distribution is being
      forced onto positive-only data. Pre-filter and log-transform the input
      in the same way as the other estimators before calling this function.
    '''
    alpha, beta, mu, sigma = levy_stable.fit(x, method='mle',
                                             parameterization='S0')
    return alpha, beta, sigma, mu
