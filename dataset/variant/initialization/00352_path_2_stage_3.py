import numpy as np
import matplotlib.pyplot as plt

# Islands and magical elements
islands = ['Avalon', 'Eldoria', 'Lumina', 'Noxterra', 'Vespera']
elements = ['Mana', 'Ether', 'Elixir', 'Aura']

# Percentage data
percentage_data = np.array([
    [30, 25, 20, 25],
    [20, 30, 35, 15],
    [25, 25, 30, 20],
    [15, 35, 25, 25],
    [35, 15, 20, 30]
])

# Compute total abundance for each magical element
element_totals = np.sum(percentage_data, axis=0)

# Sort the elements and their totals in descending order
sorted_indices = np.argsort(-element_totals)
sorted_elements = np.array(elements)[sorted_indices]
sorted_totals = element_totals[sorted_indices]

# Plotting sorted bar chart
plt.figure(figsize=(10, 6))

bar_colors = ['#FFA07A', '#20B2AA', '#9370DB', '#FF4500']

plt.bar(sorted_elements, sorted_totals, color=[bar_colors[i] for i in sorted_indices], alpha=0.8)

plt.xlabel('Magical Elements', fontsize=10, fontweight='bold', color='grey')
plt.ylabel('Total Abundance (%)', fontsize=10, fontweight='bold', color='grey')
plt.title('Total Magical Element Abundance in Fantasia', fontsize=16, fontweight='bold', pad=20, color='navy')

plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()