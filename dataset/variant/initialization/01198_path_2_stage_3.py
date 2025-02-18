import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2024)

podcast_data = {
    'True Crime': np.array([1, 3, 6, 9, 14, 16, 18, 20, 21]),
    'Health & Fitness': np.array([1, 2, 3, 5, 7, 9, 12, 15, 18]),
    'Comedy': np.array([3, 4, 6, 8, 10, 13, 15, 17, 20]),
}

values = np.array(list(podcast_data.values()))
cumulative_listeners = values.sum(axis=0)

fig, ax = plt.subplots(figsize=(12, 7))

# Change color order, add different color shades
ax.stackplot(years, values, labels=podcast_data.keys(), colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.75)

# Change line style, color and marker styles
ax.plot(years, cumulative_listeners, color='navy', linewidth=3, linestyle='-', marker='s', markersize=7, label='Total Listeners')

ax.set_title('Podcast Popularity Surge (2015-2023):\nRise of Genre-Specific and Overall Listening Trends', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Listeners (millions)', fontsize=12)

ax.annotate(f'Total: {cumulative_listeners[-1]}M', xy=(2023, cumulative_listeners[-1]), xytext=(2020, cumulative_listeners[-1] + 5),
            arrowprops=dict(facecolor='darkred', arrowstyle='|-|', lw=1.5),
            fontsize=11, fontweight='bold', color='black')

# Change legend location and enable frame
ax.legend(loc='upper right', frameon=True, framealpha=0.9)

# Adjust grid style
ax.grid(linestyle='-.', alpha=0.6, color='gray')

plt.tight_layout()
plt.show()