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

bar_width = 0.15
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))
single_color = '#20B2AA'

for i, city in enumerate(cities):
    ax.bar(x + i * bar_width, solar_installs[i], width=bar_width, label=city, color=single_color)

ax.set_title('Solar Energy Adoption:\nNumber of Solar Panels Installed (2018-2022)', fontsize=16, fontweight='bold', pad=20, wrap=True)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Solar Panels Installed (Hundreds)', fontsize=13)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title='Cities', fontsize=10, title_fontsize='11')
ax.grid(axis='y', linestyle='--', alpha=0.7)

for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, solar_installs[i, j] + 0.5, str(solar_installs[i, j]), ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()