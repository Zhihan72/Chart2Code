import matplotlib.pyplot as plt
import numpy as np

spacecraft_models = ['Explorer-X1', 'Pioneer-3G', 'Voyager-A2', 'Titan-Z10', 'Aurora-F5']
fuel_efficiency_2020 = [1400, 1300, 1350, 1500, 1450]
fuel_efficiency_2021 = [1350, 1250, 1300, 1450, 1400]
fuel_efficiency_2022 = [1300, 1200, 1250, 1400, 1350]

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_width = 0.25
y = np.arange(len(spacecraft_models))

bars1 = ax1.barh(y - bar_width, fuel_efficiency_2020, bar_width, label='2020', color='skyblue')
bars2 = ax1.barh(y, fuel_efficiency_2021, bar_width, label='2021', color='lightgreen')
bars3 = ax1.barh(y + bar_width, fuel_efficiency_2022, bar_width, label='2022', color='salmon')

ax1.set_title('Space Exploration Institute: Annual Fuel Efficiency by Spacecraft Model\n(2020-2022)', fontsize=16, fontweight='bold')
ax1.set_ylabel('Spacecraft Model', fontsize=12)
ax1.set_xlabel('Average Fuel Consumption (kg/mission)', fontsize=12)
ax1.set_yticks(y)
ax1.set_yticklabels(spacecraft_models, fontsize=11)
ax1.set_xlim(1000, 1600)

def add_labels(bars, orientation='horizontal'):
    for bar in bars:
        xval = bar.get_width() if orientation == 'horizontal' else bar.get_height()
        yval = bar.get_y() + bar.get_height()/2.0 if orientation == 'horizontal' else bar.get_x() + bar.get_width()/2.0
        ax1.text(xval + 20, yval, f'{xval}', va='center', fontsize=10, color='black')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

ax1.legend(loc='lower right', fontsize=10)

ax1.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()