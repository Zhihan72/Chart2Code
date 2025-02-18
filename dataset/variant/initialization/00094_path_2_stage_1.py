import matplotlib.pyplot as plt
import numpy as np

percentages = [25, 35, 15, 10, 15]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

wedges, _ = ax.pie(percentages, startangle=140, colors=colors, pctdistance=0.85,
                   wedgeprops=dict(width=0.3), explode=(0.05, 0.05, 0.05, 0.05, 0.05))

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()