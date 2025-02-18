import numpy as np
import matplotlib.pyplot as plt

years = np.array(['2000', '2005', '2010', '2015', '2020'])
dogs = np.array([60, 65, 70, 75, 80])
cats = np.array([55, 58, 60, 62, 65])
birds = np.array([15, 20, 22, 25, 28])
fish = np.array([30, 32, 35, 38, 40])
reptiles = np.array([5, 7, 9, 10, 12])
small_mammals = np.array([10, 12, 14, 16, 18])

colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(years, dogs, color=colors[0], alpha=0.9)
ax.bar(years, cats, bottom=dogs, color=colors[1], alpha=0.9)
ax.bar(years, birds, bottom=dogs + cats, color=colors[2], alpha=0.9)
ax.bar(years, fish, bottom=dogs + cats + birds, color=colors[3], alpha=0.9)
ax.bar(years, reptiles, bottom=dogs + cats + birds + fish, color=colors[4], alpha=0.9)
ax.bar(years, small_mammals, bottom=dogs + cats + birds + fish + reptiles, color=colors[5], alpha=0.9)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

plt.tight_layout()
plt.show()