import matplotlib.pyplot as plt
import numpy as np

# Existing fruit data sets
fruits = ['Apples', 'Bananas', 'Oranges', 'Strawberries', 'Grapes']
consumption_data = [50, 30, 40, 20, 10]
calories_data = [2000, 1500, 1600, 500, 300]

# Additional made-up data series or groups
fruits.extend(['Mangoes', 'Blueberries'])
consumption_data.extend([25, 15])  # Adding consumption data for new fruits
calories_data.extend([700, 250])   # Adding calories data for new fruits

fig, ax1 = plt.subplots(figsize=(14, 8))
x_pos = np.arange(len(fruits))
bar_width = 0.4

bars1 = ax1.bar(x_pos, consumption_data, width=bar_width, color='#5F9EA0', edgecolor='black', linestyle='--', label='Consumption (Servings)', alpha=0.85)

ax2 = ax1.twinx()
bars2 = ax2.bar(x_pos + bar_width, calories_data, width=bar_width, color='#FFD700', edgecolor='brown', linestyle=':', label='Total Calories', alpha=0.85)

# Data labels for consumption
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, color='darkcyan')

# Data labels for calories
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom', fontsize=10, color='darkgoldenrod')

plt.title('Fruits Consumption and Caloric Intake\nCommunity Nutrition Survey 2023', fontsize=16, fontweight='bold', color='darkgreen')
ax1.set_xlabel('Fruits', fontsize=12)
ax1.set_ylabel('Average Consumption (Servings)', fontsize=12, color='darkcyan')
ax2.set_ylabel('Total Calories', fontsize=12, color='darkgoldenrod')

ax1.set_xticks(x_pos + bar_width / 2)
ax1.set_xticklabels(fruits, fontsize=12, rotation=45, ha='right')

# Legend adjustments
bars = [bars1[0], bars2[0]]
legends = [bars1.get_label(), bars2.get_label()]
ax1.legend(bars, legends, loc='upper right')

ax1.yaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.6)

plt.tight_layout()
plt.show()