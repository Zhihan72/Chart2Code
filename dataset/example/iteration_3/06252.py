import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart depicts the growth and decline of different vehicle types in a fictional city named "Automotiville"
# over the decade from 2010 to 2020. The city underwent massive urban development and shifts in transportation trends.
# Data reflects registrations of different vehicle types over the years.

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Registration data for each type of vehicle (in thousands)
gas_vehicles = np.array([50, 48, 45, 40, 35, 30,25,20,15,10,5])
electric_vehicles = np.array([1, 2, 4, 6, 10, 15, 25, 30, 40, 50, 65])
hybrid_vehicles = np.array([5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 38])
bikes = np.array([10, 12, 15, 19, 25, 35, 45, 50, 55, 60, 70])
public_transport = np.array([30, 31, 32, 33, 34, 33, 34, 35, 36, 37, 38])

# Stack the data for the area chart
vehicle_data = np.vstack([gas_vehicles, electric_vehicles, hybrid_vehicles, bikes, public_transport])

# Define colors for each vehicle type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the figure and axis for the area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack plot for vehicle registrations
ax.stackplot(years, vehicle_data, labels=[
    'Gas Vehicles', 'Electric Vehicles', 'Hybrid Vehicles', 'Bikes', 'Public Transport'],
    colors=colors, alpha=0.8)

# Customize the plot
ax.set_title('Transportation Evolution in Automotiville\nVehicle Registration Trends (2010-2020)',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Registrations (Thousands)', fontsize=12)

# Add legend and grid
ax.legend(loc='upper left', fontsize=10, title='Vehicle Types', frameon=False)
ax.grid(linestyle='--', alpha=0.6)

# Adjust x-axis labels to prevent overlap
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 81, 10))

# Annotate significant shifts in trend
ax.annotate('Electric vehicles gain popularity', xy=(2015, 20), xytext=(2016, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=10, color='blue')

ax.annotate('Gas vehicles decline', xy=(2015, 35), xytext=(2013, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=-.2'), fontsize=10, color='red')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()