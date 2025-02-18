import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
languages = ['JavaScript', 'Python', 'Ruby', 'Java', 'C++']
repos_data = np.array([
    [100, 120, 140, 160, 180, 200, 220, 240, 260, 280],  # JavaScript
    [150, 165, 180, 200, 220, 250, 300, 350, 400, 450],  # Python
    [40, 45, 50, 55, 60, 65, 70, 75, 80, 85],            # Ruby
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170],    # Java
    [60, 70, 80, 85, 90, 100, 110, 120, 125, 130]        # C++
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
positions = np.arange(len(years))

for i, language in enumerate(languages):
    ax.bar(positions + i * bar_width, repos_data[i], width=bar_width, label=language)

ax.set_title('GitHub Programming Trends (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Repo Count', fontsize=14)
ax.set_xticks(positions + bar_width * (len(languages) / 2))
ax.set_xticklabels(years, rotation=45)
ax.legend(title='Code Languages', fontsize=12)

for i, repos in enumerate(repos_data):
    max_repo = max(repos)
    year_max = years[repos.argmax()]
    ax.annotate(f'{max_repo}', 
                xy=(year_max - 2013 + i * bar_width, max_repo), 
                xycoords='data', 
                xytext=(0, 5), 
                textcoords='offset points', 
                ha='center', 
                fontsize=9,
                fontstyle='italic')

ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()