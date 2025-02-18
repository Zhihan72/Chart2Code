import matplotlib.pyplot as plt
import numpy as np

cities = ['Solton', 'Sunville', 'Raymont', 'Sunnyridge', 'Heliocity']
years = [2018, 2019, 2020, 2021, 2022]
solar_installs = np.array([
    [40, 20, 65, 50, 35],  # Solton - shuffled
    [70, 30, 45, 25, 55],  # Sunville - shuffled
    [25, 50, 15, 45, 35],  # Raymont - shuffled
    [30, 40, 35, 10, 20],  # Sunnyridge - shuffled
    [48, 24, 60, 12, 36]   # Heliocity - shuffled
])

bar_height = 0.15
y = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))
single_color = '#20B2AA'

for i, city in enumerate(cities):
    ax.barh(y + i * bar_height, solar_installs[i], height=bar_height, label=city, color=single_color)

ax.set_title('Solar Energy Adoption:\nNumber of Solar Panels Installed (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Year', fontsize=13)
ax.set_xlabel('Solar Panels Installed (Hundreds)', fontsize=13)
ax.set_yticks(y + bar_height * 2)
ax.set_yticklabels(years)
ax.legend(title='Cities', fontsize=10, title_fontsize='11')
ax.grid(axis='x', linestyle='--', alpha=0.7)

for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(solar_installs[i, j] + 0.5, y[j] + i * bar_height, str(solar_installs[i, j]), va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.show()