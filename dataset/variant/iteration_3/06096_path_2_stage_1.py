import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_share = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
revenue = np.array([1, 2, 3.5, 5, 7.5, 10, 13.5, 17, 22])
rnd_investment = np.array([0.2, 0.5, 0.8, 1.2, 1.8, 2.5, 4, 5.5, 7])
employee_growth = np.array([50, 60, 80, 110, 150, 200, 270, 350, 450])

fig, ax = plt.subplots(figsize=(14, 8))

# Alter fill styles and labels
ax.fill_between(years, market_share, color='coral', alpha=0.4, hatch='/', label='Market Share (%)')
ax.fill_between(years, revenue, color='lightblue', alpha=0.5, hatch='\\', label='Revenue (Millions)')
ax.fill_between(years, rnd_investment, color='lightgreen', alpha=0.6, hatch='-', label='R&D Investment')
ax.fill_between(years, employee_growth, color='gold', alpha=0.5, hatch='x', label='Employee Growth')

ax.set_title('Growth Metrics of Software Company (2015-2023)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Values (millions)', fontsize=12)

# Modified legend styling
ax.legend(loc='lower right', fontsize=10, title='Company Metrics', title_fontsize='11')

# Change grid style
ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.3)

ax.annotate('Start-up Phase', xy=(2015, market_share[0]), xytext=(2016.5, 12),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')
ax.annotate('Revenue Surge', xy=(2020, revenue[5]), xytext=(2021.5, 15),
            arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='green')
ax.annotate('Major R&D Boost', xy=(2022, rnd_investment[7]), xytext=(2023, 8),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='red')
ax.annotate('Employee Growth Spurt', xy=(2023, employee_growth[8]), xytext=(2020, 370),
            arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=10, color='orange')

plt.tight_layout()
plt.show()