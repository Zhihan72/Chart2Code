import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])

# Shuffled data values for each streaming category
movies_streaming = np.array([6, 5, 7, 5, 8, 7])
tv_series_streaming = np.array([12, 11, 9, 12, 6, 11])
music_streaming = np.array([5, 11, 3, 4, 7, 9])
podcast_streaming = np.array([4, 7, 5, 3, 6, 2])

total_streaming = movies_streaming + tv_series_streaming + music_streaming + podcast_streaming

fig, ax = plt.subplots(figsize=(14, 9))

def gradient_fill(x, y, ax=None, label=None, color='blue', alpha=0.7):
    if ax is None:
        ax = plt.gca()
    line, = ax.plot(x, y, color=color, alpha=alpha, linewidth=2.5)
    ax.fill_between(x, 0, y, color=color, alpha=alpha*0.4, label=label)
    return line

gradient_fill(years, movies_streaming, ax=ax, label='Movies', color='#FF6347')
gradient_fill(years, movies_streaming + tv_series_streaming, ax=ax, label='TV Series', color='#4682B4')
gradient_fill(years, movies_streaming + tv_series_streaming + music_streaming, ax=ax, label='Music', color='#32CD32')
gradient_fill(years, total_streaming, ax=ax, label='Podcasts', color='#FFD700')

ax.plot(years, total_streaming, color='darkorchid', linewidth=3, linestyle='--', marker='o', markersize=8, label='Total Streaming Users')

for i, year in enumerate(years):
    ax.text(year, total_streaming[i] + 1, f'{total_streaming[i]}M', fontsize=9, ha='center', color='black', weight='bold')

ax.set_title('The Evolution of Streaming Service Usage\nin FutureCity from 2020 to 2030', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Monthly Active Users (Millions)', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=12, rotation=45)
ax.grid(visible=True, linestyle='--', alpha=0.6)

ax2 = ax.twinx()
percentage_change = np.gradient(total_streaming, edge_order=2) / total_streaming * 100
ax2.plot(years, percentage_change, 'o-', color='grey', markersize=6, linestyle='-', label='Percentage Change', alpha=0.7)
ax2.set_ylabel('Percentage Change (%)', fontsize=14, color='grey')
ax2.tick_params(axis='y', labelcolor='grey')

handles, labels = ax.get_legend_handles_labels()
handles.append(mpatches.Patch(color='grey', label='Percentage Change'))
ax.legend(handles=handles, loc='upper left', fontsize=12, frameon=False)

plt.tight_layout()

plt.show()