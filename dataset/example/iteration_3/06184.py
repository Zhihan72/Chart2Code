import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the consumption of different fruits over the last four seasons within a hypothetical city. The data shows how seasonal preferences affect fruit consumption trends.

# Seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Fruit consumption (in kg) for each season
apples = np.array([120, 80, 100, 90])
bananas = np.array([100, 150, 80, 60])
oranges = np.array([60, 70, 110, 130])
grapes = np.array([40, 100, 50, 30])
strawberries = np.array([70, 200, 90, 40])

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.15

#Create positions for the bars
positions_apples = np.arange(len(seasons))
positions_bananas = positions_apples + bar_width
positions_oranges = positions_apples + 2 * bar_width
positions_grapes = positions_apples + 3 * bar_width
positions_strawberries = positions_apples + 4 * bar_width

# Create bars
bars_apples = ax.bar(positions_apples, apples, bar_width, label='Apples', color='red')
bars_bananas = ax.bar(positions_bananas, bananas, bar_width, label='Bananas', color='yellow')
bars_oranges = ax.bar(positions_oranges, oranges, bar_width, label='Oranges', color='orange')
bars_grapes = ax.bar(positions_grapes, grapes, bar_width, label='Grapes', color='purple')
bars_strawberries = ax.bar(positions_strawberries, strawberries, bar_width, label='Strawberries', color='pink')

# Titles and labels
ax.set_title('Seasonal Fruit Consumption Trends in Hypothetical City', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Fruit Consumption (kg)', fontsize=12)
ax.set_xticks(positions_apples + 2 * bar_width)
ax.set_xticklabels(seasons)

# Adding a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adding legend
ax.legend(loc='upper left', fontsize=10)

# Annotate the top of each bar with its height
bars = [bars_apples, bars_bananas, bars_oranges, bars_grapes, bars_strawberries]
for bar_set in bars:
    for bar in bar_set:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=9)

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()