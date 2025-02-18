import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])

movies_streaming = np.array([6, 5, 7, 5, 8, 7])
tv_streaming = np.array([12, 11, 9, 12, 6, 11])
music_streaming = np.array([5, 11, 3, 4, 7, 9])
podcast_streaming = np.array([4, 7, 5, 3, 6, 2])

total_streaming = movies_streaming + tv_streaming + music_streaming + podcast_streaming

fig, ax = plt.subplots(figsize=(14, 9))

def gradient_fill(x, y, ax=None, color='blue', alpha=0.7):
    if ax is None:
        ax = plt.gca()
    ax.plot(x, y, color=color, alpha=alpha, linewidth=2.5)
    ax.fill_between(x, 0, y, color=color, alpha=alpha*0.4)

gradient_fill(years, movies_streaming, ax=ax, color='#FF6347')
gradient_fill(years, movies_streaming + tv_streaming, ax=ax, color='#4682B4')
gradient_fill(years, movies_streaming + tv_streaming + music_streaming, ax=ax, color='#32CD32')
gradient_fill(years, total_streaming, ax=ax, color='#FFD700')

ax.plot(years, total_streaming, color='darkorchid', linewidth=3, linestyle='--', marker='o', markersize=8)

for i, year in enumerate(years):
    ax.text(year, total_streaming[i] + 1, f'{total_streaming[i]}M', fontsize=9, ha='center', color='black', weight='bold')

ax.set_title('Streaming Usage in FutureCity', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Users (M)', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=12, rotation=45)

ax2 = ax.twinx()
percentage_change = np.gradient(total_streaming, edge_order=2) / total_streaming * 100
ax2.plot(years, percentage_change, 'o-', color='grey', markersize=6, linestyle='-')
ax2.set_ylabel('Change (%)', fontsize=14, color='grey')
ax2.tick_params(axis='y', labelcolor='grey')

# Removed legend and grid
plt.tight_layout()
plt.show()