import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart visualizes the sales performance across different product categories of a fictional company's Q1 report. 
# Additionally, it includes a comparison of those categories' customer satisfaction rates.

# Product categories and their respective sales data (in thousands) and customer satisfaction rates (in percentages)
categories = ['Electronics', 'Furniture', 'Clothing', 'Books', 'Toys', 'Groceries']
sales = [150, 90, 130, 80, 120, 170]  # Sales in thousands
satisfaction_rates = [85, 75, 70, 60, 80, 90]  # Satisfaction rates in percentage

# Defining colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Set up figure and axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Bar positions
x_pos = np.arange(len(categories))

# Plotting the sales chart
bars1 = ax1.bar(x_pos, sales, color=colors, alpha=0.7, label='Sales (in thousands)')
ax1.set_xlabel('Product Categories')
ax1.set_ylabel('Sales (in thousands)', color='black')
ax1.set_title('Q1 Sales Performance & Customer Satisfaction Comparison', fontsize=14, fontweight='bold')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(categories, rotation=45, ha='right')

# Adding an additional y-axis for customer satisfaction rates
ax2 = ax1.twinx()
line2, = ax2.plot(x_pos, satisfaction_rates, 'o-', color='green', label='Customer Satisfaction', markersize=10)
ax2.set_ylabel('Customer Satisfaction Rate (%)', color='green')

# Annotate bars with sales values
for i, v in enumerate(sales):
    ax1.text(i, v + 3, f"{v}", ha='center', fontweight='bold')

# Annotate points with satisfaction rates
for i, v in enumerate(satisfaction_rates):
    ax2.text(i, v + 1, f"{v}%", ha='center', fontweight='bold', color='green')

# Legends for both y-axes
lns = [bars1[0], line2]  # Extract the first bar for the legend
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper left')

# Adjust layout to avoid text overlap
fig.tight_layout()

# Display the plot
plt.show()