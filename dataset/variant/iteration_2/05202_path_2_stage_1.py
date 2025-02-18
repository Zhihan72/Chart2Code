import matplotlib.pyplot as plt
import numpy as np

# Data for tree plantation activities (in thousands) for each organization over five years
years = ['2018', '2019', '2020', '2021', '2022']
org_A = np.array([20, 30, 50, 70, 90])
org_B = np.array([15, 25, 40, 55, 75])
org_C = np.array([10, 20, 30, 50, 65])
org_D = np.array([5, 10, 20, 35, 50])  # New data for Org D

# Data for impact in terms of carbon offset (in tonnes per year)
carbon_offset = np.array([200, 300, 450, 600, 750])

# Plotting the main bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

width = 0.15  # Adjust the width to accommodate the new bars
x = np.arange(len(years))

bar1 = ax1.bar(x - 1.5*width, org_A, width, label='Org A', color='#79C753', edgecolor='black')
bar2 = ax1.bar(x - 0.5*width, org_B, width, label='Org B', color='#4CAF50', edgecolor='black')
bar3 = ax1.bar(x + 0.5*width, org_C, width, label='Org C', color='#2E7D32', edgecolor='black')
bar4 = ax1.bar(x + 1.5*width, org_D, width, label='Org D', color='#1B5E20', edgecolor='black')  # Plot for Org D

ax1.set_title('Forest Conservation Efforts by Organizations\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Trees Planted (Thousands)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Adding text labels on the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)  # Add labels for Org D

# Adding a secondary y-axis for carbon offset impact
ax2 = ax1.twinx()
ax2.plot(years, carbon_offset, color='dodgerblue', marker='o', linestyle='--', linewidth=2, label='Carbon Offset')
ax2.set_ylabel('Carbon Offset (Tonnes)', fontsize=12, color='dodgerblue')
ax2.spines['right'].set_color('dodgerblue')

# Adding a legend for the secondary y-axis
ax2.legend(loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()