import numpy as np
from gp_model import fit_model, generate_candidates, generate_kernel
from acquisition import acquisition_ei, acquisition_ucb

def print_next_submission(x_next):
    print("The next points to be submitted are: ")
    print("-".join(v for v in x_next))

class BayesianOptimizer:
    def __init__(self, X, Y, acquisition="ucb", beta=2.0, length_scale=0.2, noise=1e-6, xi=0.01, length_scale_bounds="fixed"):
        self.X = X
        self.Y = Y
        self.acquisition = acquisition
        self.beta = beta
        self.length_scale = length_scale
        self.noise = noise
        self.xi = xi
        self.length_scale_bounds = length_scale_bounds


        kernel = generate_kernel(self.length_scale,self.length_scale_bounds)
        self.gp = fit_model(self.X, self.Y, kernel, self.noise)

    def propose(self, n_candidates=5000, lower_bound=0, upper_bound=1, scale=0.2):
        X_cand = ...
        mu=...
        sigma = ...

        if self.acquisition == "ucb":
            X_cand = generate_candidates(self.X.shape[1], n_candidates, lower_bound, upper_bound)
            mu, sigma = self.gp.predict(X_cand, return_std=True)
            scores = acquisition_ucb(mu, sigma, self.beta)
        elif self.acquisition == "ei":
            dim = self.X.shape[1]
            # --- 1. Find current best point ---
            best_idx = np.argmax(self.Y)
            x_best = self.X[best_idx]
            local_candidates = np.random.normal(loc=x_best, scale=scale, size=(n_candidates, dim))
            X_cand = np.clip(local_candidates, lower_bound, upper_bound)
            mu, sigma = self.gp.predict(X_cand, return_std=True)
            best_Y = np.max(self.Y)
            scores = acquisition_ei(mu, sigma, best_Y, xi=self.xi)
        else:
            raise ValueError("Unsupported acquisition")

        x_next = X_cand[np.argmax(scores)]
        return tuple(f"{v:.6f}" for v in x_next)