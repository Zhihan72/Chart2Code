import matplotlib.pyplot as plt
import numpy as np

pages = np.array([320, 50, 150, 400, 220, 180, 290, 300, 120, 200])
ratings = np.array([9, 5, 7, 6, 8, 7, 9, 9, 7, 8])
reading_duration = np.array([18, 5, 9, 22, 13, 10, 15, 17, 8, 12])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for number of pages vs satisfaction ratings
scatter = ax1.scatter(pages, ratings, color='purple', alpha=0.7, s=100, edgecolor='w')

# Adding trendline for number of pages vs satisfaction ratings
coef = np.polyfit(pages, ratings, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(pages, poly1d_fn(pages), color='violet', linestyle='--', linewidth=1)

# Customize primary y-axis
ax1.tick_params(axis='y', labelcolor='purple')
ax1.set_xlim(0, 450)
ax1.set_ylim(4, 10)

# Create a secondary y-axis for average reading duration
ax2 = ax1.twinx()
ax2.plot(pages, reading_duration, color='orange', marker='o', linestyle='-', linewidth=2)
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(0, 25)

# Grid
ax1.grid(True, linestyle='--', alpha=0.5)

plt.show()