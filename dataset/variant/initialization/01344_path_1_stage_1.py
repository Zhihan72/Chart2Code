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

fig, ax = plt.subplots(figsize=(14, 9))

# Plot adoption rates diverging positively from the central axis
adopt_bars = ax.barh(technologies, adoption_rates_2023 - 50, xerr=error, color='#1f77b4', label='Adoption (2023)', capsize=5)

# Plot non-adoption rates diverging negatively from the central axis
non_adopt_bars = ax.barh(technologies, -(non_adoption_rates_2023 - 50), color='#c7c7c7', label='Non-Adoption (2023)')

for i, (adopt, non_adopt) in enumerate(zip(adoption_rates_2023, non_adoption_rates_2023)):
    adopt_label_position = (adopt - 50) + (np.sign((adopt - 50)) * 5)
    ax.text(adopt_label_position, i, f'{adopt}%', ha='center', va='center', color='white' if adopt > 50 else 'black', fontsize=10, weight='bold')

ax.set_title('Adoption of Emerging Technologies in Smart Cities (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Divergence from 50%', fontsize=12)
ax.set_xlim(-50, 50)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.set_tick_params(rotation=0)
ax.legend(loc='lower right', fontsize=10, title='Adoption Status')

plt.tight_layout()
plt.show()