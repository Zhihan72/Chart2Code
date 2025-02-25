import matplotlib.pyplot as plt
import numpy as np

seasons = ["Blossom", "Heatwave", "Fallen Leaves", "Chill"]
drone_racing = [60, 70, 50, 80]  # Altered order
robot_wrestling = [50, 40, 65, 60]  # Altered order
ai_chess = [35, 50, 30, 45]  # Altered order

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
x = np.arange(len(seasons))
br1 = x
br2 = [i + bar_width for i in br1]
br3 = [i + bar_width for i in br2]

single_color = 'purple'
ax.bar(br1, drone_racing, color=single_color, width=bar_width, edgecolor='grey')
ax.bar(br2, robot_wrestling, color=single_color, width=bar_width, edgecolor='grey')
ax.bar(br3, ai_chess, color=single_color, width=bar_width, edgecolor='grey')

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

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()