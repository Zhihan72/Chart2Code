import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'Los Angeles', 'Dallas', 'Chicago', 'Philadelphia', 'San Jose', 'San Diego', 'Houston', 'Phoenix', 'San Antonio']
pizzas_sold = [240, 220, 190, 180, 170, 165, 160, 150, 140, 130]

types = ['Cheese', 'Pepperoni', 'Veggie', 'BBQ Chicken', 'Hawaiian']
type_data_ny = [80, 60, 40, 30, 30]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))

# Switched order of bar plots
bars1 = ax2.barh(cities, pizzas_sold, color='royalblue', edgecolor='grey', linestyle='-.', linewidth=2)
bars2 = ax1.bar(types, type_data_ny, color='salmon', edgecolor='white', hatch='/', linewidth=2)

ax2.set_title('Monthly Pizza Sales Across Major US Cities', fontsize=18, color='darkgreen')
ax2.set_xlabel('Number of Pizzas Sold', fontsize=14, color='darkred', labelpad=10)
ax2.set_ylabel('Cities', fontsize=14, color='darkblue', labelpad=10)

ax1.set_title('Pizza Type Sales in New York City', fontsize=18, color='teal')
ax1.set_xlabel('Pizza Type', fontsize=14, color='purple', labelpad=10)
ax1.set_ylabel('Number of Pizzas Sold', fontsize=14, color='darkorange', labelpad=10)

ax2.grid(axis='x', linestyle='-.', linewidth=0.5, color='grey', alpha=0.5)
ax1.grid(axis='y', linestyle=':', linewidth=1.0, color='red', alpha=0.5)

ax2.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

for bar in bars2:
    width = bar.get_width()
    ax2.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=12, fontweight='bold', color='black')

for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', va='bottom', fontsize=12, fontweight='bold', color='red')

plt.tight_layout(pad=3.0)
plt.show()