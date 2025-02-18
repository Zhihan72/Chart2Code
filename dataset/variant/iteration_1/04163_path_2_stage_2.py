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

# Changing colors, alpha and line styles for different modes of transportation
ax.fill(angles, bike, color='cyan', alpha=0.3, label='Bike')
ax.fill(angles, bus, color='yellow', alpha=0.3, label='Bus')
ax.fill(angles, car, color='magenta', alpha=0.3, label='Car')

ax.plot(angles, bike, linestyle='--', color='cyan', linewidth=1.5, marker='o')
ax.plot(angles, bus, linestyle='-.', color='yellow', linewidth=1.5, marker='x')
ax.plot(angles, car, linestyle=':', color='magenta', linewidth=1.5, marker='s')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Changing legend location and some grid settings
plt.title('Commuting Conditions Analysis\nAcross Different Modes of Transportation', size=15, y=1.05)
plt.legend(loc='upper left', bbox_to_anchor=(0.9, 0.9))

# Add custom grid
ax.grid(color='gray', linestyle='dashed')

plt.tight_layout()
plt.show()