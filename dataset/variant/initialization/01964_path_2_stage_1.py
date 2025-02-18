import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])
movies_streaming = np.array([5, 7, 8, 7, 6, 5])
tv_series_streaming = np.array([6, 9, 11, 12, 12, 11])
music_streaming = np.array([3, 4, 5, 7, 9, 11])
podcast_streaming = np.array([2, 3, 4, 5, 6, 7])
total_streaming = movies_streaming + tv_series_streaming + music_streaming + podcast_streaming

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(years, 0, movies_streaming, label='Movies', color='#FF6347', alpha=0.9)
ax.fill_between(years, movies_streaming, movies_streaming + tv_series_streaming, label='TV Series', color='#4682B4', alpha=0.6)
ax.fill_between(years, movies_streaming + tv_series_streaming, movies_streaming + tv_series_streaming + music_streaming, label='Music', color='#32CD32', alpha=0.5)
ax.fill_between(years, movies_streaming + tv_series_streaming + music_streaming, total_streaming, label='Podcasts', color='#FFD700', alpha=0.4)

ax.plot(years, total_streaming, color='indigo', linewidth=3.0, linestyle='-', marker='s', label='Total Streaming Users')

for i, year in enumerate(years):
    ax.text(year, total_streaming[i] + 0.5, f'{total_streaming[i]}M', fontsize=10, ha='center', va='bottom', color='navy', weight='bold')

ax.set_title('The Evolution of Streaming Service Usage in FutureCity from 2020 to 2030', fontsize=15, weight='bold', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Monthly Active Users (Millions)', fontsize=13)

ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=11, rotation=30)

ax.grid(visible=True, linestyle='-', alpha=0.6)
ax.legend(loc='center right', fontsize=11, frameon=True)

ax.set_facecolor('#F0F0F5')
fig.patch.set_facecolor('#E3E3E3')

plt.tight_layout()

plt.show()