import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Greek City-States', 'Chinese Han Dynasty', 'Persian Empire', 'Roman Empire', 'Indus Valley Civilization', 'Egyptian Empire']
influence = np.array([70, 88, 90, 95, 65, 85])

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(civilizations))

ax.barh(y_pos, influence, color='darkred', alpha=0.8, edgecolor='black', linestyle='--')

ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)
ax.set_xlabel('Influence (0-100)', fontsize=12, color='green')
ax.set_title('Influence of Ancient Civilizations', fontsize=16, fontweight='bold')

# Altering marker type for bar ends
for spine in ax.spines.values():
    spine.set_edgecolor('purple')
    spine.set_linewidth(1.5)

# Toggle grid
ax.grid(True, which='both', axis='x', linestyle=':', linewidth=0.5)

# Randomly chosen marker style for the legend
ax.legend(['Civilization Influence'], loc='lower right', fontsize=10, frameon=True, facecolor='lightgrey')

plt.tight_layout()
plt.show()