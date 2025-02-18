import matplotlib.pyplot as plt
import numpy as np

seasons = ["Burning", "Leap", "Harvest", "Shiverfreeze"]
drone_racing = [60, 50, 70, 80]
robot_wrestling = [50, 40, 65, 60]
ai_chess = [35, 30, 50, 45]
vr_gaming = [65, 70, 80, 75]

labels = np.array([seasons, drone_racing, robot_wrestling, ai_chess, vr_gaming])
sorted_indices = np.argsort([-x for x in drone_racing])
sorted_labels = labels[:, sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.15
x = np.arange(len(seasons))
br1 = x
br2 = [i + bar_width for i in br1]
br3 = [i + bar_width for i in br2]
br4 = [i + bar_width for i in br3]

# Changed colors as directed
ax.bar(br1, sorted_labels[1].astype(int), color='darkred', width=bar_width, linestyle='dashed', edgecolor='black', label='Drone Dash', hatch='/')
ax.bar(br2, sorted_labels[2].astype(int), color='navy', width=bar_width, linestyle='dotted', edgecolor='black', label='Robotics Rumble', hatch='\\')
ax.bar(br3, sorted_labels[3].astype(int), color='forestgreen', width=bar_width, linestyle='dashdot', edgecolor='black', label='A.I. Challenge', hatch='o')
ax.bar(br4, sorted_labels[4].astype(int), color='orchid', width=bar_width, linestyle='solid', edgecolor='black', label='Virtual Reality Quest', hatch='*')

ax.set_title('TechnoSport Ticket Craze in FutureCity', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Climate Cycles', fontsize=11)
ax.set_ylabel('Tickets Sold (1k Units)', fontsize=11)
ax.set_xticks([r + 1.5 * bar_width for r in range(len(seasons))])
ax.set_xticklabels(sorted_labels[0])

for bar, ticket_sales in zip(ax.patches, sorted_labels[1:].flatten().astype(int)):
    height = bar.get_height()
    ax.annotate(f'{ticket_sales}k',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8, color='black')

ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=10, title='Competitions')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()