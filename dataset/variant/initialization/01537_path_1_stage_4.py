import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2020)
strawberries_yield = np.array([1.0, 1.2, 1.5, 2.0, 2.2, 2.4, 2.8, 3.0, 3.5, 3.8])
kale_yield = np.array([0.8, 1.0, 1.1, 1.3, 1.6, 1.8, 2.0, 2.2, 2.5, 2.7])
tomatoes_yield = np.array([1.5, 1.7, 1.8, 2.1, 2.4, 2.6, 3.0, 3.2, 3.4, 3.9])
blueberries_yield = np.array([0.5, 0.7, 0.9, 1.1, 1.3, 1.6, 1.8, 1.9, 2.2, 2.5])

price_strawberries = 1000
price_kale = 800
price_tomatoes = 900
price_blueberries = 1200

revenue_strawberries = strawberries_yield * price_strawberries
revenue_kale = kale_yield * price_kale
revenue_tomatoes = tomatoes_yield * price_tomatoes
revenue_blueberries = blueberries_yield * price_blueberries

total_revenue = revenue_strawberries + revenue_kale + revenue_tomatoes + revenue_blueberries

cumulative_kale = strawberries_yield + kale_yield
cumulative_tomatoes = cumulative_kale + tomatoes_yield
cumulative_blueberries = cumulative_tomatoes + blueberries_yield

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.fill_between(years, strawberries_yield, color='#FFD700', alpha=0.6)
ax1.fill_between(years, cumulative_kale, strawberries_yield, color='#FF6347', alpha=0.6)
ax1.fill_between(years, cumulative_tomatoes, cumulative_kale, color='#228B22', alpha=0.6)
ax1.fill_between(years, cumulative_blueberries, cumulative_tomatoes, color='#4169E1', alpha=0.6)

# ax1.set_title('Organic Farm Harvest and Revenue Trends\n(2010-2019)', fontsize=16, fontweight='bold', color='darkgreen')
# ax1.set_xlabel('Year', fontsize=12)
# ax1.set_ylabel('Yield in Tonnes', fontsize=12, color='black')

ax2 = ax1.twinx()
ax2.plot(years, total_revenue, color='blue', linewidth=2.5, linestyle='-', marker='o')
# ax2.set_ylabel('Revenue in $', fontsize=12, color='blue')

ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 12, 1))
ax1.yaxis.set_tick_params(labelsize=10)
ax1.xaxis.set_tick_params(labelsize=10)
ax2.set_yticks(np.arange(0, 40000, 5000))
ax2.yaxis.set_tick_params(labelsize=10, colors='blue')

plt.xticks(rotation=45)

# ax1.annotate('Peak Strawberry Yield', xy=(2019, 3.8), xytext=(2016, 9),
#              arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
#              fontsize=10, color='black', fontweight='bold')

# ax2.annotate('Peak Revenue', xy=(2019, total_revenue[-1]), xytext=(2016, 35000),
#              arrowprops=dict(facecolor='blue', arrowstyle='->', linewidth=1.5),
#              fontsize=10, color='blue', fontweight='bold')

plt.tight_layout()
plt.show()