import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the early 22nd century, a series of automated gardens were implemented in an attempt to understand the correlation between autonomous plant growth and soil moisture levels in a controlled environment.

# Title: Autonomous Gardens: Soil Moisture vs. Plant Growth

# Data:
# Soil moisture levels (%) in various sections of the garden over time
soil_moisture = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

# Corresponding plant growth heights (cm) in those sections
plant_growth = np.array([2, 4, 7, 9, 13, 15, 16, 18, 20, 21, 23, 24])

# Create scatter plot
plt.figure(figsize=(12, 8))

plt.scatter(soil_moisture, plant_growth, color='seagreen', alpha=0.7, s=100, edgecolor='black', label='Growth Data')

# Fit a polynomial curve to the data
z = np.polyfit(soil_moisture, plant_growth, 3)
p = np.poly1d(z)
xp = np.linspace(soil_moisture.min(), soil_moisture.max(), 500)
plt.plot(xp, p(xp), color='chocolate', linestyle='--', linewidth=2, label='Fitted Curve')

# Adding Plot Details
plt.title('Autonomous Gardens: Soil Moisture vs. Plant Growth', fontsize=16, fontweight='bold')
plt.xlabel('Soil Moisture (%)', fontsize=14)
plt.ylabel('Plant Growth (cm)', fontsize=14)
plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

# Text annotation to highlight key information
plt.annotate('Optimal Growth',
             xy=(30, 15),
             xytext=(35, 20),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='darkred')

# Automatically adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()