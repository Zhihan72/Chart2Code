import matplotlib.pyplot as plt
import numpy as np

# Data representing spacecraft models and average fuel consumptions (in kg per mission)
spacecraft_models = ['Explorer-X1', 'Titan-Z10', 'Voyager-A2', 'Pioneer-3G', 'Aurora-F5']
fuel_efficiency_2020 = [1450, 1200, 1400, 1500, 1300]
fuel_efficiency_2021 = [1400, 1250, 1300, 1350, 1400]
fuel_efficiency_2022 = [1350, 1250, 1350, 1400, 1200]

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_height = 0.25
y = np.arange(len(spacecraft_models))

bars1 = ax1.barh(y - bar_height, fuel_efficiency_2020, bar_height, label='2020', color='skyblue')
bars2 = ax1.barh(y, fuel_efficiency_2021, bar_height, label='2021', color='lightgreen')
bars3 = ax1.barh(y + bar_height, fuel_efficiency_2022, bar_height, label='2022', color='salmon')

ax1.set_title('Space Exploration Institute: Annual Fuel Efficiency by Spacecraft Model\n(2020-2022)', fontsize=16, fontweight='bold')
ax1.set_ylabel('Spacecraft Model', fontsize=12)
ax1.set_xlabel('Average Fuel Consumption (kg/mission)', fontsize=12)
ax1.set_yticks(y)
ax1.set_yticklabels(spacecraft_models, fontsize=11)
ax1.set_xlim(1000, 1600)

def add_labels(bars):
    for bar in bars:
        xpos = bar.get_width()
        ax1.text(xpos + 20, bar.get_y() + bar.get_height()/2.0, f'{xpos}', ha='left', va='center', fontsize=10, color='black')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

ax1.legend(loc='upper right', fontsize=10)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()