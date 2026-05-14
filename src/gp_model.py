from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import numpy as np

def fit_model(X, y, kernel, noise=1e-6):
    model = GaussianProcessRegressor(
        kernel=kernel,
        alpha=noise,
        n_restarts_optimizer=9
    )
    model.fit(X, y)
    return model

def generate_candidates(dim, n=5000, lower_bound=0, upper_bound=1):
    #all possible points that could be chosen
    return np.random.uniform(lower_bound, upper_bound, size=(n, dim))

def generate_kernel(length_scale, length_scale_bounds):
    kernel = RBF(
            length_scale=length_scale,
            length_scale_bounds=length_scale_bounds
        )
    return kernel