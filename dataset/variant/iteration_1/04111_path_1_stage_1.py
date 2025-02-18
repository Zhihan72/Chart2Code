import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
cuisines = ['Italian', 'Chinese', 'Indian', 'French']

# Updated data, removing the Mexican cuisine
data = np.array([
    [120, 90, 60, 75],   # New York
    [100, 110, 95, 80],  # London
    [85, 95, 110, 90],   # Tokyo
    [90, 85, 70, 100],   # Paris
    [80, 75, 60, 95]     # Sydney
])

bar_width = 0.2

r1 = np.arange(len(cities))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

fig, ax = plt.subplots(figsize=(12, 8))

# Plot the remaining cuisine types
bar1 = ax.bar(r1, data[:, 0], color='red', width=bar_width, edgecolor='grey', label=cuisines[0])
bar2 = ax.bar(r2, data[:, 1], color='blue', width=bar_width, edgecolor='grey', label=cuisines[1])
bar3 = ax.bar(r3, data[:, 2], color='green', width=bar_width, edgecolor='grey', label=cuisines[2])
bar4 = ax.bar(r4, data[:, 3], color='purple', width=bar_width, edgecolor='grey', label=cuisines[3])

ax.set_xlabel('Cities', fontweight='bold', fontsize=12)
ax.set_ylabel('Number of Restaurants', fontweight='bold', fontsize=12)
ax.set_title('Gastronomic Festival 2023\nDistribution of Cuisines in Top Urban Areas', fontweight='bold', fontsize=14, pad=20)

ax.set_xticks([r + 1.5 * bar_width for r in range(len(cities))])
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

ax.legend(title='Cuisine Types', loc='upper right', fontsize=10, edgecolor='grey')

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height - 5, f'{int(height)}', ha='center', va='bottom', color='white', fontweight='bold')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)

plt.tight_layout()
plt.show()