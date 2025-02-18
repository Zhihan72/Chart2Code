import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2019, 2024)
food_delivery = np.array([3, 5, 7, 9, 12])
online_retail = np.array([15, 25, 35, 45, 60])

ecommerce_data = np.vstack([food_delivery, online_retail])

fig, (ax1) = plt.subplots(figsize=(14, 8))

colors = ['#ffa07a', '#98fb98']
ax1.stackplot(years, ecommerce_data, labels=['Food Delivery', 'Online Retail'], 
              colors=colors, alpha=0.75)

ax1.set_title("E-commerce Growth during and after COVID-19 Pandemic\n(2019-2023)", fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Revenue (Billions of Dollars)', fontsize=14)

ax1.legend(loc='upper right', fontsize=12, title='Sector', frameon=True, shadow=True)
ax1.grid(linestyle='-', alpha=0.3)

ax1.annotate('Surge in\nFood Delivery', xy=(2020, 5), xytext=(2020.5, 18),
             arrowprops=dict(facecolor='red', arrowstyle='-['),
             fontsize=13, color='red')

ax1.annotate('Boom in\nOnline Retail', xy=(2021, 35), xytext=(2021.5, 60),
             arrowprops=dict(facecolor='blue', arrowstyle='-['),
             fontsize=13, color='blue')

props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray')
textstr = ('E-commerce innovation surged,\n'
           'spanning food delivery and retail sectors.')
ax1.text(0.02, 0.95, textstr, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

for idx, sector in enumerate(['Food Delivery', 'Online Retail']):
    ax1.annotate(f'{ecommerce_data[idx, 0]}', (2019, ecommerce_data[idx, 0]),
                 textcoords="offset points", xytext=(-10, 5), ha='center', color='black')
    ax1.annotate(f'{ecommerce_data[idx, -1]}', (2023, ecommerce_data[idx, -1] + np.sum(ecommerce_data[:idx, -1])),
                 textcoords="offset points", xytext=(-15, -10), ha='center', color='black')

plt.tight_layout()
plt.show()