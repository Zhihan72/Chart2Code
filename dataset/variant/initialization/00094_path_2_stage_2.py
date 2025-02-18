import matplotlib.pyplot as plt
import numpy as np

# Original data series
percentages = [25, 35, 15, 10, 15]
# Add additional made-up data series
added_percentages = [8, 12]
# Overall percentages now become
percentages = percentages + added_percentages

# Original colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
# Add colors for new segments
added_colors = ['#8c564b', '#e377c2']
# Overall color list
colors = colors + added_colors

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Note: updating explode to match the total number of wedges
wedges, _ = ax.pie(percentages, startangle=140, colors=colors, pctdistance=0.85,
                   wedgeprops=dict(width=0.3), explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05))

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()