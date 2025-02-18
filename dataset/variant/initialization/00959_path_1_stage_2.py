import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2024)
epic_fantasy = np.array([70, 72, 74, 78, 75, 80, 85, 83, 88, 90, 87])
dark_fantasy = np.array([30, 35, 37, 40, 45, 50, 55, 53, 57, 60, 58])
historical_fantasy = np.array([25, 30, 28, 32, 36, 38, 42, 45, 48, 50, 52])
romantic_fantasy = np.array([10, 12, 15, 20, 22, 25, 30, 35, 33, 30, 28])

# Calculate average popularity
average_popularity = (epic_fantasy + dark_fantasy + historical_fantasy + romantic_fantasy) / 4

# Plot creation
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area chart
ax.stackplot(years, epic_fantasy, dark_fantasy, historical_fantasy, romantic_fantasy,
             labels=['Epic Fantasy', 'Dark Fantasy', 'Historical Fantasy', 'Romantic Fantasy'],
             colors=['#ff7f0e', '#d62728', '#9467bd', '#1f77b4'],  # adjusted color choices
             alpha=0.85)

# Average popularity line
ax.plot(years, average_popularity, color='green', linewidth=1.5, linestyle='-.', marker='s', label='Average Popularity')

# Updated chart elements
ax.set_title('Popularity Trends in Fantasy Novel Genres\nOver the Decade (2013-2023)', fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

# Legend properties
ax.legend(loc='lower center', title='Genres', frameon=False, fontsize=9)

# Grid styling
ax.grid(True, axis='both', linestyle=':', alpha=0.5)

# Enhancing layout
plt.tight_layout()

# Display the plot
plt.show()