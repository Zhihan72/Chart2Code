import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# Title: "Monthly Sales of Organic Fertilizers across Different Countries"
# Imagine we are plotting the monthly sales data of organic fertilizers in different countries.
# The countries in focus are USA, Canada, Germany, Australia, and India.
# We aim to visualize the sales performance over a year.

# Define the data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
countries = ['USA', 'Canada', 'Germany', 'Australia', 'India']
sales_data = np.array([
    [120, 100, 110, 140, 150, 130, 145, 180, 160, 175, 190, 210],  # USA
    [90, 85, 100, 95, 105, 115, 120, 130, 140, 150, 160, 170],    # Canada
    [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],   # Germany
    [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170],     # Australia
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]    # India
])

# Average monthly sales - across all countries
average_sales = sales_data.mean(axis=0)

# Create a figure with bar plot, featuring subplots if needed
fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
index = np.arange(len(months))

# Plot individual country sales data
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#800080']
for i, country in enumerate(countries):
    ax.bar(index + i * bar_width, sales_data[i], bar_width, label=country, color=colors[i], alpha=0.75)

# Plot average monthly sales as a line
ax.plot(index + 2 * bar_width, average_sales, color='black', linestyle='-', marker='o', linewidth=2, markersize=6, label='Average Sales')

# Set Title and Labels
ax.set_title('Monthly Sales of Organic Fertilizers across Different Countries', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Units Sold (in thousands)', fontsize=12)
ax.set_xticks(index + 2 * bar_width)
ax.set_xticklabels(months, rotation=45)
ax.legend(title='Countries', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Make sure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()