import numpy as np
import matplotlib.pyplot as plt

# Define the years
years = np.arange(2020, 2036)

# Data for different modes of transportation (in million passenger-kilometers)
public_transport = np.array([85, 87, 90, 95, 100, 105, 110, 120, 130, 140, 150, 160, 170, 180, 195, 210])
bicycles = np.array([10, 11, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100])
electric_vehicles = np.array([5, 8, 12, 18, 30, 40, 55, 75, 95, 120, 150, 180, 210, 240, 270, 300])
pedestrians = np.array([15, 15, 16, 18, 20, 23, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70])
traditional_cars = np.array([70, 68, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0])

# Stacked area plot
plt.figure(figsize=(14, 8))

# Plotting the area chart
plt.stackplot(years, public_transport, bicycles, electric_vehicles, pedestrians, traditional_cars,
              colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'], alpha=0.8)

# Title and labels
plt.title("Transformation of Transportation Modes in Urban DreamScape\n(2020-2035)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Passenger-Kilometers (Millions)", fontsize=14)

# Customize x-axis labels
plt.xticks(years, rotation=45)

# Adjust layout to prevent text cutoff
plt.tight_layout()

# Show the plot
plt.show()