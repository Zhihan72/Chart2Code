import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
book_types = ['Tales', 'Biographies', 'Sci-Fi', 'Thrillers', 'Kids']

revenue_data = np.array([
    [50, 52, 55, 60, 64, 70, 75, 80, 85, 90],
    [30, 32, 35, 40, 43, 50, 55, 60, 66, 70],
    [20, 22, 25, 28, 30, 35, 40, 45, 50, 55],
    [15, 17, 20, 23, 25, 30, 35, 40, 45, 50],
    [25, 27, 30, 33, 35, 40, 45, 50, 55, 60],
])

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.15
positions = np.arange(len(years))
single_color = '#66b3ff'  # Use a single color consistently

bottoms = np.zeros(len(years))
for i, book_type in enumerate(book_types):
    ax.bar(positions, revenue_data[i], width, bottom=bottoms, color=single_color, label=book_type)
    bottoms += revenue_data[i]

ax.set_xticks(positions)
ax.set_xticklabels(years)
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Income (in Thousands)', fontsize=12)
ax.set_title('Yearly Income from Various Book Types\nJourney of a Local Bookshop (2010-2019)', fontsize=14, fontweight='bold')
ax.legend(title='Types of Books', fontsize=10)

for i in range(len(years)):
    total_value = sum(revenue_data[:, i])
    ax.text(i, total_value + 5, f'{total_value}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()