import matplotlib.pyplot as plt
import numpy as np

# Data
soil_moisture = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
plant_growth = np.array([2, 4, 7, 9, 13, 15, 16, 18, 20, 21, 23, 24])

# Create scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(soil_moisture, plant_growth, color='cornflowerblue', alpha=0.7, s=100, edgecolor='black')

# Fit a polynomial curve to the data
z = np.polyfit(soil_moisture, plant_growth, 3)
p = np.poly1d(z)
xp = np.linspace(soil_moisture.min(), soil_moisture.max(), 500)
plt.plot(xp, p(xp), color='tomato', linestyle='--', linewidth=2)

# Remove textual elements including labels, titles, legends, and annotations
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()