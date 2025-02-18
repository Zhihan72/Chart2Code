import matplotlib.pyplot as plt
import numpy as np

software_dept = [55, 50, 60, 62, 58, 65, 72, 70, 68, 74, 76, 85, 80]
hardware_dept = [30, 35, 40, 42, 48, 45, 38, 52, 54, 60, 56, 65, 50]
hr_dept = [12, 10, 14, 16, 20, 18, 22, 25, 30, 28, 31, 35, 34]
marketing_dept = [20, 25, 32, 30, 28, 44, 38, 35, 40, 46, 50, 42, 55]
research_dept = [65, 60, 70, 80, 75, 90, 85, 95, 100, 105, 110, 120, 115]

coffee_data = [software_dept, hardware_dept, hr_dept, marketing_dept, research_dept]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(coffee_data, patch_artist=True, vert=True, notch=True,
                boxprops=dict(color='darkblue', linewidth=1.8),
                medianprops=dict(color='lightgreen', linewidth=2),
                whiskerprops=dict(color='darkblue', linewidth=1.8, linestyle='dotted'),
                capprops=dict(color='darkblue', linewidth=1.8),
                flierprops=dict(marker='x', color='red', alpha=0.6, markersize=10))

# New color palette assignment for the boxes
colors = ['#FFA07A', '#8A2BE2', '#7FFFD4', '#FFD700', '#DC143C']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

for i, data in enumerate(coffee_data, start=1):
    x = np.random.normal(i, 0.04, size=len(data))
    y = np.array(data)
    ax.scatter(x, y, alpha=0.75, edgecolor='k', s=60, marker='^')

ax.yaxis.grid(True, linestyle='-.', which='major', color='black', alpha=0.3)

for i, dept in enumerate(coffee_data, start=1):
    mean_val = np.mean(dept)
    ax.axhline(mean_val, ls=':', color=colors[i-1], alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.show()