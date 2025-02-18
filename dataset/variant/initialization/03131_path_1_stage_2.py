import matplotlib.pyplot as plt
import numpy as np

metrics = ['Strength', 'Endurance', 'Flexibility', 'Balance', 'Nutrition', 'Mental Well-being']
ideal_plan = [8, 8, 8, 8, 8, 8]
current_plan = [6, 7, 5, 9, 6, 7]

num_vars = len(metrics)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

ideal_plan += ideal_plan[:1]
current_plan += current_plan[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], metrics, color='black', size=12)
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Swapped the colors for each data group
ax.plot(angles, ideal_plan, color='orange', linewidth=2, linestyle='dashed')
ax.fill(angles, ideal_plan, color='orange', alpha=0.1)

ax.plot(angles, current_plan, color='teal', linewidth=2, linestyle='solid')
ax.fill(angles, current_plan, color='teal', alpha=0.25)

plt.show()