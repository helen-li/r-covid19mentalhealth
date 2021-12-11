"""
sample linear regression
"""
# import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression

# provide data. x is the input and y is the output
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# create a model and fit it
model = LinearRegression().fit(x, y)

# get results
r_sq = model.score(x, y)

# predict response
y_pred = model.predict(x)
