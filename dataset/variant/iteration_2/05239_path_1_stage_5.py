import matplotlib.pyplot as plt
import numpy as np

countries = ['Brewland', 'Latteville', 'Espressonia', 'Mocha Town', 'Cappuccinia']
coffee_consumption = [7, 11, 5, 8, 10]
economic_impact = [3.1, 6.0, 2.1, 4.5, 5.2]

y_pos = np.arange(len(countries))
height = 0.35

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Global Coffee Mania: Consumption vs Economy', fontsize=18, fontweight='bold', y=0.98)

# Economic Impact horizontal bar chart
bars2 = ax2.barh(y_pos + height/2, economic_impact, height, color='#8B4513', edgecolor='black', linewidth=1.2, label='Economic Influence (B USD)')
for bar in bars2:
    xval = bar.get_width()
    ax2.text(xval + 0.1, bar.get_y() + bar.get_height()/2, f'{xval} billion', va='center', ha='left', fontsize=10)

ax2.set_title('Coffee Market Economic Influence', fontsize=14, fontweight='bold', pad=10)
ax2.set_ylabel('Nations', fontsize=12)
ax2.set_xlabel('Influence (Billion USD)', fontsize=12)
ax2.set_yticks(y_pos)
ax2.set_yticklabels(countries, fontsize=11)
ax2.set_xlim(0, 7)
ax2.grid(axis='x', linestyle='--', alpha=0.7)
ax2.legend(loc='upper right', fontsize=10)

# Coffee Consumption horizontal bar chart
bars1 = ax1.barh(y_pos - height/2, coffee_consumption, height, color='#D2691E', edgecolor='black', linewidth=1.2, label='Beans (kg/person)')
for bar in bars1:
    xval = bar.get_width()
    ax1.text(xval + 0.2, bar.get_y() + bar.get_height()/2, f'{xval} kg', va='center', ha='left', fontsize=10)

ax1.set_title('Yearly Brewed Delight Intake', fontsize=14, fontweight='bold', pad=10)
ax1.set_ylabel('Nations', fontsize=12)
ax1.set_xlabel('Beans Consumed (kg/person)', fontsize=12)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(countries, fontsize=11)
ax1.set_xlim(0, 12)
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.legend(loc='upper right', fontsize=10)

plt.tight_layout(pad=2.0, rect=[0, 0.03, 1, 0.95])
plt.show()