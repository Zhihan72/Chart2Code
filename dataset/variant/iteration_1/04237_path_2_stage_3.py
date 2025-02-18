import matplotlib.pyplot as plt
import numpy as np

# Data Initialization
countries = ['France', 'Germany', 'Belgium', 'USA', 'UK', 'Switzerland']
choco_consumption_2015 = [6.5, 8.4, 8.3, 5.5, 8.2, 9.0]
choco_consumption_2020 = [10.1, 8.5, 7.0, 8.9, 9.2, 6.2]

# Sort 2015 data
sorted_2015 = sorted(zip(choco_consumption_2015, countries), reverse=True)
choco_consumption_2015_sorted, countries_sorted_2015 = zip(*sorted_2015)

# Sort 2020 data
sorted_2020 = sorted(zip(choco_consumption_2020, countries), reverse=True)
choco_consumption_2020_sorted, countries_sorted_2020 = zip(*sorted_2020)

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Plotting 2015 consumption
bar_width = 0.4
bar_locs_2015 = np.arange(len(countries))
bars_2015 = ax[0].bar(bar_locs_2015, choco_consumption_2015_sorted, bar_width, color='chocolate', edgecolor='brown')
ax[0].set_ylabel('Chocolate Intake (kg per person)', fontsize=12)
ax[0].set_title('Choco Stats by Countries (2k15)', fontsize=14, fontweight='bold')
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on bars
for bar in bars_2015:
    ax[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f} kilos', 
               ha='center', va='bottom', fontsize=10, color='brown')

# Plotting 2020 consumption
bars_2020 = ax[1].bar(bar_locs_2015, choco_consumption_2020_sorted, bar_width, color='saddlebrown', edgecolor='sienna')
ax[1].set_ylabel('Chocolate Intake (kg per person)', fontsize=12)
ax[1].set_title('Choco Stats by Countries (2k20)', fontsize=14, fontweight='bold')
ax[1].grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on bars
for bar in bars_2020:
    ax[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{bar.get_height():.1f} kilos', 
               ha='center', va='bottom', fontsize=10, color='sienna')

# Set shared x-axis labels
ax[1].set_xticks(bar_locs_2015 + bar_width / 2)
ax[1].set_xticklabels(countries_sorted_2020, rotation=30, ha='right', fontsize=12)

# Adding a common xlabel
fig.text(0.5, 0.04, 'Nations', ha='center', fontsize=12)

# Adjust layout to avoid overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show plot
plt.show()