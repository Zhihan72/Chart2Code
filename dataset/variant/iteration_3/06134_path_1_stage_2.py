import matplotlib.pyplot as plt
import numpy as np

# Define years from 2000 to 2020
years = np.arange(2000, 2021)

# Shuffled artificial data representing electricity generation in TWh
solar_energy =    np.array([1, 260, 3, 8, 15, 22, 30, 150, 45, 60, 80, 100, 130, 4, 180, 220, 2, 300, 350, 400, 450])
wind_energy =     np.array([4, 440, 11, 7, 17, 25, 35, 270, 70, 100, 135, 180, 220, 320, 320, 50, 670, 510, 590, 380, 750])
hydropower =      np.array([100, 145, 110, 115, 120, 215, 132, 138, 105, 195, 205, 168, 177, 186, 195, 205, 215, 153, 236, 247, 160])
geothermal_energy = np.array([10, 11, 88, 14, 16, 18, 21, 25, 29, 134, 40, 46, 53, 69, 29, 88, 78, 99, 110, 122, 61])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each energy source with new colors
ax.plot(years, solar_energy, label='Solar Energy', color='purple', linestyle='-', marker='o', linewidth=2)
ax.plot(years, wind_energy, label='Wind Energy', color='cyan', linestyle='--', marker='s', linewidth=2)
ax.plot(years, hydropower, label='Hydropower', color='lime', linestyle='-.', marker='^', linewidth=2)
ax.plot(years, geothermal_energy, label='Geothermal Energy', color='magenta', linestyle=':', marker='d', linewidth=2)

# Titles and labels
ax.set_title("Growth in Renewable Energy Adoption (2000-2020):\nElectricity Generation from Solar, Wind, Hydro, and Geothermal Sources", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Electricity Generation (TWh)", fontsize=12)

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.5)

# Annotating key years with significant growth in solar energy
significant_years = {
    2008: 'Global Financial Crisis\nPush for Renewables',
    2015: 'Paris Agreement',
    2020: 'Adoption Peak'
}

for year, event in significant_years.items():
    plt.annotate(event, (year, solar_energy[year-2000]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5))

# Adding a legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()