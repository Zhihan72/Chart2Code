import matplotlib.pyplot as plt
import numpy as np

# Backstory and Data Creation
# Title: "Game Console Sales Comparison (2010-2020)"
# This chart compares the total global sales of various popular gaming consoles over the past decade. 
# The data shows unit sales for three top consoles: PlayStation, Xbox, and Nintendo.

years = list(range(2010, 2021))
playstation_sales = [14.2, 13.3, 16.3, 14.9, 17.8, 18.5, 19.4, 20.0, 17.7, 14.4, 12.5]
xbox_sales = [10.3, 9.4, 11.6, 12.7, 13.8, 15.3, 14.7, 16.2, 15.4, 14.1, 13.5]
nintendo_sales = [8.8, 9.0, 10.7, 11.8, 12.3, 13.7, 16.3, 15.4, 14.2, 18.5, 20.1]

# Plotting script
fig, ax = plt.subplots(figsize=(12, 7))

# Bar width
bar_width = 0.25

# Set positions of bar on X axis
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create bars
bars1 = ax.bar(r1, playstation_sales, color='blue', width=bar_width, edgecolor='grey', label='PlayStation')
bars2 = ax.bar(r2, xbox_sales, color='green', width=bar_width, edgecolor='grey', label='Xbox')
bars3 = ax.bar(r3, nintendo_sales, color='red', width=bar_width, edgecolor='grey', label='Nintendo')

# Add labels, title, and legend
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sales (millions of units)', fontsize=14)
plt.title('Game Console Sales Comparison (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xticks([r + bar_width for r in range(len(years))], years)

# Adding value labels to bars
for bar in bars1 + bars2 + bars3:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
plt.legend()

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()