import matplotlib.pyplot as plt
import numpy as np

tech_labels = [
    'AI-Driven\nPublic Services', 'IoT', 'Autonomous\nVehicles',
    'Smart Grids', 'Renewable\nEnergy Systems', 'Blockchain\nGovernance',
    'Digital Twins', 'Urban Analytics', '5G Networks', 'Cybersecurity',
    'Quantum Computing', 'Edge Computing'  # New data series
]

adoption_data = {
    '2021': np.array([65, 75, 45, 60, 40, 35, 30, 50, 20, 55, 10, 15]),
    '2022': np.array([68, 80, 48, 63, 45, 38, 35, 55, 25, 60, 20, 25]),
    '2023': np.array([70, 85, 50, 65, 50, 40, 40, 60, 30, 65, 30, 35])
}

max_val = 100
inverse_data = {year: max_val - rates for year, rates in adoption_data.items()}

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['tab:purple', 'tab:orange', 'tab:green']

y_pos = np.arange(len(tech_labels))
for i, (year, rates) in enumerate(adoption_data.items()):
    ax.barh(y_pos - 0.2 if year == '2021' else y_pos + 0.2, rates, align='center', label=f'{year} Acceptance', color=colors[i])

for i, (year, inverse) in enumerate(inverse_data.items()):
    ax.barh(y_pos - 0.2 if year == '2021' else y_pos + 0.2, -inverse, align='center', label=f'{year} Rejection', alpha=0.5, color=colors[i])

ax.set_xlim(-max_val, max_val)

ax.set_yticks(y_pos)
ax.set_yticklabels(tech_labels)
ax.set_xlabel('Rate Divergence (%)', fontsize=12)
ax.set_title('Diverging Tech Adoption 2021-2023', fontsize=16, fontweight='bold', pad=20)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper right', fontsize=10, title='Years')

plt.tight_layout()
plt.show()