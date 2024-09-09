from scipy import optimize

# Define a quadratic function
def quadratic_func(x):
    return x**2 - 4

# Use SciPy's root finder to solve for the roots
roots = optimize.root(quadratic_func, x0=0)
print(f"Roots of the equation: {roots.x}")
