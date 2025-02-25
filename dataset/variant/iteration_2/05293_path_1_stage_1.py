import matplotlib.pyplot as plt
import numpy as np

# Define weeks from weeks 1 to 52
weeks = np.arange(1, 53)

# Visitor counts for Spring Park and Ocean Park
spring_park_visitors = [
    5, 6, 6.5, 7, 6.8, 9, 10, 11, 12, 10.5, 11, 13, 14, 15, 16.5,
    17, 18, 18.5, 17, 16, 16.5, 15.5, 14, 13.5, 13, 12.5, 10, 9.5,
    8, 7.5, 7, 6.5, 6, 6.2, 6.8, 7.2, 7.8, 9, 9.5, 10, 10.5, 11,
    11.5, 12, 12.3, 11.7, 11, 10.2, 9.8, 9.5, 9, 9
]

ocean_park_visitors = [
    8, 7.5, 7.8, 8.5, 8.8, 9.2, 10.1, 10.7, 10.5, 11, 11.5, 13, 13.5,
    14.2, 15, 17, 16.5, 16, 15.5, 15, 14.2, 13, 12, 11.5, 11, 10.8,
    10, 9.8, 9.2, 8.8, 8.5, 8.2, 8, 7.5, 7.2, 7, 7.5, 8, 8.5, 9,
    9.5, 10, 10.8, 11, 11.5, 11.8, 11.2, 10.7, 10.5, 10, 9.7, 9.5
]

fig, ax = plt.subplots(figsize=(14, 8))

# Altered markers, line styles, and colors
ax.plot(weeks, spring_park_visitors, marker='^', color='orange', linestyle='-', label='Spring Park', linewidth=2)
ax.plot(weeks, ocean_park_visitors, marker='x', color='purple', linestyle='-.', label='Ocean Park', linewidth=2)

# Titles and labels
ax.set_title('Public Park Weekly Visitor Trends: Spring vs Ocean Park', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Weeks', fontsize=14)
ax.set_ylabel('Visitors (thousands)', fontsize=14)

# Annotation with altered points and colors
for i in range(0, len(weeks), 6):
    ax.annotate(f'{spring_park_visitors[i]}k', (weeks[i], spring_park_visitors[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9, color='orange')
    ax.annotate(f'{ocean_park_visitors[i]}k', (weeks[i], ocean_park_visitors[i]), textcoords="offset points", xytext=(10,-15), ha='center', fontsize=9, color='purple')

# x and y ticks
ax.set_xticks(np.arange(0, 53, 4))
ax.set_xticklabels(np.arange(0, 53, 4), rotation=45)
ax.set_yticks(np.arange(0, 20, 2))
ax.set_yticklabels([f'{i}K' for i in range(0, 20, 2)])

# Grid with random style
ax.grid(True, linestyle='-.', alpha=0.7)

# Legend with a different location and size
ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()

plt.show()