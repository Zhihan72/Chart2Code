import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

# Provided data arrays
electric_cars = [95, 70, 50, 130, 180, 310, 240, 390, 480, 680, 570]
electric_bikes = [50, 20, 35, 95, 120, 70, 160, 210, 340, 270, 420]
electric_buses = [25, 15, 10, 35, 50, 95, 70, 125, 160, 250, 200]
electric_scooters = [40, 15, 100, 55, 75, 130, 25, 165, 205, 300, 250]
electric_trucks = [12, 5, 8, 18, 25, 50, 35, 70, 95, 155, 125]

electric_vehicles = np.array([electric_cars, electric_bikes, electric_buses, electric_scooters, electric_trucks])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, electric_vehicles, labels=['Cars', 'Bikes', 'Buses', 'Scoots', 'Trucks'], 
             colors=['salmon', 'teal', 'cornflowerblue', 'palegreen', 'khaki'], alpha=0.85)

# Modified title and label styles
ax.set_title("Growth of Electric Vehicles (2020-2030)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Years", fontsize=12, fontstyle='italic')
ax.set_ylabel("Total Number of Vehicles (in thousands)", fontsize=12, fontstyle='italic')

# Modified legend properties
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, title='Vehicle Types', title_fontsize='13')

# Added customization to grid and border
ax.grid(alpha=0.5, linestyle='--', which='both')
ax.spines['top'].set_color('none')  # Removed top border
ax.spines['right'].set_color('none')  # Removed right border

plt.tight_layout()
plt.show()