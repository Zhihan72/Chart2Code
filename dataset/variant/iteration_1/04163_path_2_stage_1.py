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

ax.fill(angles, bike, color='blue', alpha=0.25, label='Bike')
ax.fill(angles, bus, color='green', alpha=0.25, label='Bus')
ax.fill(angles, car, color='red', alpha=0.25, label='Car')

ax.plot(angles, bike, color='blue', linewidth=2)
ax.plot(angles, bus, color='green', linewidth=2)
ax.plot(angles, car, color='red', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

plt.title('Commuting Conditions Analysis\nAcross Different Modes of Transportation', size=15, y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.tight_layout()
plt.show()