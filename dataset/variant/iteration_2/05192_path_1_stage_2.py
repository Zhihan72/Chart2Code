import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)

# Revenue data (in billions USD)
ai_revenue = [6, 9, 12, 18, 25, 40]
cybersecurity_revenue = [15, 18, 20, 23, 30, 45]
blockchain_revenue = [1, 2, 3, 6, 9, 12]
cloud_revenue = [5, 8, 15, 22, 30, 50]

bar_width = 0.2
x_pos = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 8))

uniform_color = '#0072B2'
ax.bar(x_pos - 1.5*bar_width, ai_revenue, bar_width, color=uniform_color)
ax.bar(x_pos - 0.5*bar_width, cybersecurity_revenue, bar_width, color=uniform_color)
ax.bar(x_pos + 0.5*bar_width, blockchain_revenue, bar_width, color=uniform_color)
ax.bar(x_pos + 1.5*bar_width, cloud_revenue, bar_width, color=uniform_color)

ax.set_xticks(x_pos)
ax.set_xticklabels([])  # Removing tick labels

# Remove y-axis grid and annotations
ax.yaxis.set_ticks([])
ax.yaxis.grid(False)

plt.tight_layout()
plt.show()