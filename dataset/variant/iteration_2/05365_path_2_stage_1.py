import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

electric_cars = [50, 70, 95, 130, 180, 240, 310, 390, 480, 570, 680]
electric_bikes = [20, 35, 50, 70, 95, 120, 160, 210, 270, 340, 420]
electric_buses = [10, 15, 25, 35, 50, 70, 95, 125, 160, 200, 250]
electric_scooters = [15, 25, 40, 55, 75, 100, 130, 165, 205, 250, 300]
electric_trucks = [5, 8, 12, 18, 25, 35, 50, 70, 95, 125, 155]

electric_vehicles = np.array([electric_cars, electric_bikes, electric_buses,
                              electric_scooters, electric_trucks])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, electric_vehicles, labels=['Cars', 'Bikes', 'Buses',
             'Scooters', 'Trucks'], colors=['darkslateblue', 'forestgreen',
             'orange', 'crimson', 'teal'], alpha=0.7)

ax.set_title("Electric Vehicle Growth Over Years\n(2020-2030)", fontsize=16,
             fontweight='bold', pad=15)

ax.set_xlabel("Year", fontsize=13)
ax.set_ylabel("Electric Vehicles (in thousands)", fontsize=13)

ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), title='Types')

ax.grid(axis='x', color='gray', linestyle='--', lw=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()