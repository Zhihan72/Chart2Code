import matplotlib.pyplot as plt
import numpy as np

# Synthetic temperature differences (in Celsius) for a week in one city
data = [-5, -3, 0, 2, 1, -1, -4, 3, 2, 0, -2, -3, 1, 2, -3]

plt.figure(figsize=(8, 6))

# Create the violin plot
violin = plt.violinplot(data, vert=False, showmeans=False, showmedians=True)

# Title and labels
plt.title('Temperature Variability During the Week in a Fictional City', fontsize=14, fontweight='bold')
plt.xlabel('Temperature Change (°C)', fontsize=12)
plt.yticks([1], ['City'])

# Grid for readability
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()