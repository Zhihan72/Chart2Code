import matplotlib.pyplot as plt
import numpy as np

pages = np.array([320, 50, 150, 400, 220, 180, 290, 300, 120, 200])
ratings = np.array([9, 5, 7, 6, 8, 7, 9, 9, 7, 8])
reading_duration = np.array([18, 5, 9, 22, 13, 10, 15, 17, 8, 12])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Randomly altered stylistic elements

# Scatter plot with stars marker and different colors
scatter = ax1.scatter(pages, ratings, color='green', alpha=0.7, s=120, marker='*', edgecolor='black')

# Adding thicker solid trendline
coef = np.polyfit(pages, ratings, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(pages, poly1d_fn(pages), color='blue', linestyle='-', linewidth=2)

# Customize primary y-axis
ax1.tick_params(axis='y', labelcolor='green')
ax1.set_xlim(0, 450)
ax1.set_ylim(4, 10)

# Create a secondary y-axis with square marker and dashed line
ax2 = ax1.twinx()
ax2.plot(pages, reading_duration, color='red', marker='s', linestyle='--', linewidth=1.5)
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(0, 25)

# Grid with dotted style
ax1.grid(True, linestyle=':', alpha=0.7)

plt.show()