import matplotlib.pyplot as plt
import numpy as np

# Define the months and store types
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
store_types = ["Supermarkets", "Convenience Stores", "Online Retailers", "Specialty Shops", "Pop-up Stands"]

# Sales data for each store type (in units)
supermarkets_sales = [500, 520, 540, 575, 600, 650, 700, 740, 800, 850, 900, 950]
convenience_stores_sales = [300, 310, 320, 350, 370, 390, 420, 450, 480, 510, 550, 600]
online_retailers_sales = [150, 160, 170, 185, 200, 220, 240, 260, 280, 300, 330, 360]
specialty_shops_sales = [50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140]
popup_stands_sales = [20, 25, 30, 40, 45, 50, 60, 70, 80, 90, 100, 110]

# Overall sales data by summing up all store types
total_sales = np.array(supermarkets_sales) + np.array(convenience_stores_sales) \
              + np.array(online_retailers_sales) + np.array(specialty_shops_sales) \
              + np.array(popup_stands_sales)

# Calculate month-over-month growth rate (in percentage)
growth_rate = np.diff(total_sales) / total_sales[:-1] * 100
growth_rate = np.insert(growth_rate, 0, 0)

# Create the bar positions for grouped bar chart
bar_width = 0.15
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the sales data as grouped bar chart
ax1.bar(r1, supermarkets_sales, color='#FF5733', width=bar_width, edgecolor='grey', label='Supermarkets')
ax1.bar(r2, convenience_stores_sales, color='#33FF57', width=bar_width, edgecolor='grey', label='Convenience Stores')
ax1.bar(r3, online_retailers_sales, color='#3357FF', width=bar_width, edgecolor='grey', label='Online Retailers')
ax1.bar(r4, specialty_shops_sales, color='#FF33A1', width=bar_width, edgecolor='grey', label='Specialty Shops')
ax1.bar(r5, popup_stands_sales, color='#FFD700', width=bar_width, edgecolor='grey', label='Pop-up Stands')

# Create second y-axis to plot the growth rate
ax2 = ax1.twinx()
ax2.plot(months, growth_rate, color='#FFA500', marker='o', linewidth=2, label='Growth Rate (%)')

# Titles and labels
ax1.set_title("AquaFizz Monthly Sales Performance\nAcross Store Types in 2023", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Sales (units)", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12, color='#FFA500')

# Set ticks and grid
ax1.set_xticks([r + bar_width*2 for r in range(len(months))])
ax1.set_xticklabels(months)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.yaxis.grid(False)

# Configure and place the legends
ax1.legend(title='Store Types', fontsize=10, loc='upper left')
ax2.legend(loc='upper right', fontsize=10)

# Avoid overlapping
fig.tight_layout()

# Display the plot
plt.show()