import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Egyptian Empire', 'Roman Empire', 'Greek City-States', 'Persian Empire', 'Chinese Han Dynasty', 'Indus Valley Civilization']
influence = np.array([85, 95, 70, 90, 88, 65])

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(civilizations))

ax.barh(y_pos, influence, color='blue', alpha=0.7)  # Changed color to 'blue'

ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)
ax.set_xlabel('Influence (0-100)', fontsize=12)
ax.set_title('Influence of Ancient Civilizations', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()