import matplotlib.pyplot as plt
import numpy as np

# Updated yields data with an additional colony
mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]
venus_yields = [18, 19, 17, 20, 19, 21, 22, 20, 19, 21, 18, 20]
europa_yields = [25, 28, 26, 30, 29, 27, 26, 28, 30, 27, 28, 29]
titan_yields = [15, 14, 16, 13, 14, 15, 17, 13, 14, 16, 15, 14]
kepler_yields = [23, 24, 25, 26, 23, 22, 24, 25, 23, 25, 24, 23]
zaphod_yields = [22, 21, 23, 22, 24, 22, 21, 23, 24, 23, 22, 22]

months = np.arange(1, 13)
mars_trend = np.array([20, 21, 22, 23, 24, 23, 24, 23, 22, 23, 22, 23])
venus_trend = np.array([18, 18.5, 19, 20, 19.5, 20.5, 21, 20.5, 20, 20.5, 19, 20])
europa_trend = np.array([25, 26, 27, 28, 29, 28, 28, 28, 29, 29, 28, 28])
titan_trend = np.array([15, 15, 15.5, 14, 14.5, 15.5, 16, 15, 14.5, 15.5, 14.5, 15])
kepler_trend = np.array([23, 23.5, 24, 25, 24.5, 23.5, 24.5, 24.5, 23.5, 24.5, 24, 23.5])
zaphod_trend = np.array([22, 22, 23, 23, 24, 23, 23, 23.5, 24, 23.5, 23, 23])

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Updated box plot with new data
all_yields = [mars_yields, venus_yields, europa_yields, titan_yields, kepler_yields, zaphod_yields]
colony_names = ['Mars', 'Venus', 'Europa', 'Titan', 'Kepler-186f', 'Zaphod']
box = axes[0].boxplot(all_yields, vert=False, patch_artist=True, labels=colony_names, notch=True, whis=1.5)
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#F0E68C']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
axes[0].set_title("Space Farming Yields:\nLunar Corn Across Planetary Colonies", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Yield (metric tons per hectare)")
axes[0].grid(axis='x', linestyle='--', alpha=0.7)

# Updated line plot with new data
axes[1].plot(months, mars_trend, label='Mars', color='#FF9999', marker='o')
axes[1].plot(months, venus_trend, label='Venus', color='#66B3FF', marker='o')
axes[1].plot(months, europa_trend, label='Europa', color='#99FF99', marker='o')
axes[1].plot(months, titan_trend, label='Titan', color='#FFCC99', marker='o')
axes[1].plot(months, kepler_trend, label='Kepler-186f', color='#C2C2F0', marker='o')
axes[1].plot(months, zaphod_trend, label='Zaphod', color='#F0E68C', marker='o')
axes[1].set_title("Monthly Yield Trends for Planetary Colonies", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Yield (metric tons per hectare)")
axes[1].legend(loc='upper left', fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()