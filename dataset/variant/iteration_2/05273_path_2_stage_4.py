import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2051)
ev_adoption_rates = np.array([5, 7, 10, 15, 22, 30, 40, 50, 62, 75, 90])
co2_reduction = np.array([2, 3, 5, 9, 14, 20, 28, 35, 47, 60, 75])
renewable_energy_share = np.array([18, 20, 22, 25, 29, 35, 42, 50, 58, 65, 75])
battery_efficiency_improvement = np.array([2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57])

fig, ax1 = plt.subplots(figsize=(14, 8))

# EV Adoption Rates
ax1.plot(years, ev_adoption_rates, 'o-', linewidth=2, color='red')
ax1.set_xlabel('Time (Years)', fontsize=12)
ax1.set_ylabel('Electric Vehicle Uptake (%)', fontsize=12, color='red')
ax1.tick_params(axis='y', labelcolor='red')
for i, rate in enumerate(ev_adoption_rates):
    ax1.annotate(f'{rate}% EVs', (years[i], ev_adoption_rates[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color='red')

ax2 = ax1.twinx()
# CO2 Reduction
ax2.plot(years, co2_reduction, 's--', linewidth=2, color='blue')
ax2.set_ylabel('Decrease in CO2 (Million Tons)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
for i, reduction in enumerate(co2_reduction):
    ax2.annotate(f'{reduction} Mt CO2', (years[i], co2_reduction[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=10, color='blue')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
# Renewable Energy Share
ax3.plot(years, renewable_energy_share, 'd-.', linewidth=2, color='green')
ax3.set_ylabel('Share of Renewables (%)', fontsize=12, color='green')
ax3.tick_params(axis='y', labelcolor='green')
for i, share in enumerate(renewable_energy_share):
    ax3.annotate(f'{share}% Renew', (years[i], renewable_energy_share[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color='green')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
# Battery Efficiency Improvement
ax4.plot(years, battery_efficiency_improvement, 'x--', linewidth=2, color='purple')
ax4.set_ylabel('Battery Upgrades (%)', fontsize=12, color='purple')
ax4.tick_params(axis='y', labelcolor='purple')
for i, efficiency in enumerate(battery_efficiency_improvement):
    ax4.annotate(f'{efficiency}% Btr.Eff', (years[i], battery_efficiency_improvement[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color='purple')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

fig.tight_layout()
plt.show()