import matplotlib.pyplot as plt
import numpy as np

# Months and regions
months = ['January', 'February', 'March', 'April', 'May', 'June']
regions = ['North', 'South', 'East', 'West']

# Sales data for each region (in thousands of units)
north_sales = [15, 20, 25, 22, 30, 35]
south_sales = [10, 15, 12, 20, 25, 28]
east_sales = [18, 22, 27, 30, 35, 40]
west_sales = [8, 12, 10, 15, 18, 22]

# Combine data and sort for sorted bar chart
total_sales = [sum(north_sales), sum(south_sales), sum(east_sales), sum(west_sales)]
sales_data = list(zip(regions, total_sales))
sorted_sales_data = sorted(sales_data, key=lambda x: x[1], reverse=True)

sorted_regions, sorted_totals = zip(*sorted_sales_data)

# Colors for the bars
colors = ['#28A745', '#FF5733', '#007ACC', '#FFD700']  # Adjusted for better contrast

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 7))

# Plot sorted sales data as a bar chart
bar_width = 0.5
index = np.arange(len(sorted_regions))

bars = ax.bar(index, sorted_totals, bar_width, color=colors[:len(sorted_regions)], tick_label=sorted_regions)

# Add titles and labels
ax.set_title("Total Sales Data of Tech Gadgets Store by Region: First Half of the Year", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Regions", fontsize=14)
ax.set_ylabel("Total Sales (Thousands of Units)", fontsize=14)

# Annotate bars with their values
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