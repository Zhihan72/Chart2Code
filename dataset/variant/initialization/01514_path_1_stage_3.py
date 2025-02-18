import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

electric_cars = np.array([1900, 2400, 500, 3700, 700, 900, 1500, 5400, 4500, 1200, 3000])
hybrid_cars = np.array([2100, 4000, 2500, 5500, 1700, 3400, 2900, 4700, 1300, 6500, 1000])
bicycles = np.array([5900, 3400, 4300, 3000, 5000, 4600, 4000, 6400, 5200, 5400, 3200])
scooters = np.array([1800, 200, 300, 1300, 400, 3900, 600, 2400, 250, 3100, 900])

total_vehicles = electric_cars + hybrid_cars + bicycles + scooters
total_vehicle_market = np.linspace(20000, 80000, len(years))
percentage_eco_friendly = (total_vehicles / total_vehicle_market) * 100

transport_data = np.vstack([electric_cars, hybrid_cars, bicycles, scooters])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.stackplot(years, transport_data, colors=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3'], alpha=0.8)
ax2 = ax1.twinx()
ax2.plot(years, percentage_eco_friendly, color='black', linewidth=2, linestyle='--', marker='o')

ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Registered Vehicles', fontsize=14)
ax2.set_ylabel('Percentage of Eco-Friendly Vehicles (%)', fontsize=14)

ax1.set_title("Eco-Friendly Transportation Adoption in Greenfield (2010-2020)", fontsize=18, fontweight='bold')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()