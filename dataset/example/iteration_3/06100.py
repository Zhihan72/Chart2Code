import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are looking at the monthly sales data for "Tech Gadgets Store" across four regions: North, South, East, and West.
# The data spans the first half of the year. 
# The chart aims to visualize and compare the sales performance of different regions.

# Months and regions
months = ['January', 'February', 'March', 'April', 'May', 'June']
regions = ['North', 'South', 'East', 'West']

# Sales data for each region (in thousands of units)
north_sales = [15, 20, 25, 22, 30, 35]
south_sales = [10, 15, 12, 20, 25, 28]
east_sales = [18, 22, 27, 30, 35, 40]
west_sales = [8, 12, 10, 15, 18, 22]

# Colors for the bars
colors = ['#007ACC', '#FF5733', '#28A745', '#FFD700']

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 7))

# Plot each region's sales data as a bar chart
bar_width = 0.2
index = np.arange(len(months))

bars_north = ax.bar(index - bar_width*1.5, north_sales, bar_width, label='North', color=colors[0])
bars_south = ax.bar(index - bar_width/2, south_sales, bar_width, label='South', color=colors[1])
bars_east = ax.bar(index + bar_width/2, east_sales, bar_width, label='East', color=colors[2])
bars_west = ax.bar(index + bar_width*1.5, west_sales, bar_width, label='West', color=colors[3])

# Add titles and labels
ax.set_title("Monthly Sales Data of Tech Gadgets Store: First Half of the Year", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Sales (Thousands of Units)", fontsize=14)

# Set the x-axis labels and ticks
ax.set_xticks(index)
ax.set_xticklabels(months)
plt.xticks(rotation=45)

# Add a legend
ax.legend(title='Regions', loc='upper left', bbox_to_anchor=(1, 1), fontsize=11)

# Annotate bars with their values
for bars in [bars_north, bars_south, bars_east, bars_west]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height), xytext=(0, 3), 
                    textcoords="offset points", ha='center', va='bottom', fontsize=10)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent clipping of labels and titles
plt.tight_layout()

# Display the plot
plt.show()