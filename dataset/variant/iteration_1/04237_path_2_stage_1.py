import matplotlib.pyplot as plt
import numpy as np

# Data Initialization
countries = ['Switzerland', 'Germany', 'Belgium', 'UK', 'USA', 'France']
choco_consumption_2015 = [9.0, 8.4, 8.3, 8.2, 5.5, 6.5]  # kg per capita
choco_consumption_2020 = [6.2, 8.5, 7.0, 9.2, 8.9, 10.1]  # kg per capita (shuffled values)

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Bar Width and Positions
bar_width = 0.4
bar_locs_2015 = np.arange(len(countries))
bar_locs_2020 = bar_locs_2015 + bar_width

# Plotting 2015 consumption
bars_2015 = ax[0].bar(bar_locs_2015, choco_consumption_2015, bar_width, color='chocolate', edgecolor='brown', label='2015')
ax[0].set_ylabel('Consumption (kg per capita)', fontsize=12)
ax[0].set_title('Annual Chocolate Consumption by Country (2015)', fontsize=14, fontweight='bold')
ax[0].legend(loc='upper right', fontsize=10)
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on bars
for bar in bars_2015:
    ax[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f} kg', 
               ha='center', va='bottom', fontsize=10, color='brown')

# Plotting 2020 consumption
bars_2020 = ax[1].bar(bar_locs_2020, choco_consumption_2020, bar_width, color='saddlebrown', edgecolor='sienna', label='2020')
ax[1].set_ylabel('Consumption (kg per capita)', fontsize=12)
ax[1].set_title('Annual Chocolate Consumption by Country (2020)', fontsize=14, fontweight='bold')
ax[1].legend(loc='upper right', fontsize=10)
ax[1].grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on bars
for bar in bars_2020:
    ax[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f} kg', 
               ha='center', va='bottom', fontsize=10, color='sienna')

# Set shared x-axis labels
ax[1].set_xticks(bar_locs_2015 + bar_width / 2)
ax[1].set_xticklabels(countries, rotation=30, ha='right', fontsize=12)

# Adding a common xlabel
fig.text(0.5, 0.04, 'Country', ha='center', fontsize=12)

# Adjust layout to avoid overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show plot
plt.show()