import matplotlib.pyplot as plt
import numpy as np

cities = ['Sunnydale', 'Heliopolis', 'Shadytown', 'Brightfield', 'Solitaire']
years = [2020, 2019, 2021, 2018, 2022]

# Randomly changed solar installation data
solar_installs = np.array([
    [45, 30, 55, 75, 50],
    [40, 80, 35, 20, 65],
    [50, 55, 30, 25, 45],
    [35, 40, 15, 30, 50],
    [75, 46, 18, 28, 58]
])

bar_width = 0.15
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#7D33FF', '#FF33A8']
styles = ['o', '^', 's', 'x', 'D']

for i, city in enumerate(cities):
    ax.bar(x + i * bar_width, solar_installs[i], width=bar_width, label=city, color=colors[i], edgecolor='black', hatch=styles[i])

# Randomly altered titles and labels
ax.set_title('Renewable Energy Expansion:\nInstalled Solar Control Units (2020-2024)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Installation Year', fontsize=13)
ax.set_ylabel('Control Units Installed (Hundreds)', fontsize=13)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years)

ax.legend(title='Regional Areas', fontsize=10, title_fontsize='11', loc='upper left', frameon=False)
ax.grid(axis='y', linestyle='-.', alpha=0.5)

for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, solar_installs[i, j] + 0.5, str(solar_installs[i, j]), ha='center', va='bottom', fontsize=9, rotation=45)

plt.tight_layout()
plt.show()