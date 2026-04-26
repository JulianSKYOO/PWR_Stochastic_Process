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
    X =  R* np.cos(2 * np.pi * u2)
   #Y = R * np.sin(2 * np.pi * u2)
    return mu + sigma * X

def simulate_cauchy(mu: float = 0.0, sigma: float=1.0, n_steps: int=100):
    '''
    Generates  Cauchy increments (alpha=1, beta =0)
    :param mu (float): location parameter
    :param sigma: scale parameter
    :param n_steps (int): number of steps to simulate
    :return: np.array - increments following a Cauchy(mu, sigma) distribution
    '''
    u = np.random.uniform(0, 1, n_steps)
    z0 = np.tan(np.pi*(u-0.5))
    return mu + sigma * z0

def simulate_levy(mu: float = 0.0, sigma: float=1.0, n_steps: int=100):
    '''
    Generates  Levy increments (alpha=0.5, beta =1)
    :param mu (float): location parameter
    :param sigma: scale parameter
    :param n_steps (int): number of steps to simulate
    :return: np.array - increments following a Cauchy(mu, sigma) distribution
    '''
    z = simulate_gaussian(0,1,n_steps)
    z = np.random.normal(0, 1, n_steps)
    return mu + sigma/(z**2)

#Chambers-Mallows-Stuck
def simulate_stable(alpha:float, beta:float, sigma=1.0, mu=0., n_steps:int=1000):
    '''
    Implementation of Chambers-Mallows-Stuck method for simulating
    alpha-stable process
    :param n_steps: number of steps to simulate
    :param alpha: stability parameter
    :param beta: skewness parameter
    :param sigma: scale parameter (postive)
    :param mu: location parameter
    :return:
    '''
    v = np.random.uniform(-np.pi/2, np.pi/2, n_steps)
    u = np.random.uniform(0,1, n_steps)
    w = -np.log(u) #exponential

    if alpha != 1:
        b_ab = (1/alpha) * np.arctan(beta *np.tan(np.pi * alpha/2))
        a_ab = (1 + (beta**2) * (np.tan(np.pi * alpha/2)**2))**(1/(2 * alpha))

        part1 = np.sin(alpha * (v + b_ab))/(np.cos(v)**(1/alpha))
        part2 = (np.cos(v - alpha * (v + b_ab))/w)**((1 - alpha)/alpha)
        x = a_ab * part1 * part2
    else:
        x = (2/np.pi) * ((np.pi/2 + beta * v) * np.tan(v) -
                           beta * np.log((w * np.cos(v))/(np.pi/2 + beta * v)))

    return sigma * x + mu if alpha!=1 else sigma * x + (2 /np.pi)*sigma*np.log(sigma)+mu


from scipy import stats
def simulate_scipy(alpha, beta, sigma=1.0, mu=0.0, size=2500):
    data = stats.levy_stable.rvs(alpha, beta, loc=mu, scale=sigma, size=size)
    return data
