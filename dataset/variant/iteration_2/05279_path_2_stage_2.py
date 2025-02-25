import matplotlib.pyplot as plt
import numpy as np

# Randomly altered order and values
cities = ['Chicago', 'Los Angeles', 'New York', 'Houston', 'Phoenix', 'San Diego', 'Philadelphia', 'San Antonio', 'San Jose', 'Dallas']
pizzas_sold = [190, 180, 240, 140, 160, 130, 170, 150, 165, 190]

# Randomly altered values
types = ['Cheese', 'Pepperoni', 'Veggie', 'BBQ Chicken', 'Hawaiian']
type_data = {
    'New York': [70, 50, 45, 35, 35]
}

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))

# Use the same color for both sets of data
bars1 = ax1.barh(cities, pizzas_sold, color='dodgerblue', edgecolor='black')
bars2 = ax2.bar(types, type_data['New York'], color='dodgerblue', edgecolor='black')

ax1.set_title('Monthly Pizza Sales Across Major US Cities', fontsize=18, fontweight='bold')
ax1.set_xlabel('Number of Pizzas Sold', fontsize=14, labelpad=10)
ax1.set_ylabel('Cities', fontsize=14, labelpad=10)

ax2.set_title('Pizza Type Sales in New York City', fontsize=18, fontweight='bold')
ax2.set_xlabel('Pizza Type', fontsize=14, labelpad=10)
ax2.set_ylabel('Number of Pizzas Sold', fontsize=14, labelpad=10)

ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=12, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout(pad=3.0)
plt.show()