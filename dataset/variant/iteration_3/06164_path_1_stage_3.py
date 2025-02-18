import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Oranges', 'Strawbs', 'Grapes', 'Mangoes', 'Bluebs']
consumption_data = [50, 30, 40, 20, 10, 25, 15]
calories_data = [2000, 1500, 1600, 500, 300, 700, 250]

fig, ax1 = plt.subplots(figsize=(14, 8))
x_pos = np.arange(len(fruits))
bar_width = 0.4

bars1 = ax1.bar(x_pos, consumption_data, width=bar_width, color='#5F9EA0', edgecolor='black', linestyle='--', label='Servings', alpha=0.85)

ax2 = ax1.twinx()
bars2 = ax2.bar(x_pos + bar_width, calories_data, width=bar_width, color='#FFD700', edgecolor='brown', linestyle=':', label='Calories', alpha=0.85)

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, color='darkcyan')

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom', fontsize=10, color='darkgoldenrod')

plt.title('Fruit Consumption & Calories\nSurvey 2023', fontsize=16, fontweight='bold', color='darkgreen')
ax1.set_xlabel('Fruits', fontsize=12)
ax1.set_ylabel('Avg Servings', fontsize=12, color='darkcyan')
ax2.set_ylabel('Cal', fontsize=12, color='darkgoldenrod')

ax1.set_xticks(x_pos + bar_width / 2)
ax1.set_xticklabels(fruits, fontsize=12, rotation=45, ha='right')

bars = [bars1[0], bars2[0]]
legends = [bars1.get_label(), bars2.get_label()]
ax1.legend(bars, legends, loc='upper right')

ax1.yaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.6)

plt.tight_layout()
plt.show()