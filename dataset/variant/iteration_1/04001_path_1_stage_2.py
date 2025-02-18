import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

wheat_yield = np.array([2.5, 3.0, 3.1, 3.3, 3.4, 3.6, 3.7, 3.8, 4.0, 4.2, 4.3])
corn_yield = np.array([5.2, 5.0, 5.3, 5.5, 5.7, 5.8, 6.0, 6.2, 6.3, 6.5, 6.6])
soybean_yield = np.array([1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 2.0, 2.1, 2.2, 2.3, 2.5])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, wheat_yield, label='Wheat', color='darkorange', marker='o', linewidth=2, linestyle='-')
ax.plot(years, corn_yield, label='Corn', color='dodgerblue', marker='s', linewidth=2, linestyle='-.')
ax.plot(years, soybean_yield, label='Soy', color='mediumvioletred', marker='^', linewidth=2, linestyle='--')

ax.set_title('Crop Yields (2010-2020)', fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Yield (tons)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, frameon=True)

ax.grid(True, linestyle='--', alpha=0.6)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.annotate('Sustainable\nPractices', xy=(2015, 3.6), xytext=(2013, 4.0),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Drought', xy=(2012, 5.0), xytext=(2009, 5.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('New Variety', xy=(2017, 2.1), xytext=(2015, 2.2),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')

plt.tight_layout()

plt.show()