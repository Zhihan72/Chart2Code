import matplotlib.pyplot as plt
import numpy as np

years = np.array(list(range(2013, 2023)))

superaqua_activities = np.array([135, 200, 142, 120, 175, 160, 150, 170, 130, 185])
pyroman_activities = np.array([110, 165, 105, 140, 125, 130, 120, 155, 100, 115])
earthguardian_activities = np.array([85, 145, 110, 130, 135, 120, 80, 100, 95, 90])
windwoman_activities = np.array([100, 120, 92, 105, 115, 97, 130, 110, 90, 95])

plt.figure(figsize=(12, 6))

plt.plot(years, superaqua_activities, marker='o', linestyle='-', color='red', linewidth=2)
plt.plot(years, pyroman_activities, marker='s', linestyle='--', color='green', linewidth=2)
plt.plot(years, earthguardian_activities, marker='^', linestyle='-.', color='purple', linewidth=2)
plt.plot(years, windwoman_activities, marker='x', linestyle=':', color='blue', linewidth=2)

for (x, y) in zip(years, superaqua_activities):
    plt.text(x, y + 2, f'{y}', color='red', fontsize=8, ha='center')

for (x, y) in zip(years, pyroman_activities):
    plt.text(x, y + 2, f'{y}', color='green', fontsize=8, ha='center')

for (x, y) in zip(years, earthguardian_activities):
    plt.text(x, y + 2, f'{y}', color='purple', fontsize=8, ha='center')

for (x, y) in zip(years, windwoman_activities):
    plt.text(x, y + 2, f'{y}', color='blue', fontsize=8, ha='center')

plt.title('Evolution of Superhero Activity Levels\n(2013-2022)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Incidents Handled', fontsize=12)

plt.xticks(years, rotation=45)
plt.yticks(range(0, 251, 25))

plt.tight_layout()
plt.show()