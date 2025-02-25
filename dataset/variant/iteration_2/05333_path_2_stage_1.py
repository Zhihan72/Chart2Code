import matplotlib.pyplot as plt
import numpy as np

# Define marketing campaigns and their impacts
campaigns = ['Social Media', 'TV Ads', 'Email Marketing', 'Billboards', 'Trade Shows']
Q1_sales = np.array([15000, 20000, 12000, 18000, 25000])
Q2_sales = np.array([16000, 21000, 13000, 19000, 26000])
Q3_sales = np.array([17000, 22000, 14000, 20000, 27000])
Q4_sales = np.array([18000, 23000, 15000, 21000, 28000])

# Calculate total sales
total_sales = Q1_sales + Q2_sales + Q3_sales + Q4_sales

# Colors for each campaign
colors_campaigns = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width and positions
bar_width = 0.2
positions = np.arange(len(campaigns))

# Plot the bar chart for each quarter
ax.barh(positions - 1.5*bar_width, Q1_sales, height=bar_width, color=colors_campaigns, edgecolor='grey', label='Q1', alpha=0.7)
ax.barh(positions - 0.5*bar_width, Q2_sales, height=bar_width, color=colors_campaigns, edgecolor='grey', label='Q2', alpha=0.6)
ax.barh(positions + 0.5*bar_width, Q3_sales, height=bar_width, color=colors_campaigns, edgecolor='grey', label='Q3', alpha=0.5)
ax.barh(positions + 1.5*bar_width, Q4_sales, height=bar_width, color=colors_campaigns, edgecolor='grey', label='Q4', alpha=0.4)

# Overlay line plot for total sales
ax.plot(total_sales, positions, color='violet', marker='s', linestyle='--', linewidth=1.5, markersize=7, label='Total Sales')

# Annotate each point on the line plot
for i, total_val in enumerate(total_sales):
    ax.text(total_val + 1000, i, f'${int(total_val)}', ha='left', va='center', fontsize=10, color='violet')

# Titles and labels
ax.set_title("Impact of Marketing Campaigns on Sales\nAcross Quarters", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sales in USD", fontsize=12)
ax.set_ylabel("Marketing Campaigns", fontsize=12)

# Set y-ticks and labels
ax.set_yticks(positions)
ax.set_yticklabels(campaigns, fontsize=12)

# Add a different grid style
ax.xaxis.grid(True, linestyle='-.', alpha=0.6)

# Update legend position and style
ax.legend(frameon=False, loc='best')

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()
