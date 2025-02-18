import matplotlib.pyplot as plt
import numpy as np

xenon_popularity = [70, 90, 55, 85, 65]
zephyr_popularity = [65, 78, 60, 80, 70]
orbis_popularity = [80, 92, 68, 85, 72]

central_value = np.mean([xenon_popularity, zephyr_popularity, orbis_popularity], axis=0)
xenon_deviation = np.array(xenon_popularity) - central_value
zephyr_deviation = np.array(zephyr_popularity) - central_value
orbis_deviation = np.array(orbis_popularity) - central_value

bar_width = 0.5
r = np.arange(len(xenon_popularity))

fig, ax = plt.subplots(figsize=(12, 7))
ax.barh(r, xenon_deviation, color='m', height=bar_width)
ax.barh(r, zephyr_deviation, left=xenon_deviation, color='b', alpha=0.7)
ax.barh(r, orbis_deviation, left=xenon_deviation + zephyr_deviation, color='c')

ax.xaxis.grid(True, linestyle='-.', which='major', color='purple', alpha=0.5)

plt.tight_layout()
plt.show()