import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the relationship between Average Temperature, Humidity, and Crop Yield.
# This scatter plot aims to provide insights for farmers and agronomists on optimizing conditions
# for better crop yields.

# Data: Average Temperature (Celsius), Humidity (%), and Crop Yield (tons/hectare)
temperature = np.array([15, 18, 20, 25, 28, 30, 32, 35, 37, 40])
humidity = np.array([80, 75, 70, 65, 62, 60, 55, 50, 48, 45])
crop_yield = np.array([4.5, 4.7, 5.0, 5.5, 6.2, 6.0, 5.8, 5.3, 4.8, 4.0])

# Normalize crop yield for bubble size
crop_yield_normalized = (crop_yield - crop_yield.min()) / (crop_yield.ptp() / 100)

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

scatter = ax.scatter(temperature, humidity, s=crop_yield_normalized*100, c=crop_yield, cmap='viridis', alpha=0.7, edgecolor='k')

# Title and labels
ax.set_title("Impact of Temperature and Humidity on Crop Yield\nin AgroValley", fontsize=16, fontweight='bold')
ax.set_xlabel("Average Temperature (°C)", fontsize=12)
ax.set_ylabel("Humidity (%)", fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Color bar to reflect crop yield
cbar = plt.colorbar(scatter)
cbar.set_label('Crop Yield (tons/hectare)', fontsize=12)

# Annotate specific points
for temp, hum, yield_val in zip(temperature, humidity, crop_yield):
    ax.text(temp, hum, f"{yield_val:.1f}", fontsize=9, ha='right', color='black')

# Automatically adjust layout to fit elements
plt.tight_layout()

# Display the plot
plt.show()