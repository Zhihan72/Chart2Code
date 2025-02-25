import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

# Reduced data, original order
electric_cars = [95, 70, 50, 130, 180, 310, 240, 390, 480, 680, 570]
electric_bikes = [50, 20, 35, 95, 120, 70, 160, 210, 340, 270, 420]
electric_buses = [25, 15, 10, 35, 50, 95, 70, 125, 160, 250, 200]
electric_scooters = [40, 15, 100, 55, 75, 130, 25, 165, 205, 300, 250]
electric_trucks = [12, 5, 8, 18, 25, 50, 35, 70, 95, 155, 125]

electric_vehicles = np.array([electric_cars, electric_bikes, electric_buses, electric_scooters, electric_trucks])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, electric_vehicles, labels=['Cars', 'Bikes', 'Buses', 'Scoots', 'Trucks'], 
             colors=['lightcoral', 'lightseagreen', 'dodgerblue', 'limegreen', 'gold'], alpha=0.8)

ax.set_title("Electric Transport Growth (2020-2030)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Yr", fontsize=14)
ax.set_ylabel("Vehicles (k)", fontsize=14)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Types')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()