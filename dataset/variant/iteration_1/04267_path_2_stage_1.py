import matplotlib.pyplot as plt
import numpy as np

# Synthetic temperature differences (in Celsius) for a week in different cities combined into one group
data = [-5, -3, 0, 2, 1, -1, -4, 3, 2, 0, -2, -3, 1, 2, -3, 0, 3, -1, 4, 3, -2, 0, 3, -1, 2, 3, -1, -2, 1, 2, 
        2, 4, 5, 6, 7, 6, 5, 4, 4, 5, 6, 7, 6, 5, 4, 10, 15, 13, 14, 12, 13, 15, 14, 12, 10, 11, 12, 13, 14, 12, 
        -10, -8, -9, -7, -8, -9, -11, -12, -9, -8, -10, -7, -5, -6, -8]

plt.figure(figsize=(8, 6))

# Create the violin plot for the single combined data group
plt.violinplot(data, vert=False, showmeans=False, showmedians=True)

# Title and labels
plt.title('Temperature Variability During the Week\nCombined Data Group', fontsize=16, fontweight='bold')
plt.xlabel('Temperature Change (°C)', fontsize=12)
plt.yticks([1], ['Combined Cities'], fontsize=10)

# Grid for readability
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()