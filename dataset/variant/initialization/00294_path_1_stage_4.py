import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2024)
solar_energy_percentage = [
    0.5, 0.7, 1.0, 1.5, 2.3, 3.2, 4.5, 6.0, 8.0, 10.0, 
    12.5, 15.3, 18.0, 21.0, 25.0, 29.0, 34.0, 40.0, 46.0, 52.0, 
    59.0, 67.0, 74.0, 80.0
]
wind_energy_percentage = [
    1.0, 1.2, 1.6, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 
    10.0, 12.0, 14.5, 17.0, 20.0, 24.0, 29.0, 35.0, 41.0, 48.0, 
    56.0, 64.0, 72.0, 78.0
]
biomass_energy_percentage = [
    0.5, 0.8, 1.2, 1.8, 2.1, 2.7, 3.3, 4.1, 5.0, 6.5, 
    7.8, 9.2, 11.0, 13.0, 15.5, 18.0, 21.0, 24.0, 28.0, 32.0, 
    36.0, 40.0, 45.0, 50.0
]
geothermal_energy_percentage = [
    0.3, 0.4, 0.5, 0.7, 0.8, 1.0, 1.4, 1.8, 2.2, 2.8, 
    3.5, 4.0, 4.8, 5.5, 6.3, 7.0, 8.0, 9.0, 10.0, 11.5, 
    13.0, 14.5, 16.0, 17.5
]

fig, axs = plt.subplots(1, 2, figsize=(16, 6), sharex=True)

# First subplot: Line chart
axs[0].plot(years, solar_energy_percentage, color='green', marker='o', linestyle='-', linewidth=2, label='Solar')
axs[0].plot(years, wind_energy_percentage, color='orange', marker='s', linestyle='--', linewidth=2, label='Wind')
axs[0].plot(years, biomass_energy_percentage, color='blue', marker='^', linestyle='-.', linewidth=2, label='Biomass')
axs[0].plot(years, geothermal_energy_percentage, color='purple', marker='D', linestyle=':', linewidth=2, label='Geothermal')
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].axvline(2010, color='grey', linestyle='--', alpha=0.5)
axs[0].axvline(2020, color='grey', linestyle='--', alpha=0.5)
axs[0].legend()

# Second subplot: Bar chart
width = 0.2
x_indexes = np.arange(len(years))
axs[1].bar(x_indexes - 1.5*width, solar_energy_percentage, width=width, color='green', label='Solar')
axs[1].bar(x_indexes - 0.5*width, wind_energy_percentage, width=width, color='brown', label='Wind')
axs[1].bar(x_indexes + 0.5*width, biomass_energy_percentage, width=width, color='orange', label='Biomass')
axs[1].bar(x_indexes + 1.5*width, geothermal_energy_percentage, width=width, color='purple', label='Geothermal')
axs[1].set_xticks(x_indexes)
axs[1].set_xticklabels(years, rotation=45)
axs[1].legend()

plt.tight_layout()
plt.show()