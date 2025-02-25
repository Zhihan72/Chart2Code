import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Dallas', 'Chicago', 'Philadelphia', 'San Jose', 'San Diego', 'Houston', 'Phoenix', 'San Antonio']
pizzas_sold = [240, 220, 190, 180, 170, 165, 160, 150, 140, 130]

types = ['Cheese', 'Pepperoni', 'Veggie', 'BBQ Chicken', 'Hawaiian']
type_data_ny = [80, 60, 40, 30, 30]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))

# Use the same color for both bar plots
color = 'royalblue'
bars1 = ax2.barh(cities, pizzas_sold, color=color)
bars2 = ax1.bar(types, type_data_ny, color=color)

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