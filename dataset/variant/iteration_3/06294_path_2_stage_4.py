import matplotlib.pyplot as plt
import numpy as np

# Data setup
decades = np.array(['80s', '90s', '00s', '10s', '20s'])
solar_energy = np.array([2, 5, 10, 18, 25])
wind_energy = np.array([1, 3, 12, 20, 30])
hydropower = np.array([10, 15, 20, 25, 28])
geothermal = np.array([2, 4, 6, 10, 12])
biomass = np.array([1, 2, 4, 6, 8])
tidal = np.array([0.5, 1, 2, 3, 4])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Shuffled colors
ax.fill_between(decades, solar_energy, color='#ADFF2F', alpha=0.7)  # biomass color
ax.fill_between(decades, solar_energy, wind_energy + solar_energy, color='#4682B4', alpha=0.7)  # tidal color
ax.fill_between(decades, wind_energy + solar_energy, wind_energy + solar_energy + hydropower, color='#8B4513', alpha=0.7)  # geothermal color
ax.fill_between(decades, wind_energy + solar_energy + hydropower, wind_energy + solar_energy + hydropower + geothermal, color='#32CD32', alpha=0.7)  # hydropower color
ax.fill_between(decades, wind_energy + solar_energy + hydropower + geothermal, 
                wind_energy + solar_energy + hydropower + geothermal + biomass, color='#FFD700', alpha=0.7)  # solar energy color
ax.fill_between(decades, wind_energy + solar_energy + hydropower + geothermal + biomass, 
                wind_energy + solar_energy + hydropower + geothermal + biomass + tidal, color='#1E90FF', alpha=0.7)  # wind energy color

# Add titles and labels
ax.set_title('Renewable Energy by Decade', fontsize=16, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Energy Share (%)', fontsize=12)

# Customize x-axis ticks
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, rotation=45)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()