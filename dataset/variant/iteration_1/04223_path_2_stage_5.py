import matplotlib.pyplot as plt
import numpy as np

genres = [
    'Non-Fiction', 'Fantasy', 'Historical', 
    'Children', 'Science Fiction', 'Biographies',
    'Mystery', 'Fiction', 'Romance'
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

# Applying a new set of colors to the bars
new_colors = [
    '#FF5733', '#33FF57', '#3357FF', 
    '#F3FF33', '#FF33F3', '#33FFF3',
    '#F333FF', '#33F3FF', '#FF3F33'
]
bars = ax1.barh(genres, yearly_checkouts, color=new_colors, edgecolor='none')

for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width:.0f}', xy=(width, bar.get_y() + bar.get_height() / 2), 
                 xytext=(5, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

ax1.set_xlim(0, max(yearly_checkouts) + 20)
ax1.set_ylabel('Categories', fontsize=12)
ax1.set_xlabel('Avg Yearly Check-Outs', fontsize=12)

plt.tight_layout()
plt.title('Library Book Checkout Summary', fontsize=14, pad=20)
plt.show()