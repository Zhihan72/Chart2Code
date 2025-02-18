import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)

neo_tokyo_consumption = np.array([320, 330, 305, 295, 310, 290, 280, 275, 265, 250, 240])
metropolis_consumption = np.array([345, 340, 335, 320, 315, 310, 300, 285, 270, 260, 255])
omega_city_consumption = np.array([290, 295, 285, 280, 275, 265, 255, 250, 245, 230, 220])

events = {
    "Neo-Tokyo": [(2052, 'New Water Treatment Plant Operational'), (2056, 'Water-Saving Campaign Launched')],
    "Metropolis": [(2055, 'Water Recycling System Upgrade')],
    "Omega City": [(2053, 'Lake Reservoir Accident')]
}

fig, ax = plt.subplots(figsize=(14, 8))

# Colors have been shuffled
ax.plot(years, neo_tokyo_consumption, marker='D', linestyle='--', color='cyan', linewidth=1.5, markersize=6, label='Neo-Tokyo')
ax.plot(years, metropolis_consumption, marker='x', linestyle='-.', color='purple', linewidth=1.5, markersize=6, label='Metropolis')
ax.plot(years, omega_city_consumption, marker='p', linestyle=':', color='orange', linewidth=1.5, markersize=6, label='Omega City')

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

ax.set_title('Water Consumption Trends in Futuristic Cities (2050-2060)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Water Consumption (Million Gallons)', fontsize=14)

ax.legend(loc='lower left', fontsize=10, frameon=False)

ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()