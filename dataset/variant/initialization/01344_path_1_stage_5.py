import matplotlib.pyplot as plt
import numpy as np

technologies = [
    'AI', 'Twins', 'IoT', '5G', 'Renewable', 
    'Self-Drive', 'Blockchain', 'Grids', 'Analytics', 'Security'
]

adoption_rates_2023 = np.array([70, 40, 85, 30, 50, 50, 40, 65, 60, 65])
non_adoption_rates_2023 = 100 - adoption_rates_2023
error = np.array([2, 2, 3, 4, 3, 4, 5, 3, 2, 3])

colors = ['#ff7f0e', '#7f7f7f', '#1f77b4', '#17becf', '#8c564b', 
          '#2ca02c', '#9467bd', '#d62728', '#e377c2', '#bcbd22']

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