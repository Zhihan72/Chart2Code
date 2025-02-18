import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define metrics
metrics = ['Flexibility', 'Nutrition', 'Strength', 'Balance', 'Endurance', 'Mental Well-being']

# Example data
ideal_plan = [8, 8, 8, 8, 8, 8]
current_plan = [6, 7, 5, 9, 6, 7]

num_vars = len(metrics)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

ideal_plan += ideal_plan[:1]
current_plan += current_plan[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], metrics, color='grey', size=12)

ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["10", "4", "2", "6", "8"], color="grey", size=10)  # Randomly rearranged
plt.ylim(0, 10)

ax.plot(angles, ideal_plan, color='teal', linewidth=2, linestyle='dashed', label='Perfect Program')
ax.fill(angles, ideal_plan, color='teal', alpha=0.1)

ax.plot(angles, current_plan, color='orange', linewidth=2, linestyle='solid', label='Existing Schedule')
ax.fill(angles, current_plan, color='orange', alpha=0.25)

plt.title("Wellness Parameters: Assess Balanced Health", size=16, color='black', weight='bold', pad=20)

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.05))

plt.tight_layout()

plt.show()