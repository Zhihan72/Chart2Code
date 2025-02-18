import matplotlib.pyplot as plt
import numpy as np

# Only retain the data needed for the bar chart
mission_types = ['Planetary', 'Observation', 'Tech Demo', 'Human Flight']
mission_budgets = [100, 150, 250, 300]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a single subplot for the bar chart
fig, ax2 = plt.subplots(figsize=(8, 5))

# Plot the bar chart
ax2.barh(mission_types, mission_budgets, color=colors, edgecolor='black')
ax2.set_xlabel('Budget ($M)', fontsize=12)
ax2.set_title("Budget by Type", fontsize=14, fontweight='bold', color='navy', pad=20)

# Add text annotations
for i, budget in enumerate(mission_budgets):
    ax2.text(budget + 5, i, f'${budget}M', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()