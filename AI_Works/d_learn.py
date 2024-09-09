from sklearn.linear_model import LinearRegression
import numpy as np

# Data: X represents the years of experience, y represents the salary
X = np.array([[1], [2], [3], [4], [5]])  # Features (Years of Experience)
y = np.array([40000, 50000, 60000, 70000, 80000])  # Target (Salary)

# Create a linear regression model and fit the data
model = LinearRegression()
model.fit(X, y)

# Predict the salary for 6 years of experience
predicted_salary = model.predict([[6]])
print(f"Predicted salary for 6 years of experience: {predicted_salary[0]}")
