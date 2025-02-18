import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Han Dynasty', 'Roman Empire', 'City-States of Greece', 'Persian Fam']
influence = np.array([70, 90, 65, 85])

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(civilizations))

ax.barh(y_pos, influence, color='darkred', alpha=0.8, edgecolor='black', linestyle='--')

ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)
ax.set_xlabel('Power Level (0-100)', fontsize=12, color='green')
ax.set_title('Historical Influence Chart', fontsize=16, fontweight='bold')

for spine in ax.spines.values():
    spine.set_edgecolor('purple')
    spine.set_linewidth(1.5)

ax.grid(True, which='both', axis='x', linestyle=':', linewidth=0.5)

ax.legend(['Influence of Empires'], loc='lower right', fontsize=10, frameon=True, facecolor='lightgrey')

plt.tight_layout()
plt.show()