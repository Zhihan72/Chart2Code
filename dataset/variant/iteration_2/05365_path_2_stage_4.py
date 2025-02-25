import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

# Randomly altered content within data groups, manually shuffled
electric_cars = [50, 130, 95, 70, 180, 310, 240, 390, 570, 480, 680]
electric_bikes = [35, 50, 20, 95, 70, 160, 210, 120, 270, 420, 340]
electric_buses = [15, 25, 10, 50, 35, 95, 70, 125, 200, 160, 250]
electric_scooters = [25, 40, 15, 75, 55, 130, 100, 165, 250, 205, 300]
electric_trucks = [8, 12, 5, 25, 18, 50, 35, 70, 125, 95, 155]

electric_vehicles = np.array([electric_cars, electric_bikes, electric_buses,
                              electric_scooters, electric_trucks])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, electric_vehicles, labels=['Cars', 'Bikes', 'Buses',
             'Scooters', 'Trucks'], colors=['crimson', 'teal', 'forestgreen',
             'orange', 'darkslateblue'], alpha=0.7)

ax.set_title("EV Growth (2020-30)", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Yr", fontsize=13)
ax.set_ylabel("EVs (thousands)", fontsize=13)

ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), title='Types')

ax.grid(axis='x', color='gray', linestyle='--', lw=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()