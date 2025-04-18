import numpy as np
import matplotlib.pyplot as plt

continents = ['Afr', 'As', 'Eur', 'NA', 'SA', 'Oce', 'Ant']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10],   # Africa
    [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],   # Asia
    [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],    # Europe
    [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35],   # North America
    [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45],  # South America
    [50, 45, 55, 50, 45, 55, 50, 45, 55, 50, 45, 55],   # Oceania
    [10, 10, 15, 20, 25, 30, 35, 40, 35, 30, 25, 20]    # Antarctica
])

yearly_avg = rainfall_data.mean(axis=0)

fig, ax = plt.subplots(figsize=(15, 9))

colors = ['#ff7f0e', '#2ca02c', '#9467bd', '#1f77b4', '#d62728', '#8c564b', '#e377c2']

height = 0.1
y = np.arange(len(months))

for i, continent in enumerate(continents):
    ax.barh(y + height * i, rainfall_data[i], height, color=colors[i])

ax.plot(yearly_avg, y + height * 3, marker='o', color='black', linestyle='-')

ax.set_ylabel('Mnths', fontsize=14)
ax.set_xlabel('Rain (mm)', fontsize=14)
ax.set_title('Rainfall by Cont.', fontsize=16, fontweight='bold')

ax.set_yticks(y + height * 3)
ax.set_yticklabels(months, fontsize=12)
# ax.xaxis.grid(True)

# ax.legend(loc='upper right', fontsize=12)

# Remove the border by turning off the spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()