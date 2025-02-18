import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solar_energy = [10, 20, 30, 45, 55, 70, 85, 100, 115, 130, 150]
wind_energy = [15, 25, 35, 45, 60, 75, 90, 105, 120, 140, 160]
# hydro_energy data group removed
geothermal_energy = [5, 10, 15, 25, 35, 45, 60, 75, 90, 110, 130]

# Adjusted colors list as a color was used for each energy group
colors = ['#32CD32', '#FFD700', '#1E90FF']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, solar_energy, wind_energy, geothermal_energy, 
             colors=colors, alpha=0.8)

plt.show()