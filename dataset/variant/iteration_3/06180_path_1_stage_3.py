import matplotlib.pyplot as plt
import numpy as np

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

tomatoes_yield = np.array([18, 21, 14, 17, 15, 23, 20, 16, 19, 22])
carrots_yield = np.array([17, 14, 13, 15, 12, 19, 16, 14, 18, 19])
broccoli_yield = np.array([14, 15, 9, 10, 8, 13, 12, 11, 14, 10])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, tomatoes_yield, marker='o', linestyle='-', color='mediumvioletred', linewidth=2, label='Juicy Tomatoes')
ax.plot(years, carrots_yield, marker='s', linestyle='-', color='gold', linewidth=2, label='Fresh Carrots')
ax.plot(years, broccoli_yield, marker='^', linestyle='-', color='mediumseagreen', linewidth=2, label='Green Broccoli')

annotations = {
    'Tomatoes': (2022, 23),
    'Carrots': (2022, 19),
    'Broccoli': (2021, 15),
}
for veg, (year, value) in annotations.items():
    ax.annotate(
        f'Spike: {value} tons',
        xy=(year, value),
        xytext=(-30, 10),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='black'),
        fontsize=10,
        color='black'
    )

ax.set_title('Crop Yield Patterns in Greenvale (2013-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Harvest Yield (tons)', fontsize=12)
ax.set_xticks(years)
ax.set_ylim(0, 25)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()