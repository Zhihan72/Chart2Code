import matplotlib.pyplot as plt
import numpy as np

languages = ['C++', 'Java', 'Python', 'Ruby', 'JavaScript', 'Go', 'Swift']
repos_data = np.array([
    [60, 70, 80, 85, 90, 100, 110, 120, 125, 130],  # C++
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170],  # Java
    [150, 165, 180, 200, 220, 250, 300, 350, 400, 450],  # Python
    [40, 45, 50, 55, 60, 65, 70, 75, 80, 85],  # Ruby
    [100, 120, 140, 160, 180, 200, 220, 240, 260, 280],  # JavaScript
    [30, 50, 70, 90, 110, 130, 150, 170, 190, 210],  # Go (New)
    [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]  # Swift (New)
])

total_repos = repos_data.sum(axis=1)
sorted_indices = np.argsort(-total_repos)
sorted_languages = [languages[i] for i in sorted_indices]
sorted_repos_data = [total_repos[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.4
positions = np.arange(len(languages))

colors = ['purple', 'orange', 'cyan', 'green', 'magenta', 'brown', 'blue']

ax.bar(positions, sorted_repos_data, width=bar_width, color=[colors[i] for i in sorted_indices])

ax.set_title('Total Repository Counts by Language (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Languages', fontsize=14)
ax.set_ylabel('Total Repos Count', fontsize=14)
ax.set_xticks(positions)
ax.set_xticklabels(sorted_languages, rotation=45)

plt.show()