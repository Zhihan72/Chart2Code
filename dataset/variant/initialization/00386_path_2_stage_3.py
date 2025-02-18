import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1950, 2030, 10)

jazz_popularity = [70, 65, 55, 50, 40, 30, 25, 20]
rock_popularity = [20, 60, 80, 75, 60, 50, 45, 40]
disco_popularity = [0, 10, 45, 70, 30, 10, 5, 0]
hiphop_popularity = [0, 0, 10, 30, 65, 80, 90, 85]
electronic_popularity = [5, 10, 15, 20, 30, 50, 60, 70]
pop_popularity = [50, 55, 65, 70, 80, 85, 90, 95]
folk_popularity = [40, 45, 50, 55, 50, 45, 40, 35]

fig, ax = plt.subplots(figsize=(12, 7))

# Randomly altered stylistic elements
ax.plot(decades, jazz_popularity, label='Jazz', color='brown', marker='x', linestyle='-.')
ax.plot(decades, rock_popularity, label='Rock', color='purple', marker='*', linestyle=':')
ax.plot(decades, disco_popularity, label='Disco', color='red', marker='^', linestyle='--')
ax.plot(decades, hiphop_popularity, label='Hip-hop', color='pink', marker='v', linestyle='-')
ax.plot(decades, electronic_popularity, label='Electronic', color='blue', marker='s', linestyle='-')
ax.plot(decades, pop_popularity, label='Pop', color='orange', marker='D', linestyle='-.')
ax.plot(decades, folk_popularity, label='Folk', color='green', marker='o', linestyle=':')

ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('Decades of Melody:\nMusical Genre Popularity Over Time', fontsize=16, fontweight='bold')

# Changed grid to a different style
ax.grid(True, linestyle=':', alpha=0.7)

# Changed legend to a different location and style
ax.legend(loc='upper left', title='Music Genres', fontsize=8, title_fontsize='10')

plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()