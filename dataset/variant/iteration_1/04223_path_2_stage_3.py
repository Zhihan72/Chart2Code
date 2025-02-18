import matplotlib.pyplot as plt
import numpy as np

genres = [
    'Fiction', 'Non-Fiction', 'Mystery', 
    'Science Fiction', 'Biographies', 'Children',
    'Fantasy', 'Historical', 'Romance'
]
quarterly_checkouts = [
    [120, 80, 95, 130],   # Fiction
    [100, 110, 105, 90],  # Non-Fiction
    [60, 70, 75, 65],     # Mystery
    [50, 65, 60, 70],     # Science Fiction
    [40, 45, 40, 55],     # Biographies
    [30, 35, 40, 60],     # Children
    [90, 100, 110, 95],   # Fantasy
    [70, 80, 60, 75],     # Historical
    [95, 85, 105, 100]    # Romance
]

yearly_checkouts = [np.mean(q) for q in quarterly_checkouts]

fig, ax1 = plt.subplots(figsize=(14, 10))

bars = ax1.barh(genres, yearly_checkouts, color='skyblue', edgecolor='none')

for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width:.0f}', xy=(width, bar.get_y() + bar.get_height() / 2), 
                 xytext=(5, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

ax1.set_xlim(0, max(yearly_checkouts) + 20)
ax1.set_ylabel('Book Genres', fontsize=12)
ax1.set_xlabel('Average Yearly Check-Outs', fontsize=12)

plt.tight_layout()
plt.show()