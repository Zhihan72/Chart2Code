import numpy as np
import matplotlib.pyplot as plt

categories = ['Temp', 'Humi', 'Visib', 'Air', 'Traffic']
bike = [8, 5, 7, 6, 8]
car = [9, 4, 8, 5, 9]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
bike += bike[:1]
car += car[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill the area for Bike and Car datasets with different colors
ax.fill(angles, bike, color='cyan', alpha=0.3, label='Bike')
ax.fill(angles, car, color='orange', alpha=0.3, label='Car')

# Plot lines for each dataset with varied marker styles
ax.plot(angles, bike, color='cyan', linewidth=1.5, linestyle='--', marker='o')
ax.plot(angles, car, color='orange', linewidth=1.5, linestyle=':', marker='s')

ax.grid(color='gray', linestyle='-.', linewidth=0.7)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, ha='center')

plt.title('Commute Analysis', size=15, y=1.1)
plt.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), frameon=False)
plt.tight_layout()
plt.show()