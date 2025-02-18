import numpy as np
import matplotlib.pyplot as plt

categories = ['Temperature', 'Humidity', 'Visibility', 'Air Quality', 'Traffic']
bike = [8, 5, 7, 6, 8]
bus = [7, 6, 5, 7, 5]
car = [9, 4, 8, 5, 9]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
bike += bike[:1]
bus += bus[:1]
car += car[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Apply a single consistent color 'purple' for all groups
ax.fill(angles, bike, color='purple', alpha=0.25, label='Bike')
ax.fill(angles, bus, color='purple', alpha=0.25, label='Bus')
ax.fill(angles, car, color='purple', alpha=0.25, label='Car')

ax.plot(angles, bike, color='purple', linewidth=2)
ax.plot(angles, bus, color='purple', linewidth=2)
ax.plot(angles, car, color='purple', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, ha='center')

plt.title('Commuting Conditions Analysis\nAcross Different Modes of Transportation', size=15, y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.tight_layout()
plt.show()