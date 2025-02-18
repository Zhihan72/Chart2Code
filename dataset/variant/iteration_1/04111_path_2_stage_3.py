import matplotlib.pyplot as plt
import numpy as np

cities = ['NY', 'LDN', 'TKYO', 'PAR', 'SYD']
cuisines = ['Ital.', 'Chin.', 'Ind.', 'Mex.', 'Frn.']

data = np.array([
    [75, 60, 50, 120, 90],
    [70, 80, 110, 100, 95],
    [110, 90, 95, 85, 60],
    [100, 70, 90, 85, 65],
    [60, 95, 80, 75, 55]
])

bar_width = 0.15

r1 = np.arange(len(cities))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

fig, ax = plt.subplots(figsize=(12, 8))

bar1 = ax.bar(r1, data[:, 0], color='blue', width=bar_width, edgecolor='grey', label=cuisines[0])
bar2 = ax.bar(r2, data[:, 1], color='purple', width=bar_width, edgecolor='grey', label=cuisines[1])
bar3 = ax.bar(r3, data[:, 2], color='orange', width=bar_width, edgecolor='grey', label=cuisines[2])
bar4 = ax.bar(r4, data[:, 3], color='red', width=bar_width, edgecolor='grey', label=cuisines[3])
bar5 = ax.bar(r5, data[:, 4], color='green', width=bar_width, edgecolor='grey', label=cuisines[4])

ax.set_xlabel('City', fontweight='bold', fontsize=12)
ax.set_ylabel('Restaurant Count', fontweight='bold', fontsize=12)
ax.set_title('Gastro Fest 2023\nCuisine Distribution', fontweight='bold', fontsize=14, pad=20)

ax.set_xticks([r + 2 * bar_width for r in range(len(cities))])
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

ax.legend(title='Cuisines', loc='upper right', fontsize=10, edgecolor='grey')

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height - 5, f'{int(height)}', ha='center', va='bottom', color='white', fontweight='bold')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)
add_labels(bar5)

plt.tight_layout()

plt.show()