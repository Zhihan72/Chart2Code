import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)

# Manually altered consumption values
neo_tokyo_consumption = np.array([330, 320, 300, 310, 300, 280, 290, 260, 275, 245, 255])
metropolis_consumption = np.array([340, 350, 330, 325, 320, 315, 310, 290, 270, 255, 265])
omega_city_consumption = np.array([295, 290, 275, 285, 270, 260, 260, 255, 240, 235, 225])

events = {
    "Neo-Tokyo": [(2052, 'New Plant'), (2056, 'Saving Campaign')],
    "Metropolis": [(2055, 'Recycling Upgrade')],
    "Omega City": [(2053, 'Reservoir Accident')]
}

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, neo_tokyo_consumption, marker='D', linestyle='--', color='cyan', linewidth=1.5, markersize=6, label='NT')
ax.plot(years, metropolis_consumption, marker='x', linestyle='-.', color='purple', linewidth=1.5, markersize=6, label='MT')
ax.plot(years, omega_city_consumption, marker='p', linestyle=':', color='orange', linewidth=1.5, markersize=6, label='OC')

for city, events_list in events.items():
    for year, event in events_list:
        idx = year - 2050
        if city == "Neo-Tokyo":
            xytext = (-60, 25)
            xy = (year, neo_tokyo_consumption[idx])
        elif city == "Metropolis":
            xytext = (-60, -40)
            xy = (year, metropolis_consumption[idx])
        else:
            xytext = (60, 25)
            xy = (year, omega_city_consumption[idx])

        ax.annotate(event, xy=xy, xytext=xytext, textcoords='offset points', 
                    arrowprops=dict(arrowstyle='-|>', color='gray'), fontsize=9, backgroundcolor='lightyellow')

ax.set_title('Water Use in Futurist Cities (2050-60)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Usage (M Gallons)', fontsize=14)

ax.legend(loc='lower left', fontsize=10, frameon=False)

ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()