import matplotlib.pyplot as plt
import numpy as np

elements_discovered = np.array([35, 20, 15, 18, 12])
colors = ['#1E90FF', '#FF69B4', '#32CD32', '#FFD700', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 7))
wedges = ax.pie(
    elements_discovered,
    colors=colors,
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w'),
    explode=(0.1, 0, 0, 0, 0.2)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.show()