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

# Shuffled colors
ax1.stackplot(decades, stacked_data, labels=['Rock', 'Disco', 'Pop', 'Hip Hop', 'Elec', 'Indie'],
              colors=['#8c564b', '#2ca02c', '#d62728', '#ff7f0e', '#1f77b4', '#9467bd'], alpha=0.7)

ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("% Pop.", fontsize=14)
ax1.set_title("Music Genres & Streaming (1970-2020s)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(decades)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax1.annotate('Hip Hop Rise', xy=(2000, 20), xytext=(1980, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

ax2 = ax1.twinx()
ax2.plot(decades, streaming_services, label='Streaming', color='black', linestyle='--', marker='o')
ax2.set_ylabel("% Users", fontsize=14)

ax1.legend(loc='upper left', fontsize=12, title='Genres', bbox_to_anchor=(0, 1))
ax2.legend(loc='upper left', fontsize=12, bbox_to_anchor=(0.8, 1))

plt.tight_layout()
plt.show()