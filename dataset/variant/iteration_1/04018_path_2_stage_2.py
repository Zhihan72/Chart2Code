import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
avg_books_read = [4, 3, 2, 2.5, 3.5, 4.5]
enjoy_reading_percentages = [75, 65, 55, 60, 70, 80]

# Positions for bars
positions = np.arange(len(age_groups))

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for average books read
bar_colors = ['#FF7F50', '#6A5ACD', '#2E8B57', '#FFD700', '#DC143C', '#8A2BE2']
bars = ax1.bar(positions, avg_books_read, color=bar_colors, alpha=0.8, edgecolor='black', linewidth=1.2)

# X-axis labels
ax1.set_xticks(positions)
ax1.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')

# Y-axis label and grid for the primary axis
ax1.set_ylabel('Average Books Read per Month', fontsize=14, color='darkgreen', fontweight='bold')
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Secondary y-axis for enjoyment percentages
ax2 = ax1.twinx()
ax2.set_ylabel('Percentage Enjoy Reading (%)', fontsize=14, color='maroon', fontweight='bold')
ax2.plot(positions, enjoy_reading_percentages, color='maroon', linestyle='--', marker='o', markersize=8, markerfacecolor='orange', label="Enjoy Reading (%)")
ax2.set_ylim(0, 100)
ax2.tick_params(axis='y', colors='maroon')
ax2.spines['right'].set_color('maroon')

# Annotate the bars with average books read
for bar, value in zip(bars, avg_books_read):
    ax1.text(bar.get_x() + bar.get_width()/2, value + 0.1, f'{value:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Add legend for the secondary axis
ax2.legend(loc='upper left', fontsize=12)

# Add a border around the figure (not plot)
plt.gcf().patch.set_edgecolor('black')
plt.gcf().patch.set_linewidth(2)

# Adjust layout for readability
plt.tight_layout()

# Show plot
plt.show()