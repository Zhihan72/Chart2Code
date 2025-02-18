import matplotlib.pyplot as plt
import numpy as np

# Data for months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Monthly sales in units for each type of ice cream
classic_sales = np.array([150, 180, 200, 230, 220, 250, 270, 290, 260, 240, 210, 190])
exotic_sales = np.array([120, 130, 160, 180, 190, 200, 210, 220, 205, 195, 175, 150])
seasonal_sales = np.array([90, 80, 95, 100, 105, 110, 120, 130, 125, 115, 100, 85])

# Total sales each month
total_sales = classic_sales + exotic_sales + seasonal_sales

x = np.arange(len(months))  # the label locations
width = 0.25  # the width of the bars

fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked bar plots
ax1.bar(x, classic_sales, width, label='Classic', color='#1f77b4', edgecolor='black')
ax1.bar(x, exotic_sales, width, bottom=classic_sales, label='Exotic', color='#ff7f0e', edgecolor='black')
ax1.bar(x, seasonal_sales, width, bottom=classic_sales+exotic_sales, label='Seasonal', color='#2ca02c', edgecolor='black')

# Adding labels and title
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Units Sold', fontsize=14)
ax1.set_title('2022 Ice Cream Sales', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45, ha='right')
ax1.legend()

# Add y-axis grid for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding a secondary bar plot for total sales
ax2 = ax1.twinx()
ax2.plot(x, total_sales, "d--", color='purple', label='Total', linewidth=2)
ax2.set_ylabel("Total Units", fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Add legend for total sales
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()