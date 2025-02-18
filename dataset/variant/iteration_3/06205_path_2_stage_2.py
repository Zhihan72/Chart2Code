import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['North', 'South']
years = ['2019', '2020', '2021', '2022']

# Annual solar power generation data (GWh) for each region
north_generation = np.array([20, 25, 30, 35])
south_generation = np.array([25, 30, 35, 40])

# Create cumulative data for stacked bar chart
north_cumulative = np.cumsum(north_generation)
south_cumulative = np.cumsum(south_generation)

# Colors
colors = ['#ffcc99', '#99ccff']

# Create the figure and axes for the plot
fig, axs = plt.subplots(nrows=2, figsize=(12, 10), constrained_layout=True)

# Subplot 1: Annual Solar Power Generation by Region
x = np.arange(len(years))
bar_width = 0.35

# North
axs[0].bar(x - bar_width/2, north_generation, width=bar_width, color=colors[0], label='North', linestyle='dotted', edgecolor='black')
# South
axs[0].bar(x + bar_width/2, south_generation, width=bar_width, color=colors[1], label='South', linestyle='dashdot', edgecolor='black')

# Set labels and title
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Solar Power Generation (GWh)', fontsize=12)
axs[0].set_title('Annual Solar Power Generation by Region', fontsize=16, fontweight='bold')
axs[0].set_xticks(x)
axs[0].set_xticklabels(years)
axs[0].legend(loc='upper left')
axs[0].xaxis.grid(True, linestyle=':', alpha=0.5)

# Subplot 2: Cumulative Solar Power Generation by Region
axs[1].bar(years, north_cumulative, color=colors[0], label='North', bottom=south_cumulative)
axs[1].bar(years, south_cumulative, color=colors[1], label='South')

# Set labels and title
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Solar Power Generation (GWh)', fontsize=12)
axs[1].set_title('Cumulative Solar Power Generation by Region', fontsize=16, fontweight='bold')

# Annotate each bar with the cumulative value
for i, (n, s) in enumerate(zip(north_cumulative, south_cumulative)):
    axs[1].text(i, n + s, f'{n+s} GWh', ha='center', va='bottom', fontsize=10, fontweight='bold')

axs[1].legend(title='Regions', loc='lower right')

# Display the plot
plt.show()