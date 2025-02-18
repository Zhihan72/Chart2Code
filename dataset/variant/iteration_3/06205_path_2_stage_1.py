import matplotlib.pyplot as plt
import numpy as np

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
colors = ['#ffcc99', '#99ccff', '#ccff99']

# Create the figure and axes for the plot
fig, axs = plt.subplots(nrows=2, figsize=(12, 10), constrained_layout=True)

# Subplot 1: Annual Solar Power Generation by Region
x = np.arange(len(years))
bar_width = 0.25

# North
axs[0].bar(x - bar_width, north_generation, width=bar_width, color=colors[0], label='North', linestyle='dotted', edgecolor='black')
# South
axs[0].bar(x, south_generation, width=bar_width, color=colors[1], label='South', linestyle='dashdot', edgecolor='black')
# West
axs[0].bar(x + bar_width, west_generation, width=bar_width, color=colors[2], label='West', linestyle='dashed', edgecolor='black')

# Set labels and title
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Solar Power Generation (GWh)', fontsize=12)
axs[0].set_title('Annual Solar Power Generation by Region', fontsize=16, fontweight='bold')
axs[0].set_xticks(x)
axs[0].set_xticklabels(years)
axs[0].legend(loc='upper left')  # Changed legend position
axs[0].xaxis.grid(True, linestyle=':', alpha=0.5)  # Changed grid from y to x axis

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

axs[1].legend(title='Regions', loc='lower right')  # Changed legend position

# Display the plot
plt.show()