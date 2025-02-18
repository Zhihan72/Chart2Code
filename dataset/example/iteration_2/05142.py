import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Monthly Sales Performance Across Various Regions for a Fictional Beverage Company in 2022
# Data for the plot
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
q1_sales = [120, 98, 140, 75, 50]
q2_sales = [150, 110, 160, 65, 45]
q3_sales = [130, 120, 165, 85, 55]
q4_sales = [140, 130, 180, 90, 60]

# Create a figure and set of subplots with 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

# Define bar width and bar positions
bar_width = 0.2
bar_positions = np.arange(len(regions))

# Plotting Sales Data by Quarter
ax1.bar(bar_positions - 1.5 * bar_width, q1_sales, width=bar_width, color='#FF6347', edgecolor='black', label='Q1')
ax1.bar(bar_positions - 0.5 * bar_width, q2_sales, width=bar_width, color='#FFD700', edgecolor='black', label='Q2')
ax1.bar(bar_positions + 0.5 * bar_width, q3_sales, width=bar_width, color='#90EE90', edgecolor='black', label='Q3')
ax1.bar(bar_positions + 1.5 * bar_width, q4_sales, width=bar_width, color='#4682B4', edgecolor='black', label='Q4')

# Adding titles and labels
ax1.set_title('Monthly Sales Performance of Beverage Company Across Regions (2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Regions', fontsize=14)
ax1.set_ylabel('Sales Units (in thousands)', fontsize=14)

# Setting x-ticks and labels
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(regions, rotation=15, ha='right', fontsize=12)

# Adding legend
ax1.legend(loc='upper right', fontsize=12)

# Adding gridlines for y-axis
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Creating and plotting overall sales data
regional_labels = regions
overall_sales = np.array(q1_sales) + np.array(q2_sales) + np.array(q3_sales) + np.array(q4_sales)

ax2.barh(regional_labels, overall_sales, color='#6A5ACD', edgecolor='black', alpha=0.8)

# Adding titles and labels for horizontal bar chart
ax2.set_title('Overall Annual Sales Performance by Region (2022)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Sales Units (in thousands)', fontsize=14)
ax2.set_ylabel('Regions', fontsize=14)

# Adding value labels for each bar
for i in range(len(overall_sales)):
    ax2.text(overall_sales[i] + 5, i, f'{overall_sales[i]}K', va='center', ha='left', fontsize=12, color='white', fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()