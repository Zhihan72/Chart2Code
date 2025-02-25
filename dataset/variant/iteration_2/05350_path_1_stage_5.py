import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
languages = ['JavaScript', 'Python', 'Java']
repos_data = np.array([
    [100, 120, 140, 160, 180, 200, 220, 240, 260, 280],  # JavaScript
    [150, 165, 180, 200, 220, 250, 300, 350, 400, 450],  # Python
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170]     # Java
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15
positions = np.arange(len(years))

for i, language in enumerate(languages):
    ax.barh(positions + i * bar_height, repos_data[i], height=bar_height, color='blue', label=language)

ax.set_title('GitHub Programming Trends (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Timeline', fontsize=14)
ax.set_xlabel('Repo Count', fontsize=14)
ax.set_yticks(positions + bar_height * (len(languages) / 2))
ax.set_yticklabels(years)
ax.legend(title='Code Languages', fontsize=12, loc='lower right', borderaxespad=1.5, edgecolor='blue', facecolor='lightgrey')

ax.grid(axis='x', linestyle='--', color='orange', alpha=0.4)

plt.tight_layout()
plt.show()