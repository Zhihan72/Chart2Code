import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

classic_sales = np.array([150, 180, 200, 230, 220, 250, 270, 290, 260, 240, 210, 190])
exotic_sales = np.array([120, 130, 160, 180, 190, 200, 210, 220, 205, 195, 175, 150])
seasonal_sales = np.array([90, 80, 95, 100, 105, 110, 120, 130, 125, 115, 100, 85])

x = np.arange(len(months))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(x - width, classic_sales, width, label='Classic', color='#1f77b4')
ax.bar(x, exotic_sales, width, label='Exotic', color='#ff7f0e')
ax.bar(x + width, seasonal_sales, width, label='Seasonal', color='#2ca02c')

ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Sales (Units)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(months, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()