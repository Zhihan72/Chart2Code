import matplotlib.pyplot as plt
import numpy as np

categories = ['Strength', 'Agility', 'Intelligence', 'Charisma', 'Resilience']
num_vars = len(categories)
arthur = [8, 6, 7, 9, 8]
elena = [5, 9, 8, 7, 6]

average_abilities = [
    np.mean([arthur[i], elena[i]]) 
    for i in range(num_vars)
]

def create_radar_chart(ax, data, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.5)
    ax.plot(angles, data, color=color, linewidth=2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.bar(categories, average_abilities, color=['g', 'b', 'g', 'b', 'g'])
ax1.set_ylim(0, 10)
ax1.set_ylabel('Average Rating')
ax1.set_xlabel('Ability')
for i, score in enumerate(average_abilities):
    ax1.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

polar_ax = fig.add_subplot(122, polar=True)
create_radar_chart(polar_ax, arthur, 'g')
create_radar_chart(polar_ax, elena, 'b')

polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=12)

plt.tight_layout()
plt.show()