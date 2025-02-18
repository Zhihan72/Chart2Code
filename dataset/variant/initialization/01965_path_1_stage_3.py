import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])
# Modify each array by randomizing the original data order to keep the dimensional structure unchanged
movies_streaming = np.array([5, 7, 8, 6, 5, 7])
tv_series_streaming = np.array([11, 9, 12, 6, 7, 12])
music_streaming = np.array([7, 5, 11, 4, 3, 9])
podcast_streaming = np.array([4, 7, 3, 5, 6, 2])

# Recalculate total_streaming based on altered arrays
total_streaming = movies_streaming + tv_series_streaming + music_streaming + podcast_streaming

fig, ax = plt.subplots(figsize=(14, 9))

def gradient_fill(x, y, ax=None, color='blue', alpha=0.7):
    if ax is None:
        ax = plt.gca()
    ax.plot(x, y, color=color, alpha=alpha, linewidth=2.5)
    ax.fill_between(x, 0, y, color=color, alpha=alpha*0.4)

gradient_fill(years, movies_streaming, ax=ax, color='#B22222')
gradient_fill(years, movies_streaming + tv_series_streaming, ax=ax, color='#1E90FF')
gradient_fill(years, movies_streaming + tv_series_streaming + music_streaming, ax=ax, color='#228B22')
gradient_fill(years, total_streaming, ax=ax, color='#FFA500')

ax.plot(years, total_streaming, color='darkolivegreen', linewidth=3, linestyle='--', marker='o', markersize=8)

for i, year in enumerate(years):
    ax.text(year, total_streaming[i] + 1, f'{total_streaming[i]}M', fontsize=9, ha='center', color='black', weight='bold')

ax.set_title('Streaming Service Usage in FutureCity from 2020 to 2030', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Monthly Active Users (Millions)', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=12, rotation=45)

plt.tight_layout()

plt.show()