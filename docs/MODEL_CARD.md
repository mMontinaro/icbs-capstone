# Model Card: Black-Box Optimisation (BBO) Surrogate Model

## 1. Basic Details

**Model Name:** GINGER — Gaussian INference for Guided Exploration and Regression  
**Version:** 1.0  
**Description:**    
This model is a Gaussian Process (GP)-based surrogate used to approximate unknown objective functions in a black-box optimisation setting. It is paired with acquisition functions (Expected Improvement and Upper Confidence Bound) to iteratively select new query points under a limited evaluation budget.

The model operates across **eight independent optimisation tasks**, each with different input dimensionality, and is updated sequentially as new data becomes available.

**Developer:**  
Matteo Montinaro (Student)  
Professional Certificate in Machine Learning and Artificial Intelligence  
Imperial College Business School  

**License:**  
Not formally specified (educational use)  

---

## 2. Intended Uses and Limitations

### Intended Uses

- Black-box optimisation under **limited query budgets**
- Studying **exploration vs exploitation trade-offs**
- Benchmarking **surrogate-based optimisation strategies**
- Educational use in **sequential decision-making and optimisation**

---

### Limitations

- Not suitable for:
  - Real-world deployment without domain validation  
  - High-dimensional or highly discontinuous functions  
  - Problems requiring guaranteed global optimality  

- Performance depends heavily on:
  - Assumption of **smoothness** (RBF kernel)
  - Quality and distribution of sampled data  

- The model may:
  - Converge to **local optima**
  - Perform poorly in **sparse or under-explored regions**

---

## 3. Training Data

### Data Source

The model is trained on a **synthetic, sequentially generated dataset** collected through iterative optimisation.

- Number of tasks: 8 functions  
- Input dimensionality: varies (2D to 8D)  

### Data Characteristics

- Data is:
  - **Numerical**
  - **Low-sample**
  - **Sequentially dependent** (not i.i.d.)

- Inputs:
  - Continuous vectors

- Outputs:
  - Scalar objective values  

### Important Notes

- No external datasets (e.g., ImageNet, Wikipedia) are used  
- Data is **not representative of real-world distributions**  
- Sampling is **biased toward high-performing regions** due to optimisation strategy  

---

## 4. Evaluation Metrics

### Primary Metrics

- **Best observed value (per function)**  
- **Improvement over iterations**  
- **Query efficiency** (performance vs number of queries)

| Function    | Best initial output | Best observed value | Best week
| ------      | ----- | ------- | -
| 1 | 7.710875e-16 | 7.710875e-16 | N/A
| 2 | 0.611205 | 0.689719 | 6
| 3 | -0.034835 | -0.027985 | 3
| 4| -4.025542 | 0.439861 | 10
| 5| 1088.859618 | 4708.375108 | 13
| 6| -0.714265 | -0.080502 | 9
| 7| 1.364968 | 2.482543 | 13
| 8| 9.598482 | 9.985306 | 13


### Observed Behaviour

- Early iterations:
  - High variance, low signal  

- Later iterations:
  - Convergence toward **locally optimal regions**
  - Diminishing returns in improvement  

### Limitations of Evaluation

- No ground truth global optimum available  
- No standard metrics like accuracy or F1-score (regression/optimisation setting)  
- No fairness evaluation (no demographic or subgroup data)

---

## 5. Ethical Considerations

### Biases

- **Sampling bias**:
  - Model increasingly focuses on known high-performing regions  
  - Under-explores other areas of the search space  

- **Model bias**:
  - GP with RBF assumes smoothness  
  - May fail on functions with discontinuities or sharp transitions  

---

### Risks

- Overconfidence in:
  - Local optima  
  - Surrogate predictions in sparse regions  

- Misinterpretation:
  - Results may appear optimal but are **not guaranteed globally optimal**

---

### Risk Mitigation Strategies

- Use of:
  - Multiple acquisition functions (EI, UCB)  
  - Controlled exploration alongside exploitation  

- Maintaining:
  - Some level of global search to avoid premature convergence  

- Transparency:
  - Clear documentation of assumptions and limitations  

---

## Additional Notes

This model is part of a **sequential optimisation pipeline**, not a standalone predictive system. Its behaviour is tightly coupled with:

- The data collection process  
- The acquisition strategy  
- The limited query budget  

As a result, performance should be interpreted in context, and conclusions should not be generalized beyond similar constrained optimisation settings.