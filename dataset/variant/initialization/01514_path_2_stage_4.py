import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
electric_cars = np.array([520, 680, 910, 1180, 1470, 1950, 2340, 3050, 3650, 4600, 5300])
hybrid_cars = np.array([980, 1320, 1600, 2250, 2450, 3000, 3300, 4100, 4600, 5600, 6700])
bicycles = np.array([2900, 3250, 3500, 3600, 4050, 4250, 4650, 4950, 5350, 5800, 6500])
scooters = np.array([190, 240, 310, 410, 580, 920, 1250, 1850, 2450, 3000, 3800])

total_vehicles = electric_cars + hybrid_cars + bicycles + scooters
total_vehicle_market = np.linspace(20000, 80000, len(years))
percentage_eco_friendly = (total_vehicles / total_vehicle_market) * 100

transport_data = np.vstack([electric_cars, hybrid_cars, bicycles, scooters])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.stackplot(years, transport_data, labels=['Electric Cars', 'Hybrid Vehicles', 'Bicycles', 'Scooters'], 
              colors=['#9b59b6', '#2ecc71', '#f1c40f', '#e74c3c'], alpha=0.7)

ax2 = ax1.twinx()
ax2.plot(years, percentage_eco_friendly, color='purple', linewidth=3, linestyle='-', marker='s', label='Eco-Friendly %')

ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Vehicles', fontsize=14)
ax2.set_ylabel('Eco-Friendly %', fontsize=14)

ax1.set_title("Eco Transport Growth (2010-2020)", fontsize=18, fontweight='bold')

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

ax1.grid(False)  # Removing the grid

stacked_legend = ax1.legend(loc='upper right', bbox_to_anchor=(0.85, 0.5), title='Transport Modes')
line_legend = ax2.legend(loc='upper right', bbox_to_anchor=(0.85, 0.6), title='Percentage')

ax1.add_artist(stacked_legend)

ax1.annotate('Scooter Peak', xy=(2018, scooters[-1]), xytext=(2015, 17000),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()