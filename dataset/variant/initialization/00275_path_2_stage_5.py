import matplotlib.pyplot as plt
import numpy as np

xenon_popularity = [85, 65, 90, 70, 55]
orbis_popularity = [92, 72, 80, 85, 68]

fig, ax = plt.subplots(figsize=(12, 7))
r = np.arange(len(xenon_popularity))

# Changed both to have the same color 'b'
ax.bar(r, xenon_popularity, color='b')
ax.bar(r, orbis_popularity, color='b', bottom=xenon_popularity)

plt.tight_layout()
plt.show()