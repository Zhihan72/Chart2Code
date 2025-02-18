import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2021)

car_commuters = np.array([50, 54, 59, 61, 61, 64, 67, 66, 71, 73, 74, 75, 72, 73, 75, 76])
public_transport_commuters = np.array([31, 33, 34, 36, 42, 44, 47, 50, 56, 58, 61, 62, 66, 67, 70, 73])
cycling_commuters = np.array([3, 2, 5, 4, 6, 10, 12, 15, 16, 20, 21, 26, 27, 31, 31, 34])
walking_commuters = np.array([9, 12, 11, 14, 13, 14, 16, 14, 14, 16, 15, 12, 11, 13, 12, 11])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(years, car_commuters, public_transport_commuters, cycling_commuters, walking_commuters,
             colors=['#66b3ff'], alpha=0.8)

ax.set_title('Modes of Transport in Urbania (2005-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Count of Commuters (thousands)', fontsize=14)
ax.set_xticks(years[::1])
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.set_yticks(np.arange(0, 160, 10))
ax.set_yticklabels(np.arange(0, 160, 10), fontsize=10)

plt.tight_layout()
plt.show()