import matplotlib.pyplot as plt
import numpy as np

# Data: Average Temperature (Celsius) and Crop Yield (tons/hectare)
temperature = np.array([25, 32, 18, 30, 15, 40, 37, 20, 35, 28])  # Shuffled
crop_yield = np.array([5.5, 5.8, 4.7, 6.0, 4.5, 4.0, 4.8, 5.0, 5.3, 6.2])  # Shuffled

# Sort data by crop yield in ascending order
sorted_indices = np.argsort(crop_yield)
sorted_temperature = temperature[sorted_indices]
sorted_crop_yield = crop_yield[sorted_indices]

# Create bar chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(sorted_temperature, sorted_crop_yield, color='skyblue', edgecolor='k')

# Title and labels
ax.set_xlabel("Average Temperature (°C)", fontsize=12)
ax.set_ylabel("Crop Yield (tons/hectare)", fontsize=12)

# Annotate bars with crop yield values
for x, y in zip(sorted_temperature, sorted_crop_yield):
    ax.text(x, y + 0.1, f"{y:.1f}", fontsize=9, ha='center', color='black')

plt.tight_layout()
plt.show()