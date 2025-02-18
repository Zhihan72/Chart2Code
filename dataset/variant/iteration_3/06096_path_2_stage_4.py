import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_share = np.array([11, 14, 19, 26, 28, 33, 42, 44, 49])
revenue = np.array([0.5, 2.5, 3, 6, 8, 9.5, 12.5, 18, 21.5])
rnd_investment = np.array([0.3, 0.4, 0.9, 1.1, 1.7, 2.7, 3.5, 6, 6.5])
employee_growth = np.array([45, 65, 75, 115, 145, 205, 260, 340, 460])

fig, ax = plt.subplots(figsize=(14, 8))

# Changed the colors for each dataset
ax.fill_between(years, market_share, color='mediumseagreen', alpha=0.4, hatch='/', label='Mkt Share (%)')
ax.fill_between(years, revenue, color='skyblue', alpha=0.5, hatch='\\', label='Rev (M)')
ax.fill_between(years, rnd_investment, color='salmon', alpha=0.6, hatch='-', label='R&D Inv')
ax.fill_between(years, employee_growth, color='khaki', alpha=0.5, hatch='x', label='Emp Growth')

ax.set_title('Growth Metrics (2015-23)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Values (M)', fontsize=12)

ax.legend(loc='lower right', fontsize=10, title='Metrics', title_fontsize='11')
ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.3)

ax.annotate('Start-up', xy=(2015, market_share[0]), xytext=(2016.5, 12),
            arrowprops=dict(facecolor='darkgreen', arrowstyle='->'), fontsize=10, color='darkgreen')
ax.annotate('Rev Surge', xy=(2020, revenue[5]), xytext=(2021.5, 15),
            arrowprops=dict(facecolor='navy', arrowstyle='->'), fontsize=10, color='navy')
ax.annotate('R&D Boost', xy=(2022, rnd_investment[7]), xytext=(2023, 8),
            arrowprops=dict(facecolor='firebrick', arrowstyle='->'), fontsize=10, color='firebrick')
ax.annotate('Emp Spurt', xy=(2023, employee_growth[8]), xytext=(2020, 370),
            arrowprops=dict(facecolor='goldenrod', arrowstyle='->'), fontsize=10, color='goldenrod')

plt.tight_layout()
plt.show()