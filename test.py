import numpy as np
import matplotlib.pyplot as plt

# Define the quantities of two goods
quantity_good1 = np.linspace(0.1, 10, 100)
quantity_good2 = np.linspace(0.1, 10, 100)

# Define the utility function
def utility_function(good1, good2):
    return np.sqrt(good1) + np.sqrt(good2)

# Create a meshgrid of quantity combinations
good1, good2 = np.meshgrid(quantity_good1, quantity_good2)
utility = utility_function(good1, good2)

# Plot the indifference curve
plt.figure(figsize=(8, 6))
plt.contour(good1, good2, utility, levels=10, cmap='viridis')
plt.xlabel('Good 1')
plt.ylabel('Good 2')
plt.title('Indifference Curve')
plt.colorbar(label='Utility')
plt.grid(True)
plt.show()
