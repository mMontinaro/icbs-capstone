# Datasheet for Black-Box Optimisation (BBO) Capstone Project

## 1. Motivation

This dataset was created to support the task of **black-box optimisation (BBO)**, where the goal is to identify input configurations that maximise an unknown function using a limited number of queries. The dataset captures iterative observations of multiple unknown functions, enabling analysis of optimisation strategies under constrained sampling conditions.

The dataset was created by a student as part of a **machine learning and AI certification capstone project**, with the aim of developing and evaluating efficient optimisation strategies using surrogate models. The primary motivation is educational and experimental: to understand how different optimisation techniques behave in low-data regimes and to simulate decision-making under uncertainty.

The dataset was developed as part of a Professional Certificate in Machine Learning and Artificial Intelligence offered by Imperial College Business School, and is therefore supported within an academic training context rather than external funding.

---

## 2. Composition

The dataset consists of **input-output pairs** collected across multiple rounds of optimisation.

### Data Format
The dataset is collected and stored in a two-stage structure:

Weekly input format (raw data)
Each week, a .txt file is provided where:
Each line represents one full submission
Each submission is a list of NumPy arrays
Each array corresponds to one function
Each array contains the input vector for that function

Example (Week 1):

[array([x₁, x₂]),
 array([x₁, x₂]),
 array([x₁, x₂, x₃]),
 ...
 array([x₁, ..., x₈])]

### Structure
- Number of functions: 8  
* Number of data points / Input dimensionality per function: 
  * Function 1: 22 / 2D
  * Function 2: 22 / 2D
  * Function 3: 27 / 3D
  * Function 4: 42 / 4D
  * Function 5: 32 / 4D
  * Function 6: 32 / 5D
  * Function 7: 42 / 6D
  * Function 8: 52 / 8D

- Total data points: 271 
- Input format: numerical vectors (e.g., x₁, x₂, x₃, x₄)
- Output format: scalar numerical value (objective function output)

Each data point represents:

(x₁, x₂, ..., xₙ) → y

### Completeness and Gaps
- The dataset is **sparse by design**, due to limited query budgets  
- Large portions of the input space remain **unexplored**  
- Sampling is **non-uniform**, with higher density around promising regions  

There are no known issues related to:
- Missing values (all queries produce outputs)  
- Sensitive or personal data (purely synthetic/numerical)

No explicit train/test split is defined, as the dataset is used iteratively rather than for supervised learning.

---

## 3. Collection Process

Data was collected through an **iterative optimisation process** over multiple weeks.

### Strategy
Queries were generated using:
- **Gaussian Process (GP) surrogate model**
- **RBF kernel**
- Acquisition functions:
  - Expected Improvement (EI)
  - Upper Confidence Bound (UCB)

The process followed a loop:
1. Fit surrogate model on existing data  
2. Generate candidate points  
3. Select next query using acquisition function  
4. Evaluate function and append result  

### Sampling Approach
- Early rounds: broader exploration  
- Later rounds: local refinement around high-performing regions  

This results in a **biased sampling distribution**, favouring exploitation over time.

### Time Frame
- Data collected over ~11 weekly iterations  
[<confirm exact duration if needed>]

No human subjects were involved, so:
- No consent or ethical review was required  
- No privacy concerns are present  

---

## 4. Preprocessing and Uses

### Preprocessing

The dataset is assumed to be either:
- Used in raw form  
- Or lightly transformed (e.g., normalization of inputs)

[<specify whether inputs were normalized, scaled, or transformed>]

No tokenisation or feature engineering beyond numerical representation is involved.

It is unclear whether:
- Raw data is preserved alongside processed data  
[<confirm if both versions are stored>]

---

### Intended Uses

- Evaluation of **black-box optimisation strategies**
- Studying **exploration vs exploitation trade-offs**
- Benchmarking **surrogate model performance in low-data regimes**

### Inappropriate Uses

- Not suitable for:
  - Real-world deployment decisions  
  - Any domain requiring validated or representative data  
- Not representative of real-world distributions (synthetic/unknown functions)

### Risks and Biases

- Strong **sampling bias** toward high-performing regions  
- Limited coverage may lead to **incorrect assumptions about global optima**  
- Results are dependent on **model assumptions (e.g., smoothness)**  

---

## 5. Distribution and Maintenance

### Distribution

The dataset is assumed to be stored:
- In a local or version-controlled environment (e.g., GitHub repository)  
[<specify exact location or repository link>]

Availability:
- Likely private or shared within course context  
[<confirm public/private access>]

License:
- No formal license specified  
[<add license if applicable>]

No fees or access restrictions are known.

---

### Maintenance

The dataset is maintained by the original creator as part of the capstone project.

Maintenance includes:
- Weekly updates with new query points  
- Iterative refinement of dataset  

Versioning:
- Likely tracked through:
  - Git commits  
  - or manual versioning  
[<confirm version control method>]

Future updates:
- Dataset may be frozen after project completion  
- No long-term maintenance plan currently defined  

---

## Additional Notes

This dataset reflects a **process-driven collection method**, where data is not sampled independently but generated sequentially based on prior observations. As a result, it encodes both:
- The behaviour of the underlying functions  
- The biases of the optimisation strategy  

Understanding this interaction is critical when interpreting results.