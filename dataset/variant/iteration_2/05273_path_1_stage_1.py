import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2051)
ev_adoption_rates = np.array([5, 7, 10, 15, 22, 30, 40, 50, 62, 75, 90])
co2_reduction = np.array([2, 3, 5, 9, 14, 20, 28, 35, 47, 60, 75])
renewable_energy_share = np.array([18, 20, 22, 25, 29, 35, 42, 50, 58, 65, 75])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Set a single color for all plot elements
single_color = 'purple'

ax1.plot(years, ev_adoption_rates, 'o-', linewidth=2, color=single_color, label='EV Adoption (%)')
ax1.set_xlabel('Years', fontsize=12)
ax1.set_ylabel('EV Adoption (%)', fontsize=12, color=single_color)
ax1.tick_params(axis='y', labelcolor=single_color)

for i, rate in enumerate(ev_adoption_rates):
    ax1.annotate(f'{rate}%', (years[i], ev_adoption_rates[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color=single_color)

ax2 = ax1.twinx()
ax2.plot(years, co2_reduction, 's--', linewidth=2, color=single_color, label='CO2 Reduction (Million Tons)')
ax2.set_ylabel('CO2 Reduction (Million Tons)', fontsize=12, color=single_color)
ax2.tick_params(axis='y', labelcolor=single_color)

for i, reduction in enumerate(co2_reduction):
    ax2.annotate(f'{reduction} MT', (years[i], co2_reduction[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=10, color=single_color)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, renewable_energy_share, 'd-.', linewidth=2, color=single_color, label='Renewable Energy Share (%)')
ax3.set_ylabel('Renewable Energy Share (%)', fontsize=12, color=single_color)
ax3.tick_params(axis='y', labelcolor=single_color)

for i, share in enumerate(renewable_energy_share):
    ax3.annotate(f'{share}%', (years[i], renewable_energy_share[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color=single_color)

plt.title('Global Transition to Sustainable Transport & Energy\n(2040 - 2050)', fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.6)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=12)
fig.tight_layout()
plt.show()