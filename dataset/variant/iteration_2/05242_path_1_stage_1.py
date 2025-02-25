import matplotlib.pyplot as plt
import numpy as np

# Define the countries and data
countries = ['DE', 'FR', 'IT', 'ES', 'SE']
years = np.array([2019, 2020, 2021, 2022, 2023])
germany_farms = np.array([2300, 2450, 2600, 2750, 2900])
france_farms = np.array([2100, 2200, 2300, 2400, 2500])
italy_farms = np.array([1800, 1950, 2050, 2200, 2350])
spain_farms = np.array([1650, 1750, 1850, 2000, 2150])
sweden_farms = np.array([900, 950, 1000, 1050, 1100])

# Bar width and positions
bar_width = 0.15
positions = np.arange(len(years))

# Create figure and subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each country's data
ax.bar(positions, germany_farms, width=bar_width, color='cornflowerblue', edgecolor='grey', label='DE')
ax.bar(positions + bar_width, france_farms, width=bar_width, color='seagreen', edgecolor='grey', label='FR')
ax.bar(positions + 2 * bar_width, italy_farms, width=bar_width, color='tomato', edgecolor='grey', label='IT')
ax.bar(positions + 3 * bar_width, spain_farms, width=bar_width, color='gold', edgecolor='grey', label='ES')
ax.bar(positions + 4 * bar_width, sweden_farms, width=bar_width, color='mediumpurple', edgecolor='grey', label='SE')

# Data labels on top of each bar
for i in range(len(years)):
    ax.text(i, germany_farms[i] + 50, f'{germany_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + bar_width, france_farms[i] + 50, f'{france_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + 2 * bar_width, italy_farms[i] + 50, f'{italy_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + 3 * bar_width, spain_farms[i] + 50, f'{spain_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + 4 * bar_width, sweden_farms[i] + 50, f'{sweden_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)

# Setting labels and title
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('No. of Farms', fontsize=12, fontweight='bold')
ax.set_title('Organic Farm Growth (2019-23)', fontsize=16, fontweight='bold', pad=20)

# Set x-ticks to display the years
ax.set_xticks(positions + 2 * bar_width)
ax.set_xticklabels(years)

# Add a legend to differentiate between countries
ax.legend(loc='upper left', fontsize=12, title='Country')

# Add grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()