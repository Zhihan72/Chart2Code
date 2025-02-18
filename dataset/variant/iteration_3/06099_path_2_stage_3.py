import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
hypermarkets_sales = [500, 520, 540, 575, 600, 650, 700, 740, 800, 850, 900, 950]
corner_stores_sales = [300, 310, 320, 350, 370, 390, 420, 450, 480, 510, 550, 600]
ecommerce_sales = [150, 160, 170, 185, 200, 220, 240, 260, 280, 300, 330, 360]
artisan_shops_sales = [50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140]
kiosk_sales = [20, 25, 30, 40, 45, 50, 60, 70, 80, 90, 100, 110]

total_revenue = np.array(hypermarkets_sales) + np.array(corner_stores_sales) \
                + np.array(ecommerce_sales) + np.array(artisan_shops_sales) \
                + np.array(kiosk_sales)

sales_increase_rate = np.diff(total_revenue) / total_revenue[:-1] * 100
sales_increase_rate = np.insert(sales_increase_rate, 0, 0)

bar_width = 0.15
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.bar(r1, hypermarkets_sales, color='#FF5733', width=bar_width, edgecolor='none')
ax1.bar(r2, corner_stores_sales, color='#33FF57', width=bar_width, edgecolor='none')
ax1.bar(r3, ecommerce_sales, color='#3357FF', width=bar_width, edgecolor='none')
ax1.bar(r4, artisan_shops_sales, color='#FF33A1', width=bar_width, edgecolor='none')
ax1.bar(r5, kiosk_sales, color='#FFD700', width=bar_width, edgecolor='none')

ax2 = ax1.twinx()
ax2.plot(months, sales_increase_rate, color='#FFA500', marker='o', linewidth=2)

ax1.set_xlabel("Timeline", fontsize=12)
ax1.set_ylabel("Unit Sales", fontsize=12)
ax2.set_ylabel("Increase Rate (%)", fontsize=12, color='#FFA500')

ax1.set_xticks([r + bar_width*2 for r in range(len(months))])
ax1.set_xticklabels(months)

fig.tight_layout()
plt.show()