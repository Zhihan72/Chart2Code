import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

# Random content alterations while keeping the dimensional structure intact
action = np.array([650, 600, 500, 700, 550])
comedy = np.array([310, 330, 320, 340, 300])
drama = np.array([470, 450, 460, 480, 400])
sci_fi = np.array([250, 220, 210, 300, 200])
animation = np.array([160, 190, 180, 170, 150])

new_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

fig, ax = plt.subplots(figsize=(12, 8))

bottom_values = np.zeros(len(years))

for genre_data, color, label in zip(
    [action, comedy, drama, sci_fi, animation],
    new_colors,
    ['Humor', 'Thrill', 'Serious', 'Futuristic', 'Cartoon']
):
    ax.bar(years, genre_data, bottom=bottom_values, label=label, color=color, alpha=0.85)
    bottom_values += genre_data

ax.set_title('Movie Revenue Trends (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14, labelpad=10)
ax.set_ylabel('Earnings (Million USD)', fontsize=14, labelpad=10)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

ax.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()