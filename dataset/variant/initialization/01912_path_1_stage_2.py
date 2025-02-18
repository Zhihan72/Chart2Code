import matplotlib.pyplot as plt

decades = ['2000s', '2010s', '2020s', '2030s', '2040s']
discoveries = [15, 30, 45, 60, 80]
missions = [10, 20, 35, 55, 75]

fig, ax = plt.subplots(figsize=(14, 8))

# Changed both plots to use the same color 'b'
ax.plot(decades, discoveries, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
ax.plot(decades, missions, marker='s', linestyle='--', color='b', linewidth=2, markersize=8)

ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Discoveries / Missions', fontsize=12, labelpad=10)
ax.set_title('Journey to the Stars:\nAstronomical Discoveries and Missions Over the Decades', fontsize=16, pad=20)

plt.tight_layout()
plt.show()