import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

# Coffee consumption data
teenagers_consumption = np.array([0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3])
adults_consumption = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5])
seniors_consumption = np.array([1.0, 1.0, 1.1, 1.1, 1.2, 1.3, 1.2, 1.1, 1.1, 1.1, 1.2])

# Additional data series
students_consumption = np.array([1.0, 1.1, 1.2, 1.2, 1.3, 1.3, 1.4, 1.5, 1.5, 1.6, 1.7])
retirees_consumption = np.array([1.3, 1.3, 1.4, 1.4, 1.5, 1.6, 1.6, 1.5, 1.5, 1.6, 1.7])

plt.figure(figsize=(14, 8))

plt.plot(years, teenagers_consumption, color='blue', marker='o', linestyle='-', linewidth=2, label='Teenagers (13-19)')
plt.plot(years, adults_consumption, color='green', marker='s', linestyle='-', linewidth=2, label='Adults (20-39)')
plt.plot(years, seniors_consumption, color='red', marker='^', linestyle='-', linewidth=2, label='Seniors (40+)')

plt.plot(years, students_consumption, color='orange', marker='d', linestyle='-', linewidth=2, label='Students (19-25)')
plt.plot(years, retirees_consumption, color='purple', marker='x', linestyle='-', linewidth=2, label='Retirees (65+)')

plt.title('Trends in Coffee Consumption Across\nDifferent Age Groups (2010-2020)', fontsize=16, fontweight='bold', color='brown')
plt.xlabel('Year', fontsize=12, color='darkblue')
plt.ylabel('Average Cups of Coffee per Day', fontsize=12, color='darkblue')

plt.xticks(years, rotation=45)

plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.axvline(x=2015, linestyle='--', color='purple', linewidth=1.5)
plt.text(2015.5, 3.2, 'Significant\nYear', verticalalignment='center', horizontalalignment='left', color='purple', fontsize=10)

for year, cups in zip(years, teenagers_consumption):
    if year in [2010, 2015, 2020]:
        plt.annotate(f'{cups} cups', xy=(year, cups), textcoords='offset points', xytext=(-30, 10), ha='center', fontsize=9, color='blue')

plt.xlim(2010, 2020)
plt.ylim(0, 4)

plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()