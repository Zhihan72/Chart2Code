import numpy as np
import matplotlib.pyplot as plt

# Backstory: Monthly Sales Data Comparison
# We are analyzing the monthly sales data for three different stores over a year to compare their performances.

# Define the months and sales data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

store_a_sales = [250, 300, 400, 350, 500, 450, 600, 700, 650, 750, 800, 850]
store_b_sales = [200, 250, 300, 320, 410, 390, 480, 520, 610, 680, 730, 760]
store_c_sales = [180, 230, 260, 290, 310, 280, 350, 400, 450, 470, 500, 540]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.25

# Set the positions of the bars on the x-axis
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create bar plots for each store
bars1 = ax.bar(r1, store_a_sales, color='#5DA5DA', width=bar_width, edgecolor='grey', label='Store A')
bars2 = ax.bar(r2, store_b_sales, color='#FAA43A', width=bar_width, edgecolor='grey', label='Store B')
bars3 = ax.bar(r3, store_c_sales, color='#60BD68', width=bar_width, edgecolor='grey', label='Store C')

# Adding the values on top of bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Adding general plot customizations
ax.set_title('Monthly Sales Data Comparison of Three Stores\n (Year: 2023)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Sales (in units)', fontsize=14)
ax.set_xticks([r + bar_width for r in range(len(months))])
ax.set_xticklabels(months)
ax.grid(True, axis='y', linestyle='--', alpha=0.5)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=12, frameon=False)

# Automatically adjust subplot params to give specified padding and prevent overlap
plt.tight_layout()

# Display the plot
plt.show()