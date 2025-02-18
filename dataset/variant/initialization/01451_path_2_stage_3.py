import matplotlib.pyplot as plt
import numpy as np

retreats = ['Mars', 'Jupiter', 'Venus', 'Saturn', 'Neptune']
intellectual_diversity = np.array([80, 60, 70, 85, 55])

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(retreats, intellectual_diversity, color='skyblue')

ax.set_title("Intellectual Diversity of Galactic Writers' Retreats", fontsize=14, fontweight='bold')
ax.set_xlabel('Intellectual Diversity', fontsize=12)

plt.show()