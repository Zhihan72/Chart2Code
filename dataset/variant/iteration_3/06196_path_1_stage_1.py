import matplotlib.pyplot as plt
import numpy as np

categories = ['Strength', 'Agility', 'Intelligence', 'Charisma', 'Resilience']
num_vars = len(categories)
arthur = [8, 6, 7, 9, 8]
elena = [5, 9, 8, 7, 6]
morgana = [7, 8, 9, 6, 7]

average_abilities = [
    np.mean([arthur[i], elena[i], morgana[i]]) 
    for i in range(num_vars)
]

def create_radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, label=label)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.set_title("Heroes' Guild: Abilities Comparison\nAmong Legendary Adventurers", fontsize=14, fontweight='bold')
polar_ax = fig.add_subplot(121, polar=True)
create_radar_chart(polar_ax, arthur, 'g', 'Arthur the Brave')
create_radar_chart(polar_ax, elena, 'b', 'Elena the Swift')
create_radar_chart(polar_ax, morgana, 'orange', 'Morgana the Wise')

polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=12)
polar_ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Changed the order of colors here for the bar chart as well
ax2.bar(categories, average_abilities, color=['orange', 'g', 'b', 'purple', 'r'])
ax2.set_ylim(0, 10)
ax2.set_title('Average Abilities Across Categories', fontsize=14, fontweight='bold')
ax2.set_ylabel('Average Rating')
ax2.set_xlabel('Ability')
for i, score in enumerate(average_abilities):
    ax2.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

plt.tight_layout()
plt.show()