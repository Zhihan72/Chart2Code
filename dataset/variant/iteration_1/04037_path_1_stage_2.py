import matplotlib.pyplot as plt
import numpy as np

# Data for months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Monthly sales in units for each type of ice cream
classic_sales = np.array([150, 180, 200, 230, 220, 250, 270, 290, 260, 240, 210, 190])
exotic_sales = np.array([120, 130, 160, 180, 190, 200, 210, 220, 205, 195, 175, 150])
seasonal_sales = np.array([90, 80, 95, 100, 105, 110, 120, 130, 125, 115, 100, 85])

x = np.arange(len(months))
width = 0.2  # Reduced width for grouped bars

fig, ax1 = plt.subplots(figsize=(14, 8))

# Grouped bar plots
ax1.bar(x - width, classic_sales, width, label='Classic', color='#1f77b4', edgecolor='black')
ax1.bar(x, exotic_sales, width, label='Exotic', color='#ff7f0e', edgecolor='black')
ax1.bar(x + width, seasonal_sales, width, label='Seasonal', color='#2ca02c', edgecolor='black')

ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Units Sold', fontsize=14)
ax1.set_title('2022 Ice Cream Sales', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45, ha='right')
ax1.legend()

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()