import matplotlib.pyplot as plt
import numpy as np

mission_types = ['Planetary', 'Observation', 'Tech Demo', 'Human Flight']
mission_budgets = [100, 150, 250, 300]
colors = ['#99ff99', '#ff9999', '#66b3ff', '#ffcc99']  # Shuffled colors

# Sort the data
sorted_indices = np.argsort(mission_budgets)[::-1]  # For descending order
sorted_types = [mission_types[i] for i in sorted_indices]
sorted_budgets = [mission_budgets[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]

fig, ax2 = plt.subplots(figsize=(8, 5))

ax2.barh(sorted_types, sorted_budgets, color=sorted_colors, edgecolor='black')
ax2.set_xlabel('Budget ($M)', fontsize=12)
ax2.set_title("Budget by Type", fontsize=14, fontweight='bold', color='navy', pad=20)

for i, budget in enumerate(sorted_budgets):
    ax2.text(budget + 5, i, f'${budget}M', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()