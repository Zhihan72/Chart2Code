import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Paris', 'New York', 'Tokyo', 'London']
cuisines = ['Italian', 'Chinese', 'Indian', 'French']

data = np.array([
    [80, 75, 60, 95],
    [90, 85, 70, 100],
    [120, 90, 60, 75],
    [85, 95, 110, 90],
    [100, 110, 95, 80]
])

sums = data.sum(axis=1)
sorted_indices = np.argsort(sums)

cities = [cities[i] for i in sorted_indices]
data = data[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
r = np.arange(len(cities))

# Manually shuffled the assignment of colors to cuisines
colors = ['purple', 'orange', 'cyan', 'green']  # Changed the color order

for i, cuisine in enumerate(cuisines):
    ax.bar(r + i * bar_width, data[:, i], width=bar_width, color=colors[i], edgecolor='grey', label=cuisine)

ax.set_xlabel('Cities', fontweight='bold', fontsize=12)
ax.set_ylabel('Number of Restaurants', fontweight='bold', fontsize=12)
ax.set_title('Gastronomic Festival 2023\nDistribution of Cuisines in Top Urban Areas', fontweight='bold', fontsize=14, pad=20)

ax.set_xticks(r + 1.5 * bar_width)
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

ax.legend(title='Cuisine Types', loc='upper right', fontsize=10, edgecolor='grey')

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height - 5, f'{int(height)}', ha='center', va='bottom', color='white', fontweight='bold')
        
bars = [ax.bar(r + i * bar_width, data[:, i], width=bar_width, color=colors[i], edgecolor='grey') for i in range(len(cuisines))]
for bar in bars:
    add_labels(bar)

plt.tight_layout()
plt.show()