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

ax.plot(decades, jazz_popularity, label='Jazz', color='red', marker='o', linestyle='-')
ax.plot(decades, rock_popularity, label='Rock', color='blue', marker='s', linestyle='--')
ax.plot(decades, disco_popularity, label='Disco', color='green', marker='^', linestyle='-.')
ax.plot(decades, hiphop_popularity, label='Hip-hop', color='orange', marker='D', linestyle=':')
ax.plot(decades, electronic_popularity, label='Electronic', color='brown', marker='x', linestyle='-.')
ax.plot(decades, pop_popularity, label='Pop', color='purple', marker='*', linestyle='-')
ax.plot(decades, folk_popularity, label='Folk', color='pink', marker='v', linestyle='--')

ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('Decades of Melody:\nMusical Genre Popularity Over Time', fontsize=16, fontweight='bold')

ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right', title='Music Genres', fontsize=10, title_fontsize='12')

plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()