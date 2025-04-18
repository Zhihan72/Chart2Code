import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
revenue = np.array([0.5, 2.1, 3.9, 7.0, 10.2, 13.5, 18.0, 24.0, 32.5, 45.0])
operational_costs = np.array([0.3, 1.0, 1.8, 3.5, 6.0, 7.5, 10.0, 13.0, 18.0, 25.0])  # New data series

fig, ax = plt.subplots(figsize=(12, 6))

# Plot the revenue data with a new set of colors
ax.plot(years, revenue, marker='o', linestyle='-', color='#FF6347', lw=2, markersize=8, label='Sales Figures (in millions USD)')

# Plot the operational costs data with a new set of colors
ax.plot(years, operational_costs, marker='s', linestyle='--', color='#4682B4', lw=2, markersize=8, label='Operational Costs (in millions USD)')

ax.set_title('Growth Trajectory of TechCultivation (2013-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Fiscal Year', fontsize=14)
ax.set_ylabel('Value (in millions USD)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.7)
ax.tick_params(axis='both', which='major', labelsize=12)

for i in range(len(years)):
    ax.text(years[i], revenue[i] + 1, f'{revenue[i]:.1f}', ha='center', fontsize=10, color='darkred')
    ax.text(years[i], operational_costs[i] + 1, f'{operational_costs[i]:.1f}', ha='center', fontsize=10, color='royalblue')  # New annotations

ax.legend(fontsize=12)

plt.xticks(np.arange(2013, 2023, step=1))
plt.tight_layout()

plt.show()