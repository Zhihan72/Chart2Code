import matplotlib.pyplot as plt
import numpy as np

xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]
orbis_popularity = [92, 72, 80, 85, 68]

fig, ax = plt.subplots(figsize=(12, 7))
r = np.arange(len(xenon_popularity))
ax.bar(r, xenon_popularity, color='b', edgecolor='grey')
ax.bar(r, zephyr_popularity, color='g', edgecolor='grey', bottom=xenon_popularity)
ax.bar(r, orbis_popularity, color='m', edgecolor='grey', bottom=np.array(xenon_popularity) + np.array(zephyr_popularity))

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()