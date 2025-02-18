import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The following area chart represents the growth of different categories of online streaming subscribers (in millions) from 2010 to 2020. 
# This chart helps to analyze the trends and shifts in the preferences of the audience towards different types of online streaming subscriptions over the decade.

# Data: Streaming service subscription counts (in millions) from 2010 to 2020
years = np.arange(2010, 2021)
movie_streaming = np.array([10, 15, 22, 35, 50, 65, 85, 110, 130, 155, 180])
tv_streaming = np.array([5, 10, 16, 22, 30, 38, 50, 62, 75, 90, 105])
music_streaming = np.array([8, 12, 18, 25, 33, 45, 58, 70, 85, 100, 120])
podcast_streaming = np.array([2, 3, 4, 6, 8, 12, 18, 25, 33, 42, 55])
game_streaming = np.array([1, 2, 3, 5, 8, 11, 15, 20, 27, 35, 45])

# Create a stacked cumulative data array
movie_cum = np.array(movie_streaming)
tv_cum = movie_cum + np.array(tv_streaming)
music_cum = tv_cum + np.array(music_streaming)
podcast_cum = music_cum + np.array(podcast_streaming)
game_cum = podcast_cum + np.array(game_streaming)

# Plotting the area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, game_cum, color='#ff9999', alpha=0.7, label='Game Streaming')
ax.fill_between(years, podcast_cum, game_cum, color='#66b3ff', alpha=0.7, label='Podcast Streaming')
ax.fill_between(years, music_cum, podcast_cum, color='#99ff99', alpha=0.7, label='Music Streaming')
ax.fill_between(years, tv_cum, music_cum, color='#ffcc99', alpha=0.7, label='TV Streaming')
ax.fill_between(years, movie_cum, tv_cum, color='#c2c2f0', alpha=0.7, label='Movie Streaming')

# Setting title and labels
ax.set_title('Growth of Online Streaming Subscribers (2010-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Subscribers (in millions)', fontsize=14, fontweight='bold')

# Customizing legend
ax.legend(loc='upper left', fontsize=12, title='Streaming Services', title_fontsize='13')

# Enhancing readability with grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Setting ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(0, 601, 50))

# Adjusting layout to avoid overlapping
plt.tight_layout()

# Display the chart
plt.show()