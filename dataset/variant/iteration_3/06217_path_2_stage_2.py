import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
movie_streaming = np.array([10, 15, 22, 35, 50, 65, 85, 110, 130, 155, 180])
tv_streaming = np.array([5, 10, 16, 22, 30, 38, 50, 62, 75, 90, 105])
music_streaming = np.array([8, 12, 18, 25, 33, 45, 58, 70, 85, 100, 120])

# Create a stacked cumulative data array
movie_cum = np.array(movie_streaming)
tv_cum = movie_cum + np.array(tv_streaming)
music_cum = tv_cum + np.array(music_streaming)

# Plotting the area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, music_cum, color='#c2c2f0', alpha=0.7, label='Music Streaming')  # Changed color
ax.fill_between(years, tv_cum, music_cum, color='#ff9999', alpha=0.7, label='TV Streaming')  # Changed color
ax.fill_between(years, movie_cum, tv_cum, color='#ffcc99', alpha=0.7, label='Movie Streaming')  # Changed color

# Title and labels
ax.set_title('Growth of Online Streaming Subscribers (2010-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Subscribers (in millions)', fontsize=14, fontweight='bold')

# Legend
ax.legend(loc='upper left', fontsize=12, title='Streaming Services', title_fontsize='13')

# Grid and layout
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(0, 401, 50))
plt.tight_layout()

# Display the chart
plt.show()