import matplotlib.pyplot as plt
import numpy as np

# Data with some data groups removed
soil_moisture = np.array([5, 10, 15, 45, 50, 55])
plant_growth = np.array([2, 4, 7, 20, 21, 23])

# Create scatter plot with altered stylistic elements
plt.figure(figsize=(12, 8))
plt.scatter(soil_moisture, plant_growth, color='purple', alpha=0.5, s=120, edgecolor='darkgreen', marker='x')

# Fit a polynomial curve to the data
z = np.polyfit(soil_moisture, plant_growth, 3)
p = np.poly1d(z)
xp = np.linspace(soil_moisture.min(), soil_moisture.max(), 500)
plt.plot(xp, p(xp), color='orange', linestyle='-.', linewidth=3)

# Modify grid, borders and other stylistic elements
plt.grid(True, linestyle=':', linewidth=0.7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()