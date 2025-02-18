import matplotlib.pyplot as plt
import numpy as np

# Months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Sales data for store types
supermarket_sales = [500, 520, 540, 575, 600, 650, 700, 740, 800, 850, 900, 950]
convenience_sales = [300, 310, 320, 350, 370, 390, 420, 450, 480, 510, 550, 600]
online_sales = [150, 160, 170, 185, 200, 220, 240, 260, 280, 300, 330, 360]
specialty_sales = [50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140]

# Overall sales data by summing up all store types
total_sales = np.array(supermarket_sales) + np.array(convenience_sales) \
              + np.array(online_sales) + np.array(specialty_sales)

# Calculate month-over-month growth rate
growth_rate = np.diff(total_sales) / total_sales[:-1] * 100
growth_rate = np.insert(growth_rate, 0, 0)

# Bar positions
bar_width = 0.2
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Grouped bar chart
ax1.bar(r1, supermarket_sales, color='#FF5733', width=bar_width)
ax1.bar(r2, convenience_sales, color='#33FF57', width=bar_width)
ax1.bar(r3, online_sales, color='#3357FF', width=bar_width)
ax1.bar(r4, specialty_sales, color='#FF33A1', width=bar_width)

# Growth rate line
ax2 = ax1.twinx()
ax2.plot(months, growth_rate, color='#FFA500', marker='o', linewidth=2)

# Labels
ax1.set_xlabel("Mth", fontsize=12)
ax1.set_ylabel("Sales (u)", fontsize=12)
ax2.set_ylabel("Grth (%)", fontsize=12, color='#FFA500')

# Set ticks
ax1.set_xticks([r + bar_width*1.5 for r in range(len(months))])
ax1.set_xticklabels(months)

# Layout
fig.tight_layout()

# Display
plt.show()