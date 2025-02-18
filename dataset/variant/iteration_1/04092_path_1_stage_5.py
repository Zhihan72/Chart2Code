import matplotlib.pyplot as plt
import numpy as np

cities = ['NY', 'Tokyo', 'Berlin', 'Paris', 'Sydney', 'London', 'Cairo', 'Mumbai', 'SP', 'Beijing']
coffee_consumption = [300, 250, 220, 240, 200, 280, 220, 160, 180, 210]

# Sort the coffee consumption and associated cities in ascending order
sorted_indices = sorted(range(len(coffee_consumption)), key=lambda i: coffee_consumption[i])
sorted_cities = [cities[i] for i in sorted_indices]
sorted_coffee_consumption = [coffee_consumption[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#FF5733'
bars = ax.bar(sorted_cities, sorted_coffee_consumption, color=single_color)

for bar, consumption in zip(bars, sorted_coffee_consumption):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{consumption}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_title('Coffee Consumption by City (Sorted)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Cities', fontsize=12, labelpad=10)
ax.set_ylabel('Cups/Month', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(sorted_cities)))
ax.set_xticklabels(sorted_cities, rotation=45, ha='right', fontsize=11)

plt.tight_layout()
plt.show()