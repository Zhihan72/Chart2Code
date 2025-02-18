import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

wheat_yield = np.array([2.5, 3.0, 3.1, 3.3, 3.4, 3.6, 3.7, 3.8, 4.0, 4.2, 4.3])
corn_yield = np.array([5.2, 5.0, 5.3, 5.5, 5.7, 5.8, 6.0, 6.2, 6.3, 6.5, 6.6])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, wheat_yield, label='Wheat Harvest', color='forestgreen', marker='x', linewidth=2, linestyle='--')
ax.plot(years, corn_yield, label='Corn Production', color='purple', marker='^', linewidth=2.5, linestyle=':')

ax.set_title('Crop Yields from 2010 to 2020', fontsize=18, fontweight='bold', loc='left', pad=15)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Yield (tons)', fontsize=14)
ax.legend(loc='lower right', fontsize=11, frameon=False)

ax.grid(True, linestyle='-', alpha=0.9)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30)

ax.annotate('Sustainable\nPractices', xy=(2015, 3.6), xytext=(2012, 3.9),
            arrowprops=dict(facecolor='red', arrowstyle='->'),
            fontsize=11, backgroundcolor='lightyellow')
ax.annotate('Drought Effect', xy=(2012, 5.0), xytext=(2010, 5.7),
            arrowprops=dict(facecolor='red', arrowstyle='->'),
            fontsize=11, backgroundcolor='lightyellow')

plt.tight_layout()

plt.show()