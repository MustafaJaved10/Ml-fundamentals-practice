# 📁 ML Fundamentals Practice — Mustafa Javed 


**Subject:** Machine Learning Fundamentals

Practice scripts written while building up the math and tooling behind machine learning — matplotlib visualizations, calculus-based optimization, linear regression from scratch, probability & statistics, and scikit-learn basics.

## 📂 File Index

| # | File | Topic |
|---|------|-------|
| 01 | `matplotlib/matplotlib_practice.py` | Matplotlib — line plots, bar charts, scatter plots, histograms, pie charts |
| 02 | `math-for-ml/3_calculs_Optimazation.py` | Calculus — derivatives, gradients, gradient descent |
| 03 | `math-for-ml/linearReggrsion.py` | Linear Regression — built from scratch using gradient descent |
| 04 | `probability-stats/prob_stact.py` | Probability & Statistics — mean, variance, conditional probability, Bayes' theorem, normal distribution |
| 05 | `scikit-learn/scikit_learn.py` | Scikit-learn — train/test split, LinearRegression, MSE |

## 📄 What's Inside Each File

### `matplotlib/matplotlib_practice.py`
- Basic line plots with titles, axis labels, and custom fonts
- Markers, line styles (dotted, dashed), colors, and line width
- Plotting multiple lines on one graph with `sin(x)` vs `cos(x)` and a legend
- Grid lines (full grid and single-axis grid)
- Subplots — multiple charts in one figure with `plt.subplot()`
- Bar charts (vertical and horizontal) and grouped category comparisons
- Scatter plots (age vs salary example)
- Histograms using `np.random.normal()` for distribution shape
- Pie charts with labels, exploded slices, and legends
- A Pandas + Matplotlib combo: grouping data by city and plotting average salary

### `math-for-ml/3_calculs_Optimazation.py`
- What a derivative means in the context of machine learning (rate of loss change)
- Numerical derivatives using the forward difference method
- Central difference method (more accurate, looks both forward and backward)
- Derivatives of multi-variable functions (partial derivatives for `x` and `y`)
- Connecting derivatives to gradients and weight updates
- A full gradient descent loop: prediction → loss → gradient → weight update
- Manually tracing how loss decreases over multiple training epochs

### `math-for-ml/linearReggrsion.py`
- The linear regression equation `y = mx + b` explained conceptually
- Manually implementing gradient descent for a single data point
- Extending it to a full dataset with NumPy (vectorized weight and bias updates)
- Mean Squared Error as the loss function
- Printing weight, bias, prediction, error, and loss at every training iteration
- Manually calculating predictions for new inputs after training

### `probability-stats/prob_stact.py`
- Descriptive statistics: mean, median, standard deviation, variance, mode
- Basic probability: favorable outcomes over total outcomes (dice, coin flip)
- Simulating probability with `np.random.seed()` and large random samples
- Independent events and how to test for independence
- Conditional probability with a weather/play-cricket dataset example
- Bayes' Theorem — disease testing example and spam email classification example
- Normal distribution basics and visualizing it with a histogram

### `scikit-learn/scikit_learn.py`
- What scikit-learn is and why it replaces manual gradient descent code
- Creating and fitting a `LinearRegression` model with `model.fit(X, y)`
- Splitting data with `train_test_split()` and why `random_state` matters
- Understanding `X_train`, `y_train`, `X_test`, `y_test` roles
- Reading learned weight and bias with `model.coef_` and `model.intercept_`
- Making predictions with `model.predict()`
- Evaluating a model using `mean_squared_error`

## 🔧 How to Run

```bash
python matplotlib/matplotlib_practice.py
python math-for-ml/3_calculs_Optimazation.py
python math-for-ml/linearReggrsion.py
python probability-stats/prob_stact.py
python scikit-learn/scikit_learn.py
```

Install dependencies first:

```bash
pip install numpy matplotlib pandas scikit-learn
```

## 📚 Topics Covered

- Data visualization (line, bar, scatter, histogram, pie charts)
- Subplots and multi-line charts with legends
- Derivatives & numerical differentiation (forward and central difference)
- Gradients & gradient descent
- Linear regression (manual implementation with weight/bias updates)
- Mean Squared Error as a loss function
- Probability rules & independent events
- Conditional probability
- Bayes' theorem (disease testing, spam classification)
- Normal distribution
- Scikit-learn: `train_test_split`, `LinearRegression`, `mean_squared_error`

## 🗂 Folder Structure

```text
ml-fundamentals-practice/
│
├── matplotlib/
│   └── matplotlib_practice.py
│
├── math-for-ml/
│   ├── 3_calculs_Optimazation.py
│   └── linearReggrsion.py
│
├── probability-stats/
│   └── prob_stact.py
│
├── scikit-learn/
│   └── scikit_learn.py
│
└── README.md
```

## 📝 Note

These are learning and practice scripts, not a polished project — many files include commented-out experiments kept intentionally as a record of the learning process. Active, uncommented code at the bottom of each file represents the final working example for that topic.
