import matplotlib.pyplot as plt
import numpy as np

# Data Initialization
countries = ['CH', 'DE', 'UK', 'USA', 'FR']
choco_2015 = [9.0, 8.4, 8.2, 5.5, 6.5]
choco_2020 = [10.1, 9.2, 8.5, 6.2, 7.0]

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Bar Width and Positions
bar_width = 0.4
locs_2015 = np.arange(len(countries))
locs_2020 = locs_2015 + bar_width

# Plotting 2015 consumption
bars_2015 = ax[0].bar(locs_2015, choco_2015, bar_width, color='saddlebrown', edgecolor='sienna', label='2015')
ax[0].set_ylabel('Kg per Capita', fontsize=12)
ax[0].set_title('Choco Consumption (2015)', fontsize=14, fontweight='bold')
ax[0].legend(loc='upper right', fontsize=10)
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on bars
for bar in bars_2015:
    ax[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f}', 
               ha='center', va='bottom', fontsize=10, color='sienna')

# Plotting 2020 consumption
bars_2020 = ax[1].bar(locs_2020, choco_2020, bar_width, color='chocolate', edgecolor='brown', label='2020')
ax[1].set_ylabel('Kg per Capita', fontsize=12)
ax[1].set_title('Choco Consumption (2020)', fontsize=14, fontweight='bold')
ax[1].legend(loc='upper right', fontsize=10)
ax[1].grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on bars
for bar in bars_2020:
    ax[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f}', 
               ha='center', va='bottom', fontsize=10, color='brown')

# Set shared x-axis labels
ax[1].set_xticks(locs_2015 + bar_width / 2)
ax[1].set_xticklabels(countries, rotation=30, ha='right', fontsize=12)

# Adding a common xlabel
fig.text(0.5, 0.04, 'Country', ha='center', fontsize=12)

# Adjust layout to avoid overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show plot
plt.show()