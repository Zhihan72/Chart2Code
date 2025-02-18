import numpy as np
import matplotlib.pyplot as plt

continents = ['Afr', 'Asia', 'Eur', 'N. Am', 'S. Am', 'Aus']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10],
    [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],
    [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
    [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35],
    [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45],
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
])

yearly_avg = rainfall_data.mean(axis=0)

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

width = 0.12
x = np.arange(len(months))

for i in range(len(continents)):
    ax.bar(x + width * i, rainfall_data[i], width, color=colors[i])

ax.plot(x + 2.5 * width, yearly_avg, marker='o', color='black', linestyle='-')

ax.set_xlabel('Mnths', fontsize=12)
ax.set_ylabel('Rainfall (mm)', fontsize=12)
ax.set_title('Avg Rainfall', fontsize=14, fontweight='bold')

ax.set_xticks(x + 2.5 * width)
ax.set_xticklabels(months, rotation=45, fontsize=10)

plt.tight_layout()
plt.show()