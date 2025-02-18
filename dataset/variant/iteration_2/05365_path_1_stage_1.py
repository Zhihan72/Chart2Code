import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

electric_cars = [50, 70, 95, 130, 180, 240, 310, 390, 480, 570, 680]
electric_bikes = [20, 35, 50, 70, 95, 120, 160, 210, 270, 340, 420]
electric_buses = [10, 15, 25, 35, 50, 70, 95, 125, 160, 200, 250]
electric_scooters = [15, 25, 40, 55, 75, 100, 130, 165, 205, 250, 300]
electric_trucks = [5, 8, 12, 18, 25, 35, 50, 70, 95, 125, 155]

electric_vehicles = np.array([electric_cars, electric_bikes, electric_buses, electric_scooters, electric_trucks])

fig, ax = plt.subplots(figsize=(12, 7))

# Shuffled the colors manually
ax.stackplot(years, electric_vehicles, labels=['Cars', 'Bikes', 'Buses', 'Scooters', 'Trucks'], 
             colors=['lightcoral', 'lightseagreen', 'dodgerblue', 'limegreen', 'gold'], alpha=0.8)

ax.set_title("Rise in Different Modes of Electric Transportation Over a Decade\n(2020-2030)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Electric Vehicles (in thousands)", fontsize=14)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Vehicle Types')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()