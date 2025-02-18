import matplotlib.pyplot as plt
import numpy as np

years = np.array(list(range(2013, 2023)))
superaqua_activities = np.array([120, 130, 135, 142, 150, 160, 170, 175, 185, 200])
pyroman_activities = np.array([100, 105, 110, 115, 120, 125, 130, 140, 155, 165])
windwoman_activities = np.array([90, 92, 95, 97, 100, 105, 110, 115, 120, 130])

plt.figure(figsize=(12, 6))
plt.plot(years, superaqua_activities, marker='^', linestyle='-.', color='blue', linewidth=2.5, label='AquaHero')
plt.plot(years, pyroman_activities, marker='v', linestyle='-', color='green', linewidth=1.5, label='FireGuy')
plt.plot(years, windwoman_activities, marker='d', linestyle='--', color='magenta', linewidth=3, label='WindyWoman')

for (x, y) in zip(years, superaqua_activities):
    plt.text(x, y + 2, f'{y}', color='blue', fontsize=10, ha='center')

for (x, y) in zip(years, pyroman_activities):
    plt.text(x, y + 2, f'{y}', color='green', fontsize=10, ha='center')

for (x, y) in zip(years, windwoman_activities):
    plt.text(x, y + 2, f'{y}', color='magenta', fontsize=10, ha='center')

plt.title('Activity Levels of Heroes Over Years\n(2013-2022)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Timeline (Years)', fontsize=12)
plt.ylabel('Incidents Tackled', fontsize=12)

plt.xticks(years, rotation=45)
plt.yticks(range(0, 251, 25))

plt.legend(title='Hero Names', fontsize=10, loc='lower right', borderaxespad=0.5, frameon=False)

plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.5)
    spine.set_color('gray')

plt.tight_layout()
plt.show()