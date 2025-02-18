import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Egyptian Empire', 'Roman Empire', 'Greek City-States', 'Persian Empire', 'Chinese Han Dynasty', 'Indus Valley Civilization']
influence = np.array([85, 95, 70, 90, 88, 65])
population = np.array([10, 56, 5, 40, 60, 4])

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(civilizations))

ax.barh(y_pos, influence, color='skyblue', edgecolor='w', linewidth=0.5, height=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)

for i, pop in enumerate(population):
    ax.text(influence[i], i, f'{pop}M', va='center', ha='right', color='black', fontsize=10)

ax.set_xlabel('Influence (0-100)', fontsize=12)
ax.set_title('Influence of Ancient Civilizations', fontsize=14)
plt.tight_layout()
plt.show()