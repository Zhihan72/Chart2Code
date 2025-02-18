import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
teens = np.array([0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3])
adults = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5])
seniors = np.array([1.0, 1.0, 1.1, 1.1, 1.2, 1.3, 1.2, 1.1, 1.1, 1.1, 1.2])

plt.figure(figsize=(14, 8))

plt.plot(years, teens, color='pink', marker='x', linestyle='--', linewidth=2, label='Teens')
plt.plot(years, adults, color='orange', marker='d', linestyle='-.', linewidth=2, label='Adults')
plt.plot(years, seniors, color='purple', marker='v', linestyle=':', linewidth=2, label='Seniors')

plt.title('Coffee Consumption (2010-2020)', fontsize=16, fontweight='bold', color='olive')
plt.xlabel('Year', fontsize=12, color='maroon')
plt.ylabel('Avg Cups/Day', fontsize=12, color='maroon')

plt.xticks(years, rotation=45)

plt.grid(False)  # Removed grid

plt.axvline(x=2015, linestyle='-', color='lightblue', linewidth=1.5)
plt.text(2015.5, 3.2, '2015 Peak', verticalalignment='center', horizontalalignment='left', color='lightblue', fontsize=10)

for year, cups in zip(years, teens):
    if year in [2010, 2015, 2020]:
        plt.annotate(f'{cups}', xy=(year, cups), textcoords='offset points', xytext=(-30, 10), ha='center', fontsize=9, color='pink')

plt.xlim(2010, 2020)
plt.ylim(0, 4)

plt.legend(loc='lower right', fontsize=10)  # Moved legend position

plt.tight_layout()

plt.show()