import matplotlib.pyplot as plt
import numpy as np

# Backstory: Comparing vegetables harvested during summer and winter in Green Valley Farms

# Veggie types
veggie_types = ['Tomatoes', 'Cucumbers', 'Carrots', 'Bell Peppers', 'Lettuce']

# Harvest quantities for summer and winter in kilograms (kg)
summer_harvest = [320, 200, 180, 150, 240]
winter_harvest = [150, 80, 120, 100, 160]

# Positions for the veggies on the x-axis
x_positions = np.arange(len(veggie_types))

# Width of the bars
bar_width = 0.35

# Create a figure with two subplots: one for summer and one for winter
fig, ax = plt.subplots(figsize=(12, 7))

# Bar chart for summer harvest
bars_summer = ax.bar(x_positions - bar_width / 2, summer_harvest, bar_width, label='Summer', color='#FF9999', edgecolor='black')

# Bar chart for winter harvest
bars_winter = ax.bar(x_positions + bar_width / 2, winter_harvest, bar_width, label='Winter', color='#66B3FF', edgecolor='black')

# Annotate bars with the harvest quantities
for bar in bars_summer + bars_winter:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height} kg', ha='center', va='bottom', fontsize=9, weight='bold')

# Customize the plot
ax.set_xlabel('Vegetable Types', fontsize=12, weight='bold')
ax.set_ylabel('Harvest Quantity (kg)', fontsize=12, weight='bold')
ax.set_title('Comparative Vegetable Harvest at Green Valley Farms\nBetween Summer and Winter', fontsize=14, weight='bold')

# Set the x-ticks to match the veggie types and adjust rotation
ax.set_xticks(x_positions)
ax.set_xticklabels(veggie_types, rotation=15, ha='right', fontsize=11)

# Adding grid lines for better estimation of values
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adding legend
ax.legend(loc='upper right', fontsize=11)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()