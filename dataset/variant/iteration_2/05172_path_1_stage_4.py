import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
book_types = ['Tales', 'Biographies', 'Sci-Fi', 'Thrillers', 'Kids']

revenue_data = np.array([
    [55, 50, 80, 60, 85, 75, 64, 90, 52, 70],
    [35, 60, 30, 66, 43, 70, 32, 55, 40, 50],
    [40, 22, 45, 50, 30, 55, 28, 25, 20, 35],
    [30, 45, 25, 20, 15, 23, 50, 40, 35, 17],
    [45, 50, 55, 33, 40, 60, 25, 35, 30, 27],
])

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.15
positions = np.arange(len(years))
single_color = '#66b3ff'

bottoms = np.zeros(len(years))
for i, book_type in enumerate(book_types):
    ax.bar(positions, revenue_data[i], width, bottom=bottoms, color=single_color)
    bottoms += revenue_data[i]

ax.set_xticks(positions)
ax.set_xticklabels(years)
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Income (in Thousands)', fontsize=12)
ax.set_title('Yearly Income from Various Book Types\nJourney of a Local Bookshop (2010-2019)', fontsize=14, fontweight='bold')

for i in range(len(years)):
    total_value = sum(revenue_data[:, i])
    ax.text(i, total_value + 5, f'{total_value}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()