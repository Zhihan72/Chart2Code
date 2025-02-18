import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart presents the trends in coffee consumption in various age groups in a fictitious town over a decade.
# The study shows how different generations have adopted or changed their coffee-drinking habits from 2010 to 2020.

# Data for the chart
years = np.arange(2010, 2021)
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
consumption = np.array([
    [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300], # 18-25
    [90, 100, 110, 120, 130, 150, 170, 190, 210, 230, 250],  # 26-35
    [70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170],    # 36-45
    [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],      # 46-60
    [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]             # 60+
])

# Defining the color palette for each age group
colors = ['#FF6347', '#FFD700', '#90EE90', '#1E90FF', '#9370DB']

# Create subplots
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Loop through each age group and create stacked bar chart
bottom_vals = np.zeros_like(consumption[0])
for i, age_group in enumerate(age_groups):
    ax.bar(years, consumption[i], bottom=bottom_vals, color=colors[i], label=f'{age_group} years')
    bottom_vals += consumption[i]

# Adding the cumulative consumption over the years as a line chart
cumulative_consumption = consumption.sum(axis=0)
ax.plot(years, cumulative_consumption, color='black', marker='o', linestyle='-', linewidth=2, markersize=6, label='Total Consumption')

# Titles and labels
ax.set_title('Decadal Trends in Coffee Consumption\nin the Town of Coffeeburg (2010-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Cups of Coffee Consumed (in thousands)', fontsize=14)

# Adding legend
ax.legend(title='Age Groups', loc='upper left', fontsize=12)

# Enhance aesthetics
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()