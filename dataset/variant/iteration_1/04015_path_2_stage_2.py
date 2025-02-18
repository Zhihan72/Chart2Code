import matplotlib.pyplot as plt
import numpy as np

cafes = ['Coffee Shops', 'Tea Houses', 'Mixed Beverage Cafés']

revenue_2015 = [250, 180, 200]
revenue_2016 = [265, 190, 210]
revenue_2017 = [300, 210, 220]
revenue_2018 = [320, 230, 250]
revenue_2019 = [340, 240, 260]
revenue_2020 = [360, 260, 270]

years = [2015, 2016, 2017, 2018, 2019, 2020]
revenue = np.array([revenue_2015, revenue_2016, revenue_2017, revenue_2018, revenue_2019, revenue_2020])

# Shuffled colors for different café types
colors = ['#2ca02c', '#1f77b4', '#ff7f0e']

fig, ax1 = plt.subplots(figsize=(12, 6))

width = 0.2
x = np.arange(len(years))

for i, cafe in enumerate(cafes):
    ax1.bar(x - width + i*width, revenue[:, i], width, color=colors[i], alpha=0.75)

for i, cafe in enumerate(cafes):
    ax1.plot(x, revenue[:, i], marker='o', linestyle='-', color=colors[i], linewidth=2.5)
    for j in range(len(years)):
        ax1.text(x[j] + (i-1)*width, revenue[j, i] + 5, str(revenue[j, i]), ha='center', va='bottom', fontsize=10, fontweight='bold', color=colors[i])

ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)

plt.tight_layout()
plt.show()