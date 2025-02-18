import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Han Dynasty', 'Greek City-States', 'Roman Empire', 'Egyptian Empire', 'Persian Empire', 'Indus Valley', 'Mayan Civilization', 'Incan Empire']
influence = np.array([70, 95, 85, 65, 90, 88, 75, 80]) 
population = np.array([60, 5, 56, 10, 4, 40, 6, 9]) 

fig, ax = plt.subplots(figsize=(10, 8))
y_pos = np.arange(len(civilizations))

colors = ['teal', 'orange', 'purple', 'green', 'red', 'yellow', 'blue', 'brown']

ax.barh(y_pos, influence, color=colors, edgecolor='w', linewidth=0.5, height=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)

for i, pop in enumerate(population):
    ax.text(influence[i], i, f'{pop}M', va='center', ha='right', color='black', fontsize=10)

ax.set_xlabel('Cultural Impact Score', fontsize=12)
ax.set_title('Legacy of Great Civilizations', fontsize=14)
plt.tight_layout()
plt.show()