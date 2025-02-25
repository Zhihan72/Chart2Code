import matplotlib.pyplot as plt
import numpy as np

spacecraft_models = ['Expl-X1', 'Pion-3G', 'Voy-A2', 'Tita-Z10', 'Auro-F5']
fuel_efficiency_2020 = [1400, 1300, 1350, 1500, 1450]
fuel_efficiency_2021 = [1350, 1250, 1300, 1450, 1400]

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_width = 0.25
y = np.arange(len(spacecraft_models))

bars1 = ax1.barh(y - bar_width/2, fuel_efficiency_2020, bar_width, color='orange')
bars2 = ax1.barh(y + bar_width/2, fuel_efficiency_2021, bar_width, color='purple')

ax1.set_title('Fuel Efficiency by Model\n(2020-2021)', fontsize=16, fontweight='bold')
ax1.set_ylabel('Model', fontsize=12)
ax1.set_xlabel('Avg. Fuel (kg/mission)', fontsize=12)
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

plt.tight_layout()
plt.show()