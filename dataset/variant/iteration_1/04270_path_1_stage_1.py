import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2021)

car_commuters = np.array([50, 55, 58, 60, 62, 65, 66, 68, 70, 73, 75, 74, 73, 73, 74, 75])
public_transport_commuters = np.array([30, 32, 35, 37, 41, 45, 48, 52, 55, 57, 60, 63, 65, 68, 71, 74])
cycling_commuters = np.array([2, 3, 4, 5, 7, 9, 11, 14, 17, 19, 22, 25, 28, 30, 32, 35])
walking_commuters = np.array([10, 11, 12, 13, 14, 15, 15, 15, 15, 15, 14, 13, 12, 12, 12, 12])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(years, car_commuters, public_transport_commuters, cycling_commuters, walking_commuters,
             labels=['Automobiles', 'Transit', 'Bikes', 'On Foot'],
             colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

ax.set_title('Modes of Transport in Urbania (2005-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Count of Commuters (thousands)', fontsize=14)
ax.set_xticks(years[::1])
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.set_yticks(np.arange(0, 160, 10))
ax.set_yticklabels(np.arange(0, 160, 10), fontsize=10)

ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Transport Method', fontsize=10)

plt.tight_layout()
plt.show()