import matplotlib.pyplot as plt
import numpy as np

# Randomly altered content within the same dimensional structure
pages = np.array([300, 50, 180, 400, 290, 320, 120, 220, 200, 150])
ratings = np.array([8, 9, 5, 6, 9, 7, 9, 7, 8, 7])
reading_duration = np.array([17, 10, 5, 22, 15, 18, 8, 13, 12, 9])

fig, ax1 = plt.subplots(figsize=(12, 8))

scatter = ax1.scatter(pages, ratings, color='purple', label='Readers\' Delight', alpha=0.6, s=120, marker='D', edgecolor='gray')

coef = np.polyfit(pages, ratings, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(pages, poly1d_fn(pages), color='teal', linestyle='-.', linewidth=2, label='Popularity Pathway')

ax1.set_xlabel('Pages in Tome', fontsize=12)
ax1.set_ylabel('Delight Scale (1-10)', color='purple', fontsize=12)
ax1.tick_params(axis='y', labelcolor='purple')
ax1.set_xlim(0, 450)
ax1.set_ylim(4, 10)

ax2 = ax1.twinx()
ax2.plot(pages, reading_duration, color='navy', marker='^', linestyle=':', linewidth=3, label='Time Spent Perusing')
ax2.set_ylabel('Hours Spent Engaged', color='navy', fontsize=12)
ax2.tick_params(axis='y', labelcolor='navy')
ax2.set_ylim(0, 25)

plt.title('Exploring Tome Length, Delight & Engagement Time', fontsize=16, fontweight='bold', pad=15)
ax1.grid(True, linestyle='-.', alpha=0.4)

fig.tight_layout()
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', frameon=True, shadow=True)

plt.show()