import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solar_energy = [10, 20, 30, 45, 55, 70, 85, 100, 115, 130, 150]
wind_energy = [15, 25, 35, 45, 60, 75, 90, 105, 120, 140, 160]
hydro_energy = [20, 30, 40, 55, 65, 80, 95, 110, 130, 150, 170]
geothermal_energy = [5, 10, 15, 25, 35, 45, 60, 75, 90, 110, 130]

# Shuffled colors list
colors = ['#32CD32', '#FFD700', '#FF6347', '#1E90FF']

fig, ax = plt.subplots(figsize=(14, 8))

# Apply the shuffled colors
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, geothermal_energy, 
             colors=colors, alpha=0.8)

plt.show()