import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2036)

# Data for different modes of transportation (in million passenger-kilometers)
public_transport = np.array([85, 87, 90, 95, 100, 105, 110, 120, 130, 140, 150, 160, 170, 180, 195, 210])
electric_vehicles = np.array([5, 8, 12, 18, 30, 40, 55, 75, 95, 120, 150, 180, 210, 240, 270, 300])
pedestrians = np.array([15, 15, 16, 18, 20, 23, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70])
traditional_cars = np.array([70, 68, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0])

plt.figure(figsize=(14, 8))

plt.stackplot(years, public_transport, electric_vehicles, pedestrians, traditional_cars,
              labels=['Public Transit', 'Green Autos', 'Walkers', 'Old School Rides'],
              colors=['#e6194b','#3cb44b','#ffe119','#4363d8'], alpha=0.8)

# Randomized title and labels
plt.title("Urban Commute Evolution\n(2020-2035)", fontsize=16, fontweight='bold')
plt.xlabel("Timeline", fontsize=14)
plt.ylabel("Travel Distance (Millions)", fontsize=14)

plt.xticks(years, rotation=45)

plt.tight_layout()

plt.legend(loc='upper left')
plt.show()