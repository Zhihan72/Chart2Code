import numpy as np
import matplotlib.pyplot as plt

continents = ['Afr', 'As', 'Eur', 'NA', 'SA']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10],  # Africa
    [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],  # Asia
    [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],   # Europe
    [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35],  # North America
    [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45]  # South America
])

yearly_avg = rainfall_data.mean(axis=0)

fig, ax = plt.subplots(figsize=(15, 9))

# Shuffled colors
colors = ['#ff7f0e', '#2ca02c', '#9467bd', '#1f77b4', '#d62728']

width = 0.15
x = np.arange(len(months))

for i, continent in enumerate(continents):
    ax.bar(x + width * i, rainfall_data[i], width, label=continent, color=colors[i])

ax.plot(x + 2 * width, yearly_avg, marker='o', color='black', label='Yr Avg', linestyle='-')

ax.set_xlabel('Mnths', fontsize=14)
ax.set_ylabel('Rain (mm)', fontsize=14)
ax.set_title('Rainfall by Cont.', fontsize=16, fontweight='bold')

ax.set_xticks(x + width * 2)
ax.set_xticklabels(months, rotation=45, fontsize=12)
ax.yaxis.grid(True)

ax.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()