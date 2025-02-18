import matplotlib.pyplot as plt
import numpy as np

# Concept: Tracking the growth of renewable energy adoption over time across various technologies.
# Title: "Rising Waves of Green Energy: Adoption of Renewable Technologies (2000-2023)"
# Technologies: Solar Power, Wind Power, Hydro Power, Geothermal, Bioenergy

# Define the years for the x-axis (2000 - 2023)
years = np.arange(2000, 2025)

# Data for renewable energy adoption levels (in arbitrary units)
solar_power = np.array([10, 12, 15, 18, 25, 35, 45, 60, 80, 100, 120, 140, 165, 190, 215, 240, 275, 300, 340, 400, 450, 500, 550, 600, 650])
wind_power = np.array([5, 8, 12, 20, 30, 45, 55, 80, 110, 150, 200, 250, 300, 350, 400, 460, 520, 600, 700, 800, 900, 1000, 1100, 1150, 1200])
hydro_power = np.array([180, 182, 185, 188, 190, 195, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 275, 280])
geothermal = np.array([30, 32, 34, 37, 40, 45, 50, 55, 60, 70, 80, 90, 95, 100, 110, 120, 130, 140, 150, 155, 160, 165, 170, 172, 175])
bioenergy = np.array([50, 52, 55, 58, 63, 70, 75, 80, 90, 100, 110, 125, 130, 135, 140, 145, 150, 155, 170, 180, 190, 195, 200, 205, 210])

# Stack the data for the area chart
energy_data = np.vstack([solar_power, wind_power, hydro_power, geothermal, bioenergy])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stackplot for Renewable Energy Adoption
ax.stackplot(years, energy_data, labels=['Solar Power', 'Wind Power', 'Hydro Power', 'Geothermal', 'Bioenergy'],
             colors=['#ffd700', '#1e90ff', '#32cd32', '#ff7f50', '#9370db'], alpha=0.8)

# Add title and labels
ax.set_title('Rising Waves of Green Energy: Adoption of Renewable Technologies (2000-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Level (Arbitrary Units)', fontsize=12)

# Add legend and grid
ax.legend(loc='upper left', fontsize=10, title='Renewable Technologies', frameon=False)
ax.grid(linestyle='--', alpha=0.6)

# Enhance readability of x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1301, 100))

# Annotate significant milestones
ax.annotate('Major Solar Turnaround', xy=(2010, 100), xytext=(2005, 300),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=10, color='darkgoldenrod')

ax.annotate('Wind Power Boom', xy=(2015, 250), xytext=(2010, 800),
            arrowprops=dict(arrowstyle='->', connectionstyle='angle3', color='blue', lw=1.5),
            fontsize=10, color='blue')

# Add a brief description or note
description_box = dict(boxstyle='round', facecolor='lightgrey', alpha=0.3)
description = ("The expanding scope of clean, renewable energy sources is driving global energy transition.\n"
               "Technological advancements and supportive policies are fueling the growth across sectors.")
ax.text(0.02, 0.97, description, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=description_box)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()