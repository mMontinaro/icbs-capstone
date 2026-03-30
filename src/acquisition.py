from scipy.stats import norm

def acquisition_ucb(mu, sigma, beta=1.96):
    # UCB(x) = mu(x) + beta * variance/sigma(x)
    return mu + beta * sigma

def acquisition_ei(mu, sigma, best_Y, xi):
    return (mu - best_Y - xi) / sigma

def acquisition_ei2(mu, sigma, best_Y, xi):
    # this is the 'true' EI. The official function 
    # https://botorch.org/docs/acquisition/
    improvement = mu - best_Y - xi
    z = improvement / sigma
    ei = improvement * norm.cdf(z) + sigma * norm.pdf(z)
    ei[sigma == 0.0] = 0.0
    return ei
