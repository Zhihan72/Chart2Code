import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2051)
ev_adoption_rates = np.array([5, 7, 10, 15, 22, 30, 40, 50, 62, 75, 90])
co2_reduction = np.array([2, 3, 5, 9, 14, 20, 28, 35, 47, 60, 75])
renewable_energy_share = np.array([18, 20, 22, 25, 29, 35, 42, 50, 58, 65, 75])
charging_stations_growth = np.array([10, 15, 22, 30, 40, 55, 70, 85, 100, 120, 150])

fig, ax1 = plt.subplots(figsize=(14, 8))

primary_color = 'blue'
secondary_color = 'darkorange'

ax1.plot(years, ev_adoption_rates, 'v--', linewidth=2, color=primary_color, label='Electric Vehicles (%)')
ax1.set_xlabel('Timeline (Years)', fontsize=12)
ax1.set_ylabel('EV Popularity (%)', fontsize=12, color=primary_color)
ax1.tick_params(axis='y', labelcolor=primary_color)

for i, rate in enumerate(ev_adoption_rates):
    ax1.annotate(f'{rate}%', (years[i], ev_adoption_rates[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color=primary_color)

ax2 = ax1.twinx()
ax2.plot(years, co2_reduction, '^:', linewidth=2, color=secondary_color, label='Carbon Reduction (Tons)')
ax2.set_ylabel('CO2 Saved (Million Tons)', fontsize=12, color=secondary_color)
ax2.tick_params(axis='y', labelcolor=secondary_color)

for i, reduction in enumerate(co2_reduction):
    ax2.annotate(f'{reduction} MT', (years[i], co2_reduction[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=10, color=secondary_color)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, renewable_energy_share, 'h-', linewidth=2, color=primary_color, label='Green Energy (%)')
ax3.set_ylabel('Renewable Sources (%)', fontsize=12, color=primary_color)
ax3.tick_params(axis='y', labelcolor=primary_color)

for i, share in enumerate(renewable_energy_share):
    ax3.annotate(f'{share}%', (years[i], renewable_energy_share[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color=primary_color)

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.plot(years, charging_stations_growth, 'p-.', linewidth=2, color=secondary_color, label='Charging Stations Growth (%)')
ax4.set_ylabel('Charging Stations (%)', fontsize=12, color=secondary_color)
ax4.tick_params(axis='y', labelcolor=secondary_color)

for i, growth in enumerate(charging_stations_growth):
    ax4.annotate(f'{growth}%', (years[i], charging_stations_growth[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color=secondary_color)

plt.title('Trends in Eco-Friendly Transportation & Energy\nAcross Future Decades', fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle=':', alpha=0.7)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=12)
ax1.spines['top'].set_visible(False)
fig.tight_layout()
plt.show()