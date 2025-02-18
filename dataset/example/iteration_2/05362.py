import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the yearly water consumption trends from three fictional futuristic cities: Neo-Tokyo, Metropolis, and Omega City, from the years 2050 to 2060.
# We explore their water usage and compare these trends using line plots and an overlay to indicate important events (e.g., implementation of new water-saving technologies).

# Years from 2050 to 2060
years = np.arange(2050, 2061)

# Artificial data for water consumption (in million gallons)
neo_tokyo_consumption = np.array([320, 330, 305, 295, 310, 290, 280, 275, 265, 250, 240])
metropolis_consumption = np.array([345, 340, 335, 320, 315, 310, 300, 285, 270, 260, 255])
omega_city_consumption = np.array([290, 295, 285, 280, 275, 265, 255, 250, 245, 230, 220])

# Important events
events = {
    "Neo-Tokyo": [(2052, 'New Water Treatment Plant Operational'), (2056, 'Water-Saving Campaign Launched')],
    "Metropolis": [(2055, 'Water Recycling System Upgrade')],
    "Omega City": [(2053, 'Lake Reservoir Accident')]
}

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the water consumption data with markers
ax.plot(years, neo_tokyo_consumption, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8, label='Neo-Tokyo')
ax.plot(years, metropolis_consumption, marker='s', linestyle='-', color='green', linewidth=2, markersize=8, label='Metropolis')
ax.plot(years, omega_city_consumption, marker='^', linestyle='-', color='red', linewidth=2, markersize=8, label='Omega City')

# Annotate important events
for city, events_list in events.items():
    for year, event in events_list:
        idx = year - 2050
        if city == "Neo-Tokyo":
            xytext = (-70, 30)
            xy = (year, neo_tokyo_consumption[idx])
        elif city == "Metropolis":
            xytext = (-70, -50)
            xy = (year, metropolis_consumption[idx])
        else:  # Omega City
            xytext = (70, 30)
            xy = (year, omega_city_consumption[idx])

        ax.annotate(event, xy=xy, xytext=xytext, textcoords='offset points', 
                    arrowprops=dict(arrowstyle='->', color='black'), fontsize=10, backgroundcolor='white')

# Set titles and labels
ax.set_title('Water Consumption Trends in Futuristic Cities (2050-2060)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Water Consumption (Million Gallons)', fontsize=14)

# Display legend
ax.legend(loc='upper right', fontsize=12, frameon=True)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()