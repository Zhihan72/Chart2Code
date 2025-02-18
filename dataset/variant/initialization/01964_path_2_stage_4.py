import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])
movies_streaming = np.array([5, 7, 8, 7, 6, 5])
tv_series_streaming = np.array([6, 9, 11, 12, 12, 11])
music_streaming = np.array([3, 4, 5, 7, 9, 11])
podcast_streaming = np.array([2, 3, 4, 5, 6, 7])
audiobook_streaming = np.array([1, 2, 3, 3, 4, 5])

total_streaming = movies_streaming + tv_series_streaming + music_streaming + podcast_streaming + audiobook_streaming

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(years, 0, movies_streaming, color='#FF4500', alpha=0.9)
ax.fill_between(years, movies_streaming, movies_streaming + tv_series_streaming, color='#1E90FF', alpha=0.6)
ax.fill_between(years, movies_streaming + tv_series_streaming, movies_streaming + tv_series_streaming + music_streaming, color='#3CB371', alpha=0.5)
ax.fill_between(years, movies_streaming + tv_series_streaming + music_streaming, movies_streaming + tv_series_streaming + music_streaming + podcast_streaming, color='#FFA07A', alpha=0.4)
ax.fill_between(years, movies_streaming + tv_series_streaming + music_streaming + podcast_streaming, total_streaming, color='#9400D3', alpha=0.3)

ax.plot(years, total_streaming, color='indigo', linewidth=3.0, linestyle='-', marker='s')

# Remove axis labels, text annotations, title and legend
ax.set_xticks(years)
ax.set_xticklabels([])  # Remove the labels for x-ticks

ax.grid(visible=True, linestyle='-', alpha=0.6)

ax.set_facecolor('#F0F0F5')
fig.patch.set_facecolor('#E3E3E3')

plt.tight_layout()

plt.show()