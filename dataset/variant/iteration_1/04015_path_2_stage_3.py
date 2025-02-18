import matplotlib.pyplot as plt
import numpy as np

# Only keep the relevant cafes
cafes = ['Coffee Shops', 'Mixed Beverage Cafés']

# Updated revenue data, removing the Tea Houses data
revenue_2015 = [250, 200]
revenue_2016 = [265, 210]
revenue_2017 = [300, 220]
revenue_2018 = [320, 250]
revenue_2019 = [340, 260]
revenue_2020 = [360, 270]

years = [2015, 2016, 2017, 2018, 2019, 2020]
revenue = np.array([revenue_2015, revenue_2016, revenue_2017, revenue_2018, revenue_2019, revenue_2020])

# Updated colors for the two remaining café types
colors = ['#2ca02c', '#ff7f0e']

fig, ax1 = plt.subplots(figsize=(12, 6))

width = 0.3  # Adjusted width for spacing with fewer bars
x = np.arange(len(years))

for i, cafe in enumerate(cafes):
    ax1.bar(x - width/2 + i*width, revenue[:, i], width, color=colors[i], alpha=0.75)

for i, cafe in enumerate(cafes):
    ax1.plot(x, revenue[:, i], marker='o', linestyle='-', color=colors[i], linewidth=2.5)
    for j in range(len(years)):
        ax1.text(x[j] + (i-0.5)*width, revenue[j, i] + 5, str(revenue[j, i]), ha='center', va='bottom', fontsize=10, fontweight='bold', color=colors[i])

ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)

plt.tight_layout()
plt.show()