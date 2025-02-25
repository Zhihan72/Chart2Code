import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

action = np.array([650, 600, 500, 700, 550])
comedy = np.array([310, 330, 320, 340, 300])
drama = np.array([470, 450, 460, 480, 400])
sci_fi = np.array([250, 220, 210, 300, 200])
animation = np.array([160, 190, 180, 170, 150])

new_colors = ['#377eb8', '#e41a1c', '#ff7f00', '#4daf4a', '#984ea3']

fig, ax = plt.subplots(figsize=(10, 6))

bottom_values = np.zeros(len(years))

for genre_data, color, label in zip(
    [action, comedy, drama, sci_fi, animation],
    new_colors,
    ['Funny', 'Exciting', 'Emotional', 'Sci-Fi', 'Animated']
):
    ax.bar(years, genre_data, bottom=bottom_values, label=label, color=color, alpha=0.8, edgecolor='black', linewidth=1.5)
    bottom_values += genre_data

ax.set_title('Movie Revenue Analysis (2018-2022)', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Years', fontsize=12, labelpad=8)
ax.set_ylabel('Revenue (Million USD)', fontsize=12, labelpad=8)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=0, ha='center')

ax.legend(title='Genre', loc='upper right', fontsize=9)

ax.grid(axis='x', linestyle='-.', alpha=0.5)

plt.tight_layout()

plt.show()