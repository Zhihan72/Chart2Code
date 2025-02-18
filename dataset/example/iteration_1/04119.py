import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The world of Esports has been booming, with growing engagement in different genres.
# We’re interested in visualizing the growth of engagement in various Esports genres
# from 2015 to 2025. We’ll also show the total engagement trend.

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Esports genres engagement data (millions)
battle_royale = np.array([5, 7, 10, 15, 20, 25, 35, 45, 55, 60, 65])
MOBA = np.array([20, 23, 25, 27, 30, 32, 35, 38, 40, 45, 48])
FPS = np.array([15, 18, 20, 22, 23, 25, 28, 30, 33, 36, 40])
sports = np.array([10, 12, 13, 15, 18, 20, 23, 27, 30, 33, 35])
strategy = np.array([8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26])

# Cumulative total engagement
total_engagement = battle_royale + MOBA + FPS + sports + strategy

# Create the figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 14))

# Stacked area chart on the first subplot
axs[0].stackplot(years, battle_royale, MOBA, FPS, sports, strategy,
                 labels=['Battle Royale', 'MOBA', 'FPS', 'Sports', 'Strategy'],
                 colors=['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0'],
                 alpha=0.8)
axs[0].set_title('Global Esports Engagement (2015-2025)\nGrowth Across Different Genres', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Engagement (Millions)', fontsize=14)
axs[0].legend(loc='upper left', title='Esports Genres', fontsize=11)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Line plot for total engagement trend on the second subplot
axs[1].plot(years, total_engagement, marker='o', color='#ff7f0e', linestyle='-', linewidth=2)
axs[1].fill_between(years, 0, total_engagement, color='#ffcc66', alpha=0.5)
axs[1].set_title('Total Esports Engagement (2015-2025)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Total Engagement (Millions)', fontsize=14)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()