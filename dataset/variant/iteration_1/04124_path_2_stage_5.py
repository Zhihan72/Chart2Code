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

fig, ax = plt.subplots(figsize=(10, 8))

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33']

height = 0.12
y = np.arange(len(months))

for i in range(len(continents)):
    ax.barh(y + height * i, rainfall_data[i], height, color=colors[i], label=continents[i])

ax.plot(yearly_avg, y + 2.5 * height, marker='o', color='black', linestyle='-')

ax.set_ylabel('Months', fontsize=12)
ax.set_xlabel('Rainfall (mm)', fontsize=12)
ax.set_title('Avg Rainfall', fontsize=14, fontweight='bold')

ax.set_yticks(y + 2.5 * height)
ax.set_yticklabels(months, fontsize=10)
ax.invert_yaxis()
ax.legend(title='Continents', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()