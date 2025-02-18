import matplotlib.pyplot as plt
import numpy as np

# Data: Average Temperature (Celsius) and Crop Yield (tons/hectare)
temperature = np.array([15, 18, 20, 25, 28, 30, 32, 35, 37, 40])
crop_yield = np.array([4.5, 4.7, 5.0, 5.5, 6.2, 6.0, 5.8, 5.3, 4.8, 4.0])

# Sort data by crop yield in ascending order
sorted_indices = np.argsort(crop_yield)
sorted_temperature = temperature[sorted_indices]
sorted_crop_yield = crop_yield[sorted_indices]

# Create bar chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(sorted_temperature, sorted_crop_yield, color='skyblue', edgecolor='k')

# Title and labels
ax.set_title("Crop Yield Sorted by Temperature\nin AgroValley", fontsize=16, fontweight='bold')
ax.set_xlabel("Average Temperature (°C)", fontsize=12)
ax.set_ylabel("Crop Yield (tons/hectare)", fontsize=12)

# Annotate bars with crop yield values
for x, y in zip(sorted_temperature, sorted_crop_yield):
    ax.text(x, y + 0.1, f"{y:.1f}", fontsize=9, ha='center', color='black')

# Automatically adjust layout to fit elements
plt.tight_layout()

# Display the plot
plt.show()