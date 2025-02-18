import matplotlib.pyplot as plt
import numpy as np

cafes = ['Coffee', 'Tea']

revenue_2015 = [250, 180]
revenue_2016 = [265, 190]
revenue_2017 = [300, 210]
revenue_2018 = [320, 230]
revenue_2019 = [340, 240]
revenue_2020 = [360, 260]

years = [2015, 2016, 2017, 2018, 2019, 2020]
revenue = np.array([revenue_2015, revenue_2016, revenue_2017, revenue_2018, revenue_2019, revenue_2020])

colors = ['#2ca02c', '#1f77b4']

fig, ax1 = plt.subplots(figsize=(10, 8))

fig.suptitle('Café Revenue (2015-2020)', fontsize=16, fontweight='bold', color='darkslategray')
ax1.set_title('Revenue in USD Thousands', fontsize=14, color='indigo')
ax1.set_xlabel('Revenue ($K)', fontsize=12, labelpad=10)
ax1.set_ylabel('Year', fontsize=12, labelpad=10)

height = 0.2
y = np.arange(len(years))

for i, cafe in enumerate(cafes):
    ax1.barh(y - height/2 + i*height, revenue[:, i], height, label=cafe, color=colors[i], alpha=0.75, edgecolor='black')

for i, cafe in enumerate(cafes):
    ax1.plot(revenue[:, i], y, marker='o', linestyle='-', color=colors[i], linewidth=2.5)
    for j in range(len(years)):
        ax1.text(revenue[j, i] + 5, y[j] + (i-0.5)*height, str(revenue[j, i]), ha='left', va='center', fontsize=10, fontweight='bold', color=colors[i])

ax1.set_yticks(y)
ax1.set_yticklabels(years, fontsize=11)
ax1.legend(loc='lower right', fontsize=11, title='Types', title_fontsize='13')

ax1.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()