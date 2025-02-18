import matplotlib.pyplot as plt
import numpy as np

# Months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Sales data for store types
supermarket_sales = [500, 520, 540, 575, 600, 650, 700, 740, 800, 850, 900, 950]
convenience_sales = [300, 310, 320, 350, 370, 390, 420, 450, 480, 510, 550, 600]
online_sales = [150, 160, 170, 185, 200, 220, 240, 260, 280, 300, 330, 360]

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked bar chart
ax1.bar(months, supermarket_sales, color='#1E90FF', label='Supermarket')  # DodgerBlue
ax1.bar(months, convenience_sales, bottom=supermarket_sales, color='#32CD32', label='Convenience')  # LimeGreen
ax1.bar(months, online_sales, bottom=np.array(supermarket_sales) + np.array(convenience_sales), color='#FFD700', label='Online')  # Gold

# Labels
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Sales (units)", fontsize=12)

# Legend
ax1.legend()

# Layout
fig.tight_layout()

# Display
plt.show()