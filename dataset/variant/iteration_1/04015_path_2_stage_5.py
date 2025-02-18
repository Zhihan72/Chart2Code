import matplotlib.pyplot as plt
import numpy as np

cafes = ['Java Houses', 'Hybrid Drink Bars']

revenue_2015 = [250, 200]
revenue_2016 = [265, 210]
revenue_2017 = [300, 220]
revenue_2018 = [320, 250]
revenue_2019 = [340, 260]
revenue_2020 = [360, 270]

years = [2015, 2016, 2017, 2018, 2019, 2020]
revenue = np.array([revenue_2015, revenue_2016, revenue_2017, revenue_2018, revenue_2019, revenue_2020])

colors = ['#2ca02c', '#ff7f0e']

fig, ax1 = plt.subplots(figsize=(12, 6))
height = 0.3
y = np.arange(len(years))

for i, cafe in enumerate(cafes):
    ax1.barh(y + i*height, revenue[:, i], height, color=colors[i], alpha=0.75)
    for j in range(len(years)):
        ax1.text(revenue[j, i] + 5, y[j] + (i-0.5)*height, str(revenue[j, i]), va='center', fontsize=10, fontweight='bold', color=colors[i])

ax1.set_yticks(y + height/2)
ax1.set_yticklabels(years, fontsize=11)

ax1.set_title('Annual Earnings of Selected Cafés', fontsize=14)
ax1.set_xlabel('Income (in Thousands)', fontsize=12)
ax1.set_ylabel('Yearly Overview', fontsize=12)

plt.tight_layout()
plt.show()