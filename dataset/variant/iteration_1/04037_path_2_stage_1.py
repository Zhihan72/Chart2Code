import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

classic_sales = np.array([150, 180, 200, 230, 220, 250, 270, 290, 260, 240, 210, 190])
exotic_sales = np.array([120, 130, 160, 180, 190, 200, 210, 220, 205, 195, 175, 150])
seasonal_sales = np.array([90, 80, 95, 100, 105, 110, 120, 130, 125, 115, 100, 85])

total_sales = classic_sales + exotic_sales + seasonal_sales

x = np.arange(len(months))
width = 0.25

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.bar(x, classic_sales, width, color='#1f77b4')
ax1.bar(x, exotic_sales, width, bottom=classic_sales, color='#ff7f0e')
ax1.bar(x, seasonal_sales, width, bottom=classic_sales+exotic_sales, color='#2ca02c')

ax1.set_xlabel('Months', fontsize=14)
ax1.set_ylabel('Sales (Units)', fontsize=14)
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45, ha='right')

ax2 = ax1.twinx()
ax2.plot(x, total_sales, "d--", color='purple', linewidth=2)
ax2.set_ylabel("Total Sales (Units)", fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

plt.tight_layout()
plt.show()