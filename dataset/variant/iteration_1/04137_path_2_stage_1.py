import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
corn_yield = np.array([5.2, 5.5, 5.8, 6.0, 5.7, 5.9, 6.3, 6.5, 6.1, 6.8])
soybean_yield = np.array([2.1, 2.4, 2.6, 2.9, 2.5, 2.8, 3.1, 3.3, 3.0, 3.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, corn_yield, color='green', linestyle='-', marker='o', linewidth=2, markersize=8)
ax1.plot(years, soybean_yield, color='orange', linestyle='--', marker='s', linewidth=2, markersize=8)

annotations = {
    2015: ('Drought Year', (0, 50)),
    2018: ('Record High Yield', (0, -50))
}

for year, (text, offset) in annotations.items():
    index = np.where(years == year)[0][0]
    ax1.annotate(
        text, 
        (years[index], corn_yield[index]), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='grey'),
        ha='center', fontsize=10, color='darkred'
    )

ax1.set_title("Decade Long Crop Yield Analysis: Corn vs Soybean\n(2010-2019)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Yield (Metric Tons)", fontsize=14, color='black')

ax1.xaxis.set_tick_params(rotation=45)
ax1.yaxis.set_tick_params(labelcolor='black')

plt.tight_layout()
plt.show()