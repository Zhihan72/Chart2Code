import matplotlib.pyplot as plt
import numpy as np

programs = ['AM Fit', 'PM Yoga', 'WK Hiking', 'Dance', 'WorkWell', 'Stretch Class']
steps_data = [
    [8500, 8700, 7800, 9000, 8800, 8900, 8600, 9100, 9200, 8450],
    [4500, 4200, 4100, 4600, 4700, 4900, 4300, 4800, 4400, 4550],
    [9500, 9600, 9400, 9300, 9200, 9800, 9900, 9700, 9350, 9600],
    [7000, 7500, 7200, 7100, 7350, 7600, 7800, 7400, 7500, 7350],
    [5000, 4800, 4700, 5100, 5200, 5400, 4550, 4900, 5050, 5250],
    [3000, 3200, 3100, 3300, 3250, 3100, 3150, 3400, 3350, 3450]
]

fig, ax = plt.subplots(figsize=(8, 6))

# Alter the stylistic elements of the plot
mean_steps = [np.mean(data) for data in steps_data]
ax.barh(programs, mean_steps, color='#66b3ff', edgecolor='darkgrey', linestyle='dashed', linewidth=2)
ax.set_xlabel('Avg Steps', fontsize=10, color='darkred', fontweight='bold')
ax.set_title('Mean Steps by Program', fontsize=16, fontweight='heavy', pad=30, loc='right')

# Change legend, grid, and markers
ax.grid(True, linestyle='-.', linewidth=0.7, color='grey', alpha=0.5)
ax.invert_yaxis()  # Random alteration: programs from bottom to top
for i, v in enumerate(mean_steps):
    ax.text(v - 500, i, f'{v:.0f}', color='navy', va='center', fontweight='medium')

plt.tight_layout()
plt.show()