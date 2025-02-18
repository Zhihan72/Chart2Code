import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

classic_sales = np.array([150, 180, 200, 230, 220, 250, 270, 290, 260, 240, 210, 190])
seasonal_sales = np.array([90, 80, 95, 100, 105, 110, 120, 130, 125, 115, 100, 85])

x = np.arange(len(months))
width = 0.3

fig, ax1 = plt.subplots(figsize=(14, 8))

# Swapping colors between the two data groups
ax1.bar(x - width / 2, classic_sales, width, label='Classic', color='#2ca02c', edgecolor='black')
ax1.bar(x + width / 2, seasonal_sales, width, label='Seasonal', color='#1f77b4', edgecolor='black')

ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Units Sold', fontsize=14)
ax1.set_title('2022 Ice Cream Sales', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45, ha='right')
ax1.legend()
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()