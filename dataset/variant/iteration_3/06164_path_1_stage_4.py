import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Oranges', 'Strawbs', 'Grapes', 'Mangoes', 'Bluebs']
consumption_data = [50, 30, 40, 20, 10, 25, 15]
calories_data = [2000, 1500, 1600, 500, 300, 700, 250]

fig, ax1 = plt.subplots(figsize=(14, 8))

y_pos = np.arange(len(fruits))
bar_height = 0.4

bars1 = ax1.barh(y_pos, consumption_data, height=bar_height, color='#5F9EA0', edgecolor='black', linestyle='--', label='Servings', alpha=0.85)

ax2 = ax1.twiny()
bars2 = ax2.barh(y_pos + bar_height, calories_data, height=bar_height, color='#FFD700', edgecolor='brown', linestyle=':', label='Calories', alpha=0.85)

for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 0.5, bar.get_y() + bar.get_height()/2, int(width), va='center', ha='left', fontsize=10, color='darkcyan')

for bar in bars2:
    width = bar.get_width()
    ax2.text(width + 50, bar.get_y() + bar.get_height()/2, int(width), va='center', ha='left', fontsize=10, color='darkgoldenrod')

plt.title('Fruit Consumption & Calories\nSurvey 2023', fontsize=16, fontweight='bold', color='darkgreen')
ax1.set_ylabel('Fruits', fontsize=12)
ax1.set_xlabel('Avg Servings', fontsize=12, color='darkcyan')
ax2.set_xlabel('Cal', fontsize=12, color='darkgoldenrod')

ax1.set_yticks(y_pos + bar_height / 2)
ax1.set_yticklabels(fruits, fontsize=12, rotation=0, ha='right')

bars = [bars1[0], bars2[0]]
legends = [bars1.get_label(), bars2.get_label()]
ax1.legend(bars, legends, loc='lower right')

ax1.xaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.6)

plt.tight_layout()
plt.show()