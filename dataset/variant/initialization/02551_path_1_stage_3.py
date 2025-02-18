import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

teenagers = np.array([0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3])
adults = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5])
seniors = np.array([1.0, 1.0, 1.1, 1.1, 1.2, 1.3, 1.2, 1.1, 1.1, 1.1, 1.2])

students = np.array([1.0, 1.1, 1.2, 1.2, 1.3, 1.3, 1.4, 1.5, 1.5, 1.6, 1.7])
retirees = np.array([1.3, 1.3, 1.4, 1.4, 1.5, 1.6, 1.6, 1.5, 1.5, 1.6, 1.7])

plt.figure(figsize=(14, 8))

plt.plot(years, teenagers, color='green', marker='o', linestyle='-', linewidth=2, label='Teens')   # Color changed to green
plt.plot(years, adults, color='purple', marker='s', linestyle='-', linewidth=2, label='Adults')   # Color changed to purple
plt.plot(years, seniors, color='orange', marker='^', linestyle='-', linewidth=2, label='Seniors') # Color changed to orange

plt.plot(years, students, color='blue', marker='d', linestyle='-', linewidth=2, label='Students') # Color changed to blue
plt.plot(years, retirees, color='red', marker='x', linestyle='-', linewidth=2, label='Retirees')  # Color changed to red

plt.title('Coffee Use by Age (2010-20)', fontsize=16, fontweight='bold', color='brown')
plt.xlabel('Year', fontsize=12, color='darkblue')
plt.ylabel('Avg Cups/Day', fontsize=12, color='darkblue')

plt.xticks(years, rotation=45)

plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.axvline(x=2015, linestyle='--', color='purple', linewidth=1.5)
plt.text(2015.5, 3.2, 'Key Yr', verticalalignment='center', horizontalalignment='left', color='purple', fontsize=10)

for year, cups in zip(years, teenagers):
    if year in [2010, 2015, 2020]:
        plt.annotate(f'{cups} c', xy=(year, cups), textcoords='offset points', xytext=(-30, 10), ha='center', fontsize=9, color='green') # Updated annotation color to match teenagers' line

plt.xlim(2010, 2020)
plt.ylim(0, 4)

plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()