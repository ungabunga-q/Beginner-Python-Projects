"""
Simple Linear Regression
-----------------------
Fits a line to data using scikit-learn and plots the result.

Steps for Beginners:
1. Import numpy, matplotlib, and sklearn.linear_model.
2. Create sample data for X and y.
3. Fit a LinearRegression model.
4. Plot the data and the regression line.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 2. Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# 3. Fit model
model = LinearRegression()
model.fit(X, y)

# 4. Plot
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Simple Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
