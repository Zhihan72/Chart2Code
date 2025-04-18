import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2020)
strawberries_yield = np.array([1.0, 1.2, 1.5, 2.0, 2.2, 2.4, 2.8, 3.0, 3.5, 3.8])
kale_yield = np.array([0.8, 1.0, 1.1, 1.3, 1.6, 1.8, 2.0, 2.2, 2.5, 2.7])
tomatoes_yield = np.array([1.5, 1.7, 1.8, 2.1, 2.4, 2.6, 3.0, 3.2, 3.4, 3.9])

cumulative_kale = strawberries_yield + kale_yield
cumulative_tomatoes = cumulative_kale + tomatoes_yield

fig, ax = plt.subplots(figsize=(10, 6))

ax.fill_between(years, strawberries_yield, color='#8A2BE2', alpha=0.6, label='Strawberries')  # Changed to blueviolet
ax.fill_between(years, cumulative_kale, strawberries_yield, color='#5F9EA0', alpha=0.6, label='Kale')  # Changed to cadetblue
ax.fill_between(years, cumulative_tomatoes, cumulative_kale, color='#DC143C', alpha=0.6, label='Tomatoes')  # Changed to crimson

ax.set_title('Organic Farm Harvest Trends\n(2010-2019)', fontsize=16, fontweight='bold', color='darkgreen')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Yield in Tonnes', fontsize=12)
ax.legend(loc='upper left', frameon=False, fontsize=10, title='Crops', title_fontsize='12')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 12, 1))
ax.yaxis.set_tick_params(labelsize=10)
ax.xaxis.set_tick_params(labelsize=10)
plt.xticks(rotation=45)

ax.annotate('Peak Strawberry Yield', xy=(2019, 3.8), xytext=(2015, 8),
            arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
            fontsize=10, color='black', fontweight='bold')

plt.tight_layout()
plt.show()