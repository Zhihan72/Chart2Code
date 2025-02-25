import matplotlib.pyplot as plt
import numpy as np

cities = ['Solton', 'Sunville', 'Raymont', 'SunnyR', 'Helio']
years = [2018, 2019, 2020, 2021, 2022]
solar_installs = np.array([
    [40, 20, 65, 50, 35],
    [70, 30, 45, 25, 55],
    [25, 50, 15, 45, 35],
    [30, 40, 35, 10, 20],
    [48, 24, 60, 12, 36]
])

bar_height = 0.15
y = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))
single_color = '#20B2AA'

for i, city in enumerate(cities):
    ax.barh(y + i * bar_height, solar_installs[i], height=bar_height, color=single_color)

ax.set_title('Solar Panel Installs (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Yr', fontsize=13)
ax.set_xlabel('Installs (100s)', fontsize=13)
ax.set_yticks(y + bar_height * 2)
ax.set_yticklabels(years)

for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(solar_installs[i, j] + 0.5, y[j] + i * bar_height, str(solar_installs[i, j]), va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.show()