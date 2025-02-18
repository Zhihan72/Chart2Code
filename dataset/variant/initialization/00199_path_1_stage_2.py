import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(1970, 2030, 10)

rock = [40, 35, 25, 15, 10, 5]
disco = [20, 25, 10, 5, 0, 0]
pop = [10, 15, 25, 30, 35, 40]
hip_hop = [0, 0, 10, 20, 25, 30]
electronic = [5, 10, 15, 20, 20, 15]
indie = [0, 0, 5, 10, 10, 10]

stacked_data = np.vstack([rock, disco, pop, hip_hop, electronic, indie])

streaming_services = [0, 0, 5, 20, 50, 70]

fig, ax1 = plt.subplots(figsize=(14, 8))

altered_colors = ['#bbf7d0', '#fbcfe8', '#fef3c7', '#c7d2fe', '#fca5a5', '#a5f3fc']
ax1.stackplot(decades, stacked_data, labels=['Rock', 'Disco', 'Pop', 'Hip Hop', 'Electronic', 'Indie'],
              colors=altered_colors, alpha=0.6)

ax1.set_xlabel("Decade", fontsize=14)
ax1.set_ylabel("Popularity (%)", fontsize=14)
ax1.set_title("Shifting Melodies: Music Genre Popularity and the Rise of Streaming\nfrom the 1970s to 2020s", 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(decades)
ax1.grid(axis='x', linestyle='-', alpha=0.8)

ax1.annotate('Rise of Hip Hop', xy=(2000, 20), xytext=(1990, 30),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=12)

ax2 = ax1.twinx()
ax2.plot(decades, streaming_services, label='Streaming Services', color='navy', linestyle='-', marker='s')
ax2.set_ylabel("Streaming Users (%)", fontsize=14)

ax1.legend(loc='upper right', fontsize=12, title='Music Genres')
ax2.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()