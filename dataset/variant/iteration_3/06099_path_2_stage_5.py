import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
hypermarkets_sales = [500, 520, 540, 575, 600, 650, 700, 740, 800, 850, 900, 950]
corner_stores_sales = [300, 310, 320, 350, 370, 390, 420, 450, 480, 510, 550, 600]
ecommerce_sales = [150, 160, 170, 185, 200, 220, 240, 260, 280, 300, 330, 360]
artisan_shops_sales = [50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140]
kiosk_sales = [20, 25, 30, 40, 45, 50, 60, 70, 80, 90, 100, 110]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked bar chart
bar_width = 0.5
ax1.bar(months, hypermarkets_sales, color='#FFD700', width=bar_width, label='Hypermarkets')
ax1.bar(months, corner_stores_sales, bottom=hypermarkets_sales, color='#FF33A1', width=bar_width, label='Corner Stores')
ax1.bar(months, ecommerce_sales, bottom=np.array(hypermarkets_sales) + np.array(corner_stores_sales), color='#FF5733', width=bar_width, label='Ecommerce')
ax1.bar(months, artisan_shops_sales, bottom=np.array(hypermarkets_sales) + np.array(corner_stores_sales) + np.array(ecommerce_sales), color='#3357FF', width=bar_width, label='Artisan Shops')
ax1.bar(months, kiosk_sales, bottom=np.array(hypermarkets_sales) + np.array(corner_stores_sales) + np.array(ecommerce_sales) + np.array(artisan_shops_sales), color='#33FF57', width=bar_width, label='Kiosk')

ax1.set_xlabel("Timeline", fontsize=12)
ax1.set_ylabel("Unit Sales", fontsize=12)

ax1.set_xticks(range(len(months)))
ax1.set_xticklabels(months)

ax1.legend(loc='upper left')
fig.tight_layout()
plt.show()