import matplotlib.pyplot as plt
import numpy as np

fruits = ["Apple", "Banana", "Orange", "Blueberry", "Strawberry", "Grapes", "Kiwi", "Watermelon"]
vitamin_content = [6, 10, 70, 9, 32, 10, 92, 8]
avg_rating = [7.5, 8.0, 9.0, 8.5, 9.5, 7.0, 8.5, 7.0]

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.bar(fruits, vitamin_content, color="teal", edgecolor='gray', linewidth=1.5)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval} mg', ha='center', va='bottom', color='navy', fontsize=11)

ax1.set_xlabel('Delicious Fruits', fontsize=14)
ax1.set_ylabel('Vitamin Power (mg per 100g)', fontsize=14)
ax1.set_title('Vitamin Explosion and Taste Test of Fruits', fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='-.', color='grey', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(fruits, avg_rating, color="goldenrod", marker='s', linestyle='--', linewidth=3, markersize=8, label='Taste Score (out of 10)')

for i, rating in enumerate(avg_rating):
    ax2.text(i, rating + 0.2, f'{rating}', ha='center', va='bottom', color='darkgreen', fontsize=10)

ax2.set_ylabel('Taste Score Board', fontsize=14, color='goldenrod')
ax2.tick_params(axis='y', labelcolor='goldenrod')

ax2.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.show()