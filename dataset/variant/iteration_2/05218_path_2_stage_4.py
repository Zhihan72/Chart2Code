import matplotlib.pyplot as plt
import numpy as np

models = ['Ex-X1', 'T-Z10', 'V-A2', 'P-3G', 'Au-F5']
fuel_2020 = [1450, 1200, 1400, 1500, 1300]
fuel_2021 = [1400, 1250, 1300, 1350, 1400]
fuel_2022 = [1350, 1250, 1350, 1400, 1200]

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_height = 0.25
y = np.arange(len(models))

ax1.barh(y - bar_height, fuel_2020, bar_height, color='skyblue')
ax1.barh(y, fuel_2021, bar_height, color='lightgreen')
ax1.barh(y + bar_height, fuel_2022, bar_height, color='salmon')

ax1.set_title('Fuel Eff. by Model (2020-2022)', fontsize=16, fontweight='bold')
ax1.set_ylabel('Model', fontsize=12)
ax1.set_xlabel('Fuel Cons. (kg/mission)', fontsize=12)
ax1.set_yticks(y)
ax1.set_yticklabels(models, fontsize=11)
ax1.set_xlim(1000, 1600)

plt.tight_layout()
plt.show()