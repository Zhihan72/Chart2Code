import matplotlib.pyplot as plt

appliances = [
    'Refrigerator', 
    'Washing Machine', 
    'Dryer', 
    'Dishwasher', 
    'Oven', 
    'Microwave', 
    'Lighting', 
    'Television'
]
energy_consumption = [500, 275, 400, 300, 450, 100, 475, 250]  # kWh per year
cost_saving = [75, 45, 60, 55, 70, 30, 80, 35]  # USD per year

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF4500', '#40E0D0', '#8A2BE2']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

bars1 = ax1.barh(appliances, energy_consumption, color=colors, edgecolor='gray', linestyle='--')

for bar, consumption in zip(bars1, energy_consumption):
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{consumption} kWh', va='center', ha='left', fontsize=12, color='darkblue')

ax1.set_title('Annual Energy Consumption by Home Appliances', fontsize=16, fontweight='bold')
ax1.set_xlabel('Energy Consumption (kWh/year)', fontsize=14)
ax1.set_ylabel('Appliances', fontsize=14)
ax1.xaxis.grid(True, linestyle=':', linewidth=1)
ax1.yaxis.grid(True, linestyle=':', linewidth=1)

bars2 = ax2.barh(appliances, cost_saving, color=colors, edgecolor='gray', hatch='//')

for bar, saving in zip(bars2, cost_saving):
    ax2.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'${saving}', va='center', ha='left', fontsize=12, color='darkblue')

ax2.set_title('Expected Annual Cost-Saving from Energy-Efficient Upgrades', fontsize=16, fontweight='bold')
ax2.set_xlabel('Cost-Saving (USD/year)', fontsize=14)

ax1.legend(['Energy Consumption'], loc='upper right')
ax2.legend(['Cost-Saving'], loc='upper right')

plt.tight_layout()
plt.show()