import matplotlib.pyplot as plt
import numpy as np

# Data
temperature = np.array([25, 32, 18, 30, 15, 40, 37, 20, 35, 28])
crop_yield = np.array([5.5, 5.8, 4.7, 6.0, 4.5, 4.0, 4.8, 5.0, 5.3, 6.2])

# Sort data
sorted_indices = np.argsort(crop_yield)
sorted_temperature = temperature[sorted_indices]
sorted_crop_yield = crop_yield[sorted_indices]

# Create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
# New set of colors to replace the original one
new_colors = ['#FFA07A', '#20B2AA', '#778899', '#D2691E', '#8A2BE2', 
              '#FF1493', '#7FFF00', '#DC143C', '#FF8C00', '#8B008B']
ax.bar(sorted_temperature, sorted_crop_yield, color=new_colors, edgecolor='k')

# Labels
ax.set_xlabel("Temp (°C)", fontsize=12)
ax.set_ylabel("Yield (t/ha)", fontsize=12)

# Annotate bars
for x, y in zip(sorted_temperature, sorted_crop_yield):
    ax.text(x, y + 0.1, f"{y:.1f}", fontsize=9, ha='center', color='black')

plt.tight_layout()
plt.show()