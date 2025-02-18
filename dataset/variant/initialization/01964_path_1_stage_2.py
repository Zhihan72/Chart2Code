import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])

movies_streaming = np.array([5, 7, 8, 7, 6, 5])
tv_series_streaming = np.array([6, 9, 11, 12, 12, 11])
music_streaming = np.array([3, 4, 5, 7, 9, 11])
podcast_streaming = np.array([2, 3, 4, 5, 6, 7])

total_streaming = movies_streaming + tv_series_streaming + music_streaming + podcast_streaming

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(years, 0, movies_streaming, color='#1E90FF', alpha=0.7)  # Changed color
ax.fill_between(years, movies_streaming, movies_streaming + tv_series_streaming, color='#FF8C00', alpha=0.7)  # Changed color
ax.fill_between(years, movies_streaming + tv_series_streaming, movies_streaming + tv_series_streaming + music_streaming, color='#8A2BE2', alpha=0.7)  # Changed color
ax.fill_between(years, movies_streaming + tv_series_streaming + music_streaming, total_streaming, color='#3CB371', alpha=0.7)  # Changed color

ax.plot(years, total_streaming, color='crimson', linewidth=2.5, linestyle='--', marker='o')  # Changed color

ax.set_xticks(years)

ax.grid(visible=True, linestyle='--', alpha=0.5)

ax.set_facecolor('#F7F7F9')
fig.patch.set_facecolor('#EDEDED')

plt.tight_layout()

plt.show()