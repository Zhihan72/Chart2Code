import matplotlib.pyplot as plt
import numpy as np

cities = ['Solton', 'Sunville', 'Raymont', 'Sunnyridge', 'Heliocity']
years = [2018, 2019, 2020, 2021, 2022]

# Randomly altered the content within the dataset
solar_installs = np.array([
    [35, 20, 50, 65, 40],
    [30, 70, 45, 25, 55],
    [45, 50, 25, 15, 35],
    [30, 35, 10, 20, 40],
    [60, 36, 12, 24, 48]
])

bar_width = 0.15
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#7D33FF', '#FF33A8']
styles = ['o', '^', 's', 'x', 'D']

for i, city in enumerate(cities):
    ax.bar(x + i * bar_width, solar_installs[i], width=bar_width, label=city, color=colors[i], edgecolor='black', hatch=styles[i])

ax.set_title('Solar Energy Adoption:\nNumber of Solar Panels Installed (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Solar Panels Installed (Hundreds)', fontsize=13)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years)

ax.legend(title='Cities', fontsize=10, title_fontsize='11', loc='upper left', frameon=False)
ax.grid(axis='y', linestyle='-.', alpha=0.5)

for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, solar_installs[i, j] + 0.5, str(solar_installs[i, j]), ha='center', va='bottom', fontsize=9, rotation=45)

plt.tight_layout()
plt.show()