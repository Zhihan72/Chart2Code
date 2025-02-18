import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are charting the profits of fictional superhero-comic book series in the year 2025.
# These series are popular among fans, with each series producing a variety of merchandise and generating
# a significant amount of annual profit.

# Data: Names of comic book series and their profits in millions of USD
comic_series = [
    'The Valiant Avenger',
    'Cosmic Defender',
    'Mystery Sleuth',
    'Dark Knight',
    'Fast & Fearless',
    'Captain Marvelous',
    'The Spectrum Enigma'
]
annual_profits = [85, 75, 60, 95, 70, 50, 65] # in millions of USD

# Creating the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for the bars
colors = ['#1e90ff', '#32cd32', '#ff6347', '#8a2be2', '#ff8c00', '#ff1493', '#00ced1']

# Create the bar chart
bars = ax.barh(np.arange(len(comic_series)), annual_profits, color=colors, edgecolor='black', height=0.7, alpha=0.85)

# Adding text labels to each bar
for bar in bars:
    ax.annotate(f"${bar.get_width()}M", 
                 xy=(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2),
                 va='center', ha='left', color='black', fontsize=12, fontweight='bold')

# Customize the title and labels
ax.set_title('Annual Profits of Top Comic Book Series in 2025', fontsize=18, fontweight='bold', color='navy')
ax.set_xlabel('Annual Profit (in Millions USD)', fontsize=14)
ax.set_yticks(np.arange(len(comic_series)))
ax.set_yticklabels(comic_series, fontsize=12)

# Adjusting aesthetics: Adding grid lines, inverting y-axis, and removing spines for a cleaner look
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_visible(False)

# Adding a value-highlight plot showing the maximum profit
max_profit = max(annual_profits)
max_profit_series = comic_series[annual_profits.index(max_profit)]

ax.plot([max_profit], [annual_profits.index(max_profit)], 'ro')
ax.annotate(f"Top Profit\n{max_profit_series}: ${max_profit}M",
             xy=(max_profit, annual_profits.index(max_profit)),
             xytext=(max_profit+5, annual_profits.index(max_profit)-0.5),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=12, color='red', fontweight='bold', ha='left')

# Automatically adjust the image layout to be more readable
plt.tight_layout()

# Display the chart
plt.show()