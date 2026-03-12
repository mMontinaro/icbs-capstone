# Black-Box Optimization (BBO) Capstone Project

## Project Overview
&emsp;Each participant is given 8 different unknown functions, each of varying dimensionality. Each function accepts a set of input parameters and returns a scalar output.

The internal mechanisms of the function are hidden (hence the black-box). Each week, each participant can submit a query point and receive a response. While the bonus goal is to identify input combinations that maximise outputs efficiently, the real goal is to better prepare the participants to real world ML applications. 

It is relevant in real world ML due to the process of optimizing the model, tuning hyperparameters, and allocating resources efficiently given the limited number of data at the disposal of the participant, effectiely mirroring many real scenarios, where evaluation could be expensive, and present various constraints.

This project aims to better our understanding and improve our solutions by handling black-box systems.

## Inputs and Outputs
Each function receives a vector of numerical inputs and returns a single scalar output:

### Input format
```python
# Method that takes an array, and returns the desired format, meant to be copied and pasted onto the submission form
def print_next_submission(x_next):
    print("-".join(v for v in x_next))

# Example of an array input for a 3 Dimensional Function
next3=[0.739850,0.795225,0.785868]
print_next_submission(next3)
```

&emsp;&emsp;will return

    0.739850-0.795225-0.785868

### Output
A scalar representing a performance. All functions are maximisation problems (some are technically minimisation, but the approach is to perform maximisation and then invert the result).

### Constraints
The main constraint is sparsity of data. Participants are allowed only 1 query per week to each function; therefore, the data set will grow slowly, and minimally each week, leading to the necessity to carefully select the query points

## Challenge Objectives
The primary objective is to find near-optimal inputs for each function while respecting evaluation constraints:
- Efficiently explore the input space to maximise information gain per query.
- Ensure robustness against noise, nonlinearities, and local optima.
- Apply strategies that generalise across multiple function types, from recipe scoring to ML hyperparameter optimisation.

## Technical Approach
### ML Method Selection
I primarily use Bayesian Optimisation (BO):
- Gaussian Process (GP) surrogate to model the unknown function and estimates uncertainty.
- Acquisition functions to select the next input query points:
  - Upper Confidence Bound (UCB): Favors exploration of uncertain regions.
  - Expected Improvement (EI): Targets promising areas while accounting for uncertainty.

### Approach Evolution 
I quickly realized that keeping track of 8 different functions would have been hectic; thus the creation of a single notebook, completely dynamic, optimized for quickly switching acquisition functions, tuning hyperparameters, testing, debugging, appending the previous' weeks' inputs and outputs to the data set cleanly, and proposing the next input points. Many initial comments regarding the evolution of the first few weeks are present within the notebook.

The main approach the first 3 weeks was based upon exploration: I wanted to have a somewhat global coverage. Later queries will shift to exploit promising regions. I tuned hyperparameters like noise and length_scale plenty the first 3 weeks, as well as acquisition parameters (beta for ucb, xi for ei).

### Example Implementation
The following snippet is an example of how a BO is initialized in my project, invoking a class to handle the creation dynamically based on all function specific variables:
```python
bo3 = BayesianOptimizer(x3w3, y3w3, acquisition=acquisition3, beta=beta3, noise=noise3, xi=xi3, length_scale_bounds=length_scale_bounds3)
```

### Insights and Strategy
Functions are highly nonlinear and multimodal, making linear or logistic regression unsuitable.

Considering individual feature effects helps guide initial queries despite surrogate model opacity.

Each week, newly evaluated points are added to refine the GP model and inform subsequent proposals.

Flexibility allows switching acquisition functions, adjusting BO hyperparameters, and incorporating domain knowledge when available.

***
_This README reflects the current status of my BBO project and will be updated as strategies evolve in future weeks._
