import matplotlib.pyplot as plt
import numpy as np

# Data: Ticket Sales in Thousands
seasons = ["Blossom", "Heatwave", "Fallen Leaves", "Chill"]
drone_racing = [50, 80, 60, 70]
robot_wrestling = [40, 60, 50, 65]
ai_chess = [30, 45, 35, 50]

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
x = np.arange(len(seasons))
br1 = x
br2 = [i + bar_width for i in br1]
br3 = [i + bar_width for i in br2]

ax.bar(br1, drone_racing, color='orange', width=bar_width, edgecolor='grey', label='Futuristic Flight')
ax.bar(br2, robot_wrestling, color='blue', width=bar_width, edgecolor='grey', label='Automaton Brawl')
ax.bar(br3, ai_chess, color='green', width=bar_width, edgecolor='grey', label='Machine Minds')

ax.set_title('Nebula Sports Spectacle (Year 2125)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timelapses', fontsize=12)
ax.set_ylabel('Fans (Thousands)', fontsize=12)
ax.set_xticks([r + bar_width for r in range(len(seasons))])
ax.set_xticklabels(seasons)

for bar, ticket_sales in zip(ax.patches, drone_racing + robot_wrestling + ai_chess):
    height = bar.get_height()
    ax.annotate(f'{ticket_sales}k',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, color='black')

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=11, title='Entertainment Sectors')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()