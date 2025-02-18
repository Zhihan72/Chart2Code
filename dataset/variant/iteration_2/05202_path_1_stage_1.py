import matplotlib.pyplot as plt
import numpy as np

# Data for tree plantation activities (in thousands) for each organization over five years
years = ['2018', '2019', '2020', '2021', '2022']
org_A = np.array([20, 30, 50, 70, 90])
org_B = np.array([15, 25, 40, 55, 75])
org_C = np.array([10, 20, 30, 50, 65])

# Data for impact in terms of carbon offset (in tonnes per year)
carbon_offset = np.array([200, 300, 450, 600, 750])

# Plotting the horizontal bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

height = 0.2
y = np.arange(len(years))

bar1 = ax1.barh(y - height, org_A, height, label='Org A', color='#79C753', edgecolor='black')
bar2 = ax1.barh(y, org_B, height, label='Org B', color='#4CAF50', edgecolor='black')
bar3 = ax1.barh(y + height, org_C, height, label='Org C', color='#2E7D32', edgecolor='black')

ax1.set_title('Forest Conservation Efforts by Organizations\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Trees Planted (Thousands)', fontsize=12)
ax1.set_ylabel('Year', fontsize=12)
ax1.set_yticks(y)
ax1.set_yticklabels(years, fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Adding text labels on the bars
def add_labels(bars):
    for bar in bars:
        width = bar.get_width()
        ax1.annotate(f'{width}',
                     xy=(width, bar.get_y() + bar.get_height() / 2),
                     xytext=(3, 0),  # 3 points horizontal offset
                     textcoords="offset points",
                     ha='left', va='center')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)

# Adding a secondary x-axis for carbon offset impact
ax2 = ax1.twiny()
ax2.plot(carbon_offset, y, color='dodgerblue', marker='o', linestyle='--', linewidth=2, label='Carbon Offset')
ax2.set_xlabel('Carbon Offset (Tonnes)', fontsize=12, color='dodgerblue')
ax2.spines['top'].set_color('dodgerblue')

# Adding a legend for the secondary x-axis
ax2.legend(loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()