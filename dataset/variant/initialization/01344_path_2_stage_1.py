import matplotlib.pyplot as plt
import numpy as np

# Technologies and symmetrical adoption data
technologies = [
    'IoT', 'AI-Driven\nPublic Services', 'Autonomous\nVehicles',
    'Smart Grids', 'Blockchain\nGovernance', 'Renewable\nEnergy Systems',
    'Urban Analytics', 'Digital Twins', 'Cybersecurity', '5G Networks'
]

# Adoption rates for 2021, 2022, 2023
adoption_rates = {
    '2021': np.array([75, 65, 45, 60, 35, 40, 50, 30, 55, 20]),
    '2022': np.array([80, 68, 48, 63, 38, 45, 55, 35, 60, 25]),
    '2023': np.array([85, 70, 50, 65, 40, 50, 60, 40, 65, 30])
}

# Calculate declines or inverses to form a diverging view
max_value = 100
inverse_rates = {year: max_value - rates for year, rates in adoption_rates.items()}

fig, ax = plt.subplots(figsize=(14, 9))

# Plot as diverging bars from the central baseline
y_pos = np.arange(len(technologies))
for year, rates in adoption_rates.items():
    ax.barh(y_pos - 0.2 if year == '2021' else y_pos + 0.2, rates, align='center', label=f'{year} Adoption')

for year, inverse in inverse_rates.items():
    ax.barh(y_pos - 0.2 if year == '2021' else y_pos + 0.2, -inverse, align='center', label=f'{year} Non-Adoption', alpha=0.5)

# Center the axis at zero with symmetrical limits
ax.set_xlim(-max_value, max_value)

# Labels and titles
ax.set_yticks(y_pos)
ax.set_yticklabels(technologies)
ax.set_xlabel('Adoption Rate Divergence (%)', fontsize=12)
ax.set_title('Diverging Adoption of Emerging Technologies (2021-2023)', fontsize=16, fontweight='bold', pad=20)

# Grid and legend
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper right', fontsize=10, title='Year')

plt.tight_layout()
plt.show()