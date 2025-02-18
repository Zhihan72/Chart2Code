import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
repos_data = np.array([
    [150, 165, 180, 200, 220, 250, 300, 350, 400, 450],
    [100, 120, 140, 160, 180, 200, 220, 240, 260, 280],
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170],
    [60, 70, 80, 85, 90, 100, 110, 120, 125, 130],
    [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
])

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15
positions = np.arange(len(years))

# Manually shuffled colors
colors = ['cyan', 'magenta', 'orange', 'purple', 'green']

for i, language in enumerate(languages):
    ax.bar(positions + i * bar_width, repos_data[i], width=bar_width, color=colors[i])

ax.set_title('Popularity of Programming Languages on GitHub (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Number of Repositories', fontsize=14)
ax.set_xticks(positions + bar_width * (len(languages) / 2))
ax.set_xticklabels(years, rotation=45)

plt.show()