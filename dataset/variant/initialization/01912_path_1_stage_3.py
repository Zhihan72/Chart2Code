import matplotlib.pyplot as plt

decades = ['2000s', '2010s', '2020s', '2030s', '2040s']
discoveries = [15, 30, 45, 60, 80]
missions = [10, 20, 35, 55, 75]
research = [5, 25, 40, 50, 70]  # New data series

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(decades, discoveries, marker='o', linestyle='-', color='b', linewidth=2, markersize=8, label='Discoveries')
ax.plot(decades, missions, marker='s', linestyle='--', color='g', linewidth=2, markersize=8, label='Missions')
ax.plot(decades, research, marker='^', linestyle=':', color='r', linewidth=2, markersize=8, label='Research')

ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Discoveries / Missions / Research', fontsize=12, labelpad=10)
ax.set_title('Journey to the Stars:\nAstronomical Discoveries, Missions, and Research Over the Decades', fontsize=16, pad=20)

ax.legend()  # Add a legend to the plot

plt.tight_layout()
plt.show()