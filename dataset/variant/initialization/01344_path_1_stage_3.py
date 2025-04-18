import matplotlib.pyplot as plt
import numpy as np

technologies = [
    'IoT', 'AI-Driven\nPublic Services', 'Autonomous\nVehicles',
    'Smart Grids', 'Blockchain\nGovernance', 'Renewable\nEnergy Systems',
    'Urban Analytics', 'Digital Twins', 'Cybersecurity', '5G Networks'
]

adoption_rates_2023 = np.array([85, 70, 50, 65, 40, 50, 60, 40, 65, 30])
non_adoption_rates_2023 = 100 - adoption_rates_2023
error = np.array([3, 2, 4, 3, 5, 3, 2, 2, 3, 4])

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

colors = colors[::-1]

fig, ax = plt.subplots(figsize=(14, 9))

adopt_bars = ax.barh(technologies, adoption_rates_2023 - 50, xerr=error, color=colors, capsize=5)

non_adopt_bars = ax.barh(technologies, -(non_adoption_rates_2023 - 50), color='#c7c7c7')

for i, adopt in enumerate(adoption_rates_2023):
    adopt_label_position = (adopt - 50) + (np.sign((adopt - 50)) * 5)
    ax.text(adopt_label_position, i, f'{adopt}%', ha='center', va='center', color='white' if adopt > 50 else 'black', fontsize=10, weight='bold')

ax.set_xlim(-50, 50)
ax.xaxis.set_tick_params(width=0)
ax.yaxis.set_tick_params(rotation=0)

plt.tight_layout()
plt.show()