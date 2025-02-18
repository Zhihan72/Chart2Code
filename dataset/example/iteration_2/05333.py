import matplotlib.pyplot as plt
import numpy as np

# Title and backstory of the chart
# Imagine that we are analyzing the effects of different marketing campaigns on sales of various products
# across multiple quarters in a year. This chart will show the sales impact of each marketing campaign and 
# also illustrate the overall sales growth over the four quarters.

# Marketing campaigns and their sales impacts in USD
campaigns = ['Social Media', 'TV Ads', 'Email Marketing', 'Billboards', 'Trade Shows']
Q1_sales = np.array([15000, 20000, 12000, 18000, 25000])
Q2_sales = np.array([16000, 21000, 13000, 19000, 26000])
Q3_sales = np.array([17000, 22000, 14000, 20000, 27000])
Q4_sales = np.array([18000, 23000, 15000, 21000, 28000])

# Sum sales over all quarters for each campaign
total_sales = Q1_sales + Q2_sales + Q3_sales + Q4_sales

# Colors for each campaign
colors_campaigns = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the figure and axis for the bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width and positions
bar_width = 0.2
positions = np.arange(len(campaigns))

# Plot the bar chart for each quarter
bars_Q1 = ax.bar(positions - 1.5*bar_width, Q1_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q1')
bars_Q2 = ax.bar(positions - 0.5*bar_width, Q2_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q2', alpha=0.9)
bars_Q3 = ax.bar(positions + 0.5*bar_width, Q3_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q3', alpha=0.8)
bars_Q4 = ax.bar(positions + 1.5*bar_width, Q4_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q4', alpha=0.7)

# Overlay line plot for total sales across all quarters
total_positions = np.arange(len(campaigns))
ax.plot(total_positions, total_sales, color='purple', marker='o', linestyle='-', linewidth=2, markersize=8, label='Total Sales')

# Annotate each point on the line plot
for i, total_val in enumerate(total_sales):
    ax.text(i, total_val + 500, f'${int(total_val)}', ha='center', va='bottom', fontsize=10, color='purple')

# Titles and labels
ax.set_title("Impact of Different Marketing Campaigns on Product Sales\nAcross Four Quarters", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Marketing Campaigns", fontsize=12)
ax.set_ylabel("Sales in USD", fontsize=12)

# Set x-ticks to the campaigns and labels
ax.set_xticks(positions)
ax.set_xticklabels(campaigns, fontsize=12)

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add the legend
ax.legend(loc='upper left')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()