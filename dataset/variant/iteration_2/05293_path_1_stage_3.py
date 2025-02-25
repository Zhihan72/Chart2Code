import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

spring_park_visitors = [
    5, 10, 6.5, 9, 6.8, 6, 11, 11, 12, 10.5, 6.5, 13, 7, 15, 16.5,
    14, 10.2, 18.5, 17, 16, 16.5, 15.5, 12, 13.5, 13, 18, 10, 9.5,
    8, 17, 7, 11, 18, 12.5, 6.8, 7.2, 7.8, 13, 9.5, 10, 14, 11,
    9, 12, 12.3, 11.7, 11, 7.2, 9.8, 9.5, 7.8, 9
]

ocean_park_visitors = [
    8, 9, 7.8, 8.5, 8.8, 7.5, 13, 10.7, 10.5, 11, 11.5, 8, 8.2,
    14.2, 7, 17, 16.5, 16, 15, 15, 14.2, 10, 12, 11.5, 11, 10.8,
    10, 15.5, 16, 8.8, 8.5, 8.2, 7.2, 9, 9.2, 13.5, 16, 13, 8.5, 9,
    9.5, 10, 10.8, 11, 11.5, 11.8, 11.2, 7, 10.7, 10.5, 10, 9
]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(weeks, spring_park_visitors, marker='^', color='orange', linestyle='-', label='Spring', linewidth=2)
ax.plot(weeks, ocean_park_visitors, marker='x', color='purple', linestyle='-.', label='Ocean', linewidth=2)

ax.set_title('Weekly Visitors: Spring & Ocean', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Week #', fontsize=14)
ax.set_ylabel('Visitors (K)', fontsize=14)

for i in range(0, len(weeks), 6):
    ax.annotate(f'{spring_park_visitors[i]}k', (weeks[i], spring_park_visitors[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9, color='orange')
    ax.annotate(f'{ocean_park_visitors[i]}k', (weeks[i], ocean_park_visitors[i]), textcoords="offset points", xytext=(10,-15), ha='center', fontsize=9, color='purple')

ax.set_xticks(np.arange(0, 53, 4))
ax.set_xticklabels(np.arange(0, 53, 4), rotation=45)
ax.set_yticks(np.arange(0, 20, 2))
ax.set_yticklabels([f'{i}K' for i in range(0, 20, 2)])

ax.grid(True, linestyle='-.', alpha=0.7)

ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()