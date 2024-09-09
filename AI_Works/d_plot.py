import numpy as np  # Import NumPy
import matplotlib.pyplot as plt

# Data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple line plot
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
