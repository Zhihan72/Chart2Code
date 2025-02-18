import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Artificial data for electric vehicles (in thousands) per year
# Each array represents numbers from 2020 to 2030
electric_cars = [50, 70, 95, 130, 180, 240, 310, 390, 480, 570, 680]
electric_bikes = [20, 35, 50, 70, 95, 120, 160, 210, 270, 340, 420]
electric_buses = [10, 15, 25, 35, 50, 70, 95, 125, 160, 200, 250]
electric_scooters = [15, 25, 40, 55, 75, 100, 130, 165, 205, 250, 300]
electric_trucks = [5, 8, 12, 18, 25, 35, 50, 70, 95, 125, 155]

# Combine the datasets into a single 2D array for the stackplot function
electric_vehicles = np.array([electric_cars, electric_bikes, electric_buses, electric_scooters, electric_trucks])

# Create a new figure and axis with a specific size
fig, ax = plt.subplots(figsize=(12, 7))

# Use the stackplot function to create the stacked area chart
ax.stackplot(years, electric_vehicles, labels=['Cars', 'Bikes', 'Buses', 'Scooters', 'Trucks'], 
             colors=['dodgerblue', 'limegreen', 'gold', 'lightcoral', 'lightseagreen'], alpha=0.8)

# Set chart title with line break for clarity
ax.set_title("Rise in Different Modes of Electric Transportation Over a Decade\n(2020-2030)", fontsize=16, fontweight='bold', pad=20)

# Label the x and y axes
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Electric Vehicles (in thousands)", fontsize=14)

# Add a legend and place it outside the plot to avoid overlapping data
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Vehicle Types')

# Add grid lines for better readability of the plot
ax.grid(alpha=0.3)

# Adjust layout to avoid clipping of text
plt.tight_layout()

# Display the final plot
plt.show()