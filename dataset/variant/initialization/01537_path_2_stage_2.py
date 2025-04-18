import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2020)
strawberries_yield = np.array([1.0, 1.2, 1.5, 2.0, 2.2, 2.4, 2.8, 3.0, 3.5, 3.8])
tomatoes_yield = np.array([1.5, 1.7, 1.8, 2.1, 2.4, 2.6, 3.0, 3.2, 3.4, 3.9])

price_strawberries = 1000
price_tomatoes = 900

revenue_strawberries = strawberries_yield * price_strawberries
revenue_tomatoes = tomatoes_yield * price_tomatoes

total_revenue = revenue_strawberries + revenue_tomatoes

cumulative_tomatoes = strawberries_yield + tomatoes_yield

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.fill_between(years, strawberries_yield, color='#228B22', alpha=0.6, label='Strawberries')
ax1.fill_between(years, cumulative_tomatoes, strawberries_yield, color='#FF6347', alpha=0.6, label='Tomatoes')

ax1.set_title('Organic Farm Harvest and Revenue Trends\n(2010-2019)', fontsize=16, fontweight='bold', color='darkgreen')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Yield in Tonnes', fontsize=12, color='black')

ax2 = ax1.twinx()
ax2.plot(years, total_revenue, color='blue', linewidth=2.5, linestyle='-', marker='o', label='Total Revenue ($)')
ax2.set_ylabel('Revenue in $', fontsize=12, color='blue')

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 1.0), fontsize=10, title='Crops and Revenue', title_fontsize='12')

ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 12, 1))
ax1.yaxis.set_tick_params(labelsize=10)
ax1.xaxis.set_tick_params(labelsize=10)
ax2.set_yticks(np.arange(0, 25000, 5000))
ax2.yaxis.set_tick_params(labelsize=10, colors='blue')

plt.xticks(rotation=45)

ax1.annotate('Peak Strawberry Yield', xy=(2019, 3.8), xytext=(2016, 9),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
             fontsize=10, color='black', fontweight='bold')

ax2.annotate('Peak Revenue', xy=(2019, total_revenue[-1]), xytext=(2016, 20000),
             arrowprops=dict(facecolor='blue', arrowstyle='->', linewidth=1.5),
             fontsize=10, color='blue', fontweight='bold')

plt.tight_layout()
plt.show()