import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
sector_names = ['AI & Machine Learning', 'Cybersecurity', 'Blockchain', 'Cloud Computing']

# Alter revenue data by swapping some values while keeping the structure intact
ai_revenue = [6, 9, 15, 18, 9, 40]
cybersecurity_revenue = [15, 18, 20, 23, 25, 12]
blockchain_revenue = [1, 2, 3, 30, 30, 12]
cloud_revenue = [5, 8, 15, 22, 12, 50]

# Set up the bar widths and the x locations for the groups
bar_width = 0.2
x_pos = np.arange(len(years))

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the bars for each sector
bars1 = ax.bar(x_pos - 1.5*bar_width, ai_revenue, bar_width, label=sector_names[0], color='#FF9999')
bars2 = ax.bar(x_pos - 0.5*bar_width, cybersecurity_revenue, bar_width, label=sector_names[1], color='#66B2FF')
bars3 = ax.bar(x_pos + 0.5*bar_width, blockchain_revenue, bar_width, label=sector_names[2], color='#99FF99')
bars4 = ax.bar(x_pos + 1.5*bar_width, cloud_revenue, bar_width, label=sector_names[3], color='#FFCC99')

# Adding text annotations for sector contribution highlights
for bar, y in zip(bars1, ai_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)
for bar, y in zip(bars2, cybersecurity_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)
for bar, y in zip(bars3, blockchain_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)
for bar, y in zip(bars4, cloud_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)

# Customization of the plot
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Revenue (billion USD)', fontsize=12, fontweight='bold')
ax.set_title('Growth of Key Technology Sectors: 2015-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.legend(loc='upper left', fontsize=10)

# Adding a grid for better readability and an annotation for key insights
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.text(4.5, 55, 'Cloud Computing shows the highest growth', fontsize=10, bbox=dict(facecolor='yellow', alpha=0.5))

# Optimizing layout
plt.tight_layout()

# Display the plot
plt.show()