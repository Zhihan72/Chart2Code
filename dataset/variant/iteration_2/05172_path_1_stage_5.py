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

# Create a color palette for each book type
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot each book type as a separate group
for i, book_type in enumerate(book_types):
    ax.bar(positions + i * width, revenue_data[i], width, label=book_type, color=colors[i])

ax.set_xticks(positions + width * (len(book_types)-1) / 2)
ax.set_xticklabels(years)
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Income (in Thousands)', fontsize=12)
ax.set_title('Yearly Income from Various Book Types\nJourney of a Local Bookshop (2010-2019)', fontsize=14, fontweight='bold')

ax.legend()

plt.tight_layout()
plt.show()