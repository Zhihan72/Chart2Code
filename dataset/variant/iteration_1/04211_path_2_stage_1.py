import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
fruit_types = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

usage_data = np.array([
    [150, 160, 170, 180, 190],  # Apple
    [140, 135, 150, 160, 155],  # Banana
    [50, 55, 60, 65, 80],       # Cherry
    [40, 45, 50, 55, 70],       # Date
    [30, 35, 40, 45, 60]        # Elderberry
])

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15

positions = [np.arange(len(years))]
for _ in range(1, len(fruit_types)):
    positions.append([p + bar_width for p in positions[-1]])

# Use a single color for all fruit types
color = '#3498db'

for i, fruit in enumerate(fruit_types):
    ax.bar(positions[i], usage_data[i], bar_width, alpha=0.8, label=fruit, color=color)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage Instances', fontsize=12)
ax.set_title('Fruit Usage in Consumer Products Over 5 Years', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels(years)
ax.legend(title='Fruit Types', fontsize=10)

plt.tight_layout()
plt.show()