import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2024)
# Manually shuffled sales data within individual lists
traditional_books_sales = [810, 820, 800, 760, 770, 780, 740, 750, 730, 720, 680, 700, 640, 660, 680, 600, 560, 340, 440, 480, 380, 360, 350, 520]
e_books_sales = [710, 10, 700, 20, 690, 80, 370, 270, 50, 710, 120, 180, 460, 500, 80, 600, 620, 640, 660, 680, 270, 320, 220, 420]
audiobooks_sales = [270, 0, 0, 0, 220, 0, 0, 330, 0, 10, 0, 110, 20, 130, 70, 90, 30, 50, 0, 180, 330, 150, 0, 0]

sales_data = np.vstack([traditional_books_sales, e_books_sales, audiobooks_sales])

fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
ax.stackplot(years, sales_data, labels=['Printed Books', 'Digital Volumes', 'Spoken Editions'], 
             colors=colors, alpha=0.9)

plt.title('Shifts in Literature Mediums\n(2000-2023)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Chronological Span', fontsize=14, labelpad=10)
plt.ylabel('Quantitative Distribution (x1000)', fontsize=14, labelpad=10)

plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 901, 100))
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend(loc='upper left', fontsize=12, frameon=False)

ax.annotate('E-volumes Surge', xy=(2012, 200), xytext=(2005, 450),
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='orange', ha='center')

ax.annotate('Audiobook Ascension', xy=(2020, 330), xytext=(2013, 500),
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='green', ha='center')

plt.tight_layout()

left, bottom, width, height = [0.6, 0.5, 0.3, 0.3]
ax_inset = fig.add_axes([left, bottom, width, height])
ax_inset.plot(years, audiobooks_sales, marker='o', color='#2ca02c', linestyle='-')
ax_inset.set_title('Audiobook Trend', fontsize=10)
ax_inset.set_xlabel('Timeline', fontsize=8)
ax_inset.set_ylabel('Sales (x1000)', fontsize=8)
ax_inset.tick_params(axis='both', which='major', labelsize=8)

plt.show()