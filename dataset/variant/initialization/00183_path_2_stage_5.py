import matplotlib.pyplot as plt
import numpy as np

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

# Place the line plot on the left (axes[0])
axes[0].plot(months, mars_trend, color='#FF9999', marker='o')
axes[0].plot(months, venus_trend, color='#66B3FF', marker='o')
axes[0].plot(months, europa_trend, color='#99FF99', marker='o')
axes[0].plot(months, titan_trend, color='#FFCC99', marker='o')
axes[0].plot(months, kepler_trend, color='#C2C2F0', marker='o')
axes[0].plot(months, zaphod_trend, color='#F0E68C', marker='o')
axes[0].set_title("Planetary Colonies Yield: Monthly Trends", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Tons per Ha (Yield)")

# Place the box plot on the right (axes[1])
all_yields = [mars_yields, venus_yields, europa_yields, titan_yields, kepler_yields, zaphod_yields]
colony_names = ['Mrsa', 'Vnus', 'Eurpa', 'Ttn', 'Kpler-186f', 'Zahpod']
box = axes[1].boxplot(all_yields, vert=False, patch_artist=True, labels=colony_names, notch=True, whis=1.5)
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#F0E68C']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
axes[1].set_title("Harvests from the Cosmos:\nCross-Colony Yield for Corn", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Metrics Tons (Yield)")

plt.tight_layout()
plt.show()