import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
movie_streaming = np.array([10, 15, 22, 35, 50, 65, 85, 110, 130, 155, 180])
tv_streaming = np.array([5, 10, 16, 22, 30, 38, 50, 62, 75, 90, 105])
music_streaming = np.array([8, 12, 18, 25, 33, 45, 58, 70, 85, 100, 120])
podcast_streaming = np.array([2, 3, 4, 6, 8, 12, 18, 25, 33, 42, 55])
game_streaming = np.array([1, 2, 3, 5, 8, 11, 15, 20, 27, 35, 45])
ebook_streaming = np.array([0, 1, 2, 3, 4, 6, 9, 12, 16, 21, 27])  # New data series for eBook Streaming

movie_cum = np.array(movie_streaming)
tv_cum = movie_cum + np.array(tv_streaming)
music_cum = tv_cum + np.array(music_streaming)
podcast_cum = music_cum + np.array(podcast_streaming)
game_cum = podcast_cum + np.array(game_streaming)
ebook_cum = game_cum + np.array(ebook_streaming)

fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, ebook_cum, color='#b3e0ff', alpha=0.6, label='eBooks', linestyle='solid')  # Add eBook data
ax.fill_between(years, game_cum, ebook_cum, color='#ff9999', alpha=0.6, label='Games', linestyle='solid')
ax.fill_between(years, podcast_cum, game_cum, color='#66b3ff', alpha=0.8, label='Podcasts', linestyle='dashed')
ax.fill_between(years, music_cum, podcast_cum, color='#99ff99', alpha=0.5, label='Music', linestyle='dashdot')
ax.fill_between(years, tv_cum, music_cum, color='#ffcc99', alpha=0.4, label='TV', linestyle='dotted')
ax.fill_between(years, movie_cum, tv_cum, color='#c2c2f0', alpha=0.7, label='Movies', linestyle='solid')

ax.set_title('Streaming Subscriptions (2010-20)', fontsize=14, fontweight='normal')
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Subs (millions)', fontsize=12)

ax.legend(loc='lower right', fontsize=10, title='Services', title_fontsize='11', frameon=True, facecolor='lightgrey', edgecolor='black')
ax.grid(axis='x', linestyle='-.', alpha=0.5)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=0)
ax.set_yticks(np.arange(0, 651, 50))  # Updated y-axis to accommodate new data

plt.tight_layout()
plt.show()