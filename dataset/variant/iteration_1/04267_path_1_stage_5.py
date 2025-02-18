import matplotlib.pyplot as plt
import numpy as np

# Synthetic temperature differences (in Celsius) for a week in one city
data = [-5, -3, 0, 2, 1, -1, -4, 3, 2, 0, -2, -3, 1, 2, -3]

plt.figure(figsize=(8, 6))

# Create the violin plot with a new set of colors
violin = plt.violinplot(data, vert=False, showmeans=True, showmedians=False)

# Customize the colors of the violin plot
for pc in violin['bodies']:
    pc.set_facecolor('lightblue')
    pc.set_edgecolor('blue')
    pc.set_alpha(0.7)

violin['cmeans'].set_edgecolor('green')
violin['cmeans'].set_linewidth(2)

# Change title and labels
plt.title('Enigmatic Climate Variations over Time', fontsize=16, fontweight='normal')
plt.xlabel('Temperature Shift (°C)', fontsize=13)
plt.yticks([1], ['Unknown Region'])

# Modify grid and border style
plt.grid(visible=True, axis='y', linestyle='-.', alpha=0.3)
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()