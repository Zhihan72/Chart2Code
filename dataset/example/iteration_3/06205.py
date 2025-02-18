import matplotlib.pyplot as plt
import numpy as np

# Backstory: Understanding Solar Power Generation in Different Regions
# This chart represents the annual solar power generation in Gigawatt-hours (GWh) for three different regions over four years. Additionally, it shows the cumulative contribution of each region's power generation to the total solar capacity.

# Define regions and years
regions = ['North', 'South', 'West']
years = ['2019', '2020', '2021', '2022']

# Annual solar power generation data (GWh) for each region
north_generation = np.array([20, 25, 30, 35])
south_generation = np.array([25, 30, 35, 40])
west_generation = np.array([15, 20, 25, 30])

# Create cumulative data for stacked bar chart
total_generation = north_generation + south_generation + west_generation
north_cumulative = np.cumsum(north_generation)
south_cumulative = np.cumsum(south_generation)
west_cumulative = np.cumsum(west_generation)

# Colors
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Create the figure and axes for the plot
fig, axs = plt.subplots(nrows=2, figsize=(12, 10), constrained_layout=True)

# Subplot 1: Annual Solar Power Generation by Region
x = np.arange(len(years))
bar_width = 0.25

# North
axs[0].bar(x - bar_width, north_generation, width=bar_width, color=colors[0], label='North')
# South
axs[0].bar(x, south_generation, width=bar_width, color=colors[1], label='South')
# West
axs[0].bar(x + bar_width, west_generation, width=bar_width, color=colors[2], label='West')

# Set labels and title
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Solar Power Generation (GWh)', fontsize=12)
axs[0].set_title('Annual Solar Power Generation by Region', fontsize=16, fontweight='bold')
axs[0].set_xticks(x)
axs[0].set_xticklabels(years)
axs[0].legend(title='Regions')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Cumulative Solar Power Generation by Region
axs[1].bar(years, north_cumulative, color=colors[0], label='North', bottom=south_cumulative + west_cumulative)
axs[1].bar(years, south_cumulative, color=colors[1], label='South', bottom=west_cumulative)
axs[1].bar(years, west_cumulative, color=colors[2], label='West')

# Set labels and title
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Solar Power Generation (GWh)', fontsize=12)
axs[1].set_title('Cumulative Solar Power Generation by Region', fontsize=16, fontweight='bold')

# Annotate each bar with the cumulative value
for i, (n, s, w) in enumerate(zip(north_cumulative, south_cumulative, west_cumulative)):
    axs[1].text(i, n + s + w, f'{n+s+w} GWh', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add legend to the second plot
axs[1].legend(title='Regions', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()