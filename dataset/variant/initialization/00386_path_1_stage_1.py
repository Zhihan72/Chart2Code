import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1950, 2030, 10)
jazz_popularity = [70, 65, 55, 50, 40, 30, 25, 20]
rock_popularity = [20, 60, 80, 75, 60, 50, 45, 40]
disco_popularity = [0, 10, 45, 70, 30, 10, 5, 0]
hiphop_popularity = [0, 0, 10, 30, 65, 80, 90, 85]
electronic_popularity = [5, 10, 15, 20, 30, 50, 60, 70]

fig, ax = plt.subplots(figsize=(12, 7))

# Line & Marker alterations
ax.plot(decades, jazz_popularity, label='Jazz', color='steelblue', marker='p', linewidth=1, linestyle='--')
ax.plot(decades, rock_popularity, label='Rock', color='forestgreen', marker='h', linewidth=1.5, linestyle='-')
ax.plot(decades, disco_popularity, label='Disco', color='chocolate', marker='*', linewidth=1, linestyle='-')
ax.plot(decades, hiphop_popularity, label='Hip-hop', color='darkred', marker='v', linewidth=1.5, linestyle='-.')
ax.plot(decades, electronic_popularity, label='Electronic', color='indigo', marker='+', linewidth=2, linestyle=':')

# Labels and title
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('Decades of Melody:\nMusical Genre Popularity Over Time', fontsize=16, fontweight='bold')

# Grid and legend alterations
ax.grid(True, linestyle='-', alpha=0.1)
ax.legend(loc='lower center', title='Music Genres', fontsize=10, title_fontsize='12')

plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()