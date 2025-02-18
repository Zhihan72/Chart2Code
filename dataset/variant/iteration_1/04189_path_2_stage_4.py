import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']

ai_assistants = [120, 150, 130, 100, 60, 30]
smart_homes = [80, 140, 120, 110, 70, 40]
electric_vehicles = [50, 100, 110, 90, 50, 20]

fig, ax = plt.subplots(figsize=(12, 8))

height = 0.25

bar1 = np.arange(len(age_groups))
bar2 = [y + height for y in bar1]
bar3 = [y + height for y in bar2]

ax.barh(bar1, ai_assistants, height, label='AI', color='skyblue', linestyle='-', edgecolor='black')
ax.barh(bar2, smart_homes, height, label='Homes', color='lightgreen', linestyle=':', edgecolor='black')
ax.barh(bar3, electric_vehicles, height, label='EVs', color='lightcoral', linestyle='--', edgecolor='black')

ax.set_ylabel('Ages', fontsize=12, weight='bold')
ax.set_xlabel('# Adopters', fontsize=12, weight='bold')
ax.set_title('Tech Adoption by Age, 2023', fontsize=14, weight='bold', pad=20)

ax.set_yticks([r + height for r in range(len(age_groups))])
ax.set_yticklabels(age_groups, fontsize=12)

def add_value_labels(y_positions, values):
    for y_pos, value in zip(y_positions, values):
        ax.text(value + 3, y_pos, str(value), va='center', color='black', fontsize=10)

add_value_labels(bar1, ai_assistants)
add_value_labels(bar2, smart_homes)
add_value_labels(bar3, electric_vehicles)

ax.legend(title='Techs', loc='lower left', fontsize=9)

ax.xaxis.grid(True, linestyle='-.', alpha=0.8)

plt.tight_layout()
plt.show()