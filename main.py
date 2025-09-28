#!/usr/bin/env python3
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
x = np.array([[1],[2],[3],[4]])
y = np.array([2,4,6,8])

model = LinearRegression()
model.fit(x,y)

print("Prediction for 5:", model.predict([[5]])[0])
