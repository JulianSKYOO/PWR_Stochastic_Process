import numpy as np

def simulate_gaussian(mu: float = 0.0, sigma: float=1.0, n_steps: int=100):
    '''
    Generates normal increments using Box-Muller method (alpha=2, beta=0)
    :param mu (float): location parameter
    :param sigma: scale parameter
    :param n_steps (int): number of steps to simulate
    :return: np.array - increments following a normal(mu, sigma) distribution
    '''
    u1 = np.random.uniform(0, 1, n_steps)
    u2 = np.random.uniform(0, 1, n_steps)
    # Box-Muller transform
    R = np.sqrt(-2 * np.log(u1))
    X = R * np.cos(2 * np.pi * u2)
    # Y = R * np.sin(2 * np.pi * u2)
    return mu + sigma * X


def simulate_cauchy(mu: float = 0.0, sigma: float=1.0, n_steps: int=100):
    '''
    Generates Cauchy increments (alpha=1, beta=0)
    :param mu (float): location parameter
    :param sigma: scale parameter
    :param n_steps (int): number of steps to simulate
    :return: np.array - increments following a Cauchy(mu, sigma) distribution
    '''
    u = np.random.uniform(0, 1, n_steps)
    z0 = np.tan(np.pi * (u - 0.5))
    return mu + sigma * z0


def simulate_levy(mu: float = 0.0, sigma: float=1.0, n_steps: int=100):
    '''
    Generates Levy increments (alpha=0.5, beta=1)
    :param mu (float): location parameter
    :param sigma: scale parameter
    :param n_steps (int): number of steps to simulate
    :return: np.array - increments following a Levy(mu, sigma) distribution
    '''
    # z = simulate_gaussian(0, 1, n_steps)   # dead code: result immediately
    #                                         # overwritten by the line below,
    #                                         # so this call does nothing.
    #                                         # Removed to avoid confusion.
    z = np.random.normal(0, 1, n_steps)
    return mu + sigma / (z ** 2)


# Chambers-Mallows-Stuck
def simulate_stable(alpha: float, beta: float, sigma=1.0, mu=0., n_steps: int=1000):
    '''
    Implementation of Chambers-Mallows-Stuck method for simulating
    an alpha-stable process.
    :param alpha: stability parameter  (0 < alpha <= 2)
    :param beta:  skewness parameter   (beta in [-1, 1])
    :param sigma: scale parameter      (sigma > 0)
    :param mu:    location parameter
    :param n_steps: number of steps to simulate
    :return: np.array of alpha-stable variates

    Parameterisation note (S0):
      For alpha=2 (Gaussian), Var(X) = 2*sigma^2.
      To obtain N(0,1) you need sigma=sqrt(0.5), NOT sigma=1.
      This is a known quirk of the S0 stable parameterisation.
    '''
    v = np.random.uniform(-np.pi / 2, np.pi / 2, n_steps)
    u = np.random.uniform(0, 1, n_steps)
    w = -np.log(u)   # Exp(1) variates

    if alpha != 1:
        b_ab = (1 / alpha) * np.arctan(beta * np.tan(np.pi * alpha / 2))
        a_ab = (1 + (beta ** 2) * (np.tan(np.pi * alpha / 2) ** 2)) ** (1 / (2 * alpha))

        part1 = np.sin(alpha * (v + b_ab)) / (np.cos(v) ** (1 / alpha))
        part2 = (np.cos(v - alpha * (v + b_ab)) / w) ** ((1 - alpha) / alpha)
        x = a_ab * part1 * part2
    else:
        x = (2/np.pi) * ((np.pi/2 + beta * v) * np.tan(v) -
                           beta * np.log((w * np.cos(v))/(np.pi/2 + beta * v)))

    if alpha != 1:
        return sigma * x + mu
    else:
        return sigma * x + (2 / np.pi) * sigma * np.log(sigma) + mu


def simulate_levy_flight(n_steps=1000, alpha=0.5):
    '''
    Simulates a 2D isotropic Levy flight.
    :param n_steps: number of steps
    :param alpha: stability index controlling tail heaviness (0 < alpha <= 2)
    :return: (x, y, step_lengths)
             x, y         -- cumulative 2D positions
             step_lengths -- positive step lengths used at each step

    Fix note:
    Previously step lengths were drawn as signed stable variates:
        # steps = simulate_stable(alpha, beta=1, n_steps=n_steps)
    For alpha=0.5 this works because the Levy distribution is strictly positive.
    For alpha > 1 with beta=1, simulate_stable can return negative values.
    Using signed values as "step lengths" means the displayed step-length
    distribution (via np.abs(steps) after the fact) does not follow
    P(l) ~ l^{-(1+alpha)} for general alpha, which is the intended power-law.
    The 2D trajectory is statistically equivalent (negative step in direction
    theta == positive step in direction theta+pi, and theta+pi is also uniform),
    but the step-length analysis becomes incorrect for alpha != 0.5.
    Fix: take abs() immediately to guarantee positive step lengths for any alpha.
    '''
    # steps = simulate_stable(alpha, beta=1, n_steps=n_steps)
    # Instead of using signed variates directly, I made the change below:
    # abs() ensures step lengths are always positive for any alpha value,
    # preserving the heavy-power-law tail while eliminating the sign issue.
    step_lengths = np.abs(simulate_stable(alpha, beta=1, n_steps=n_steps))

    angles = np.random.uniform(0, 2 * np.pi, n_steps)

    dx = step_lengths * np.cos(angles)
    dy = step_lengths * np.sin(angles)

    x = np.cumsum(dx)
    y = np.cumsum(dy)

    return x, y, step_lengths


from scipy import stats

def simulate_scipy(alpha, beta, sigma=1.0, mu=0.0, size=2500):
    data = stats.levy_stable.rvs(alpha, beta, loc=mu, scale=sigma, size=size)
    return data
