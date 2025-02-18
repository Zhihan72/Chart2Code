import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

classic_sales = np.array([240, 190, 270, 200, 150, 250, 180, 290, 260, 230, 220, 210])
exotic_sales = np.array([175, 130, 150, 205, 195, 180, 120, 160, 210, 220, 200, 190])
seasonal_sales = np.array([100, 85, 120, 80, 115, 130, 90, 95, 110, 105, 125, 100])

x = np.arange(len(months))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

# Applying a single color to all data groups
single_color = '#1f77b4'
ax.bar(x - width, classic_sales, width, color=single_color)
ax.bar(x, exotic_sales, width, color=single_color)
ax.bar(x + width, seasonal_sales, width, color=single_color)

ax.set_xticks(x)
ax.set_xticklabels([])

plt.tight_layout()
plt.show()