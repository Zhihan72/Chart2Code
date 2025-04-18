import matplotlib.pyplot as plt
import numpy as np

years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
avg_temperature = np.array([15.2, 15.4, 15.6, 15.9, 16.0, 16.2, 16.4])
co2_levels = np.array([350, 360, 370, 380, 390, 400, 410])

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# CO2 Levels Trend
axs[0].plot(years, co2_levels, color='blue', marker='^', linestyle='-', linewidth=2)
axs[0].set_title('Atmospheric CO2 Levels in Ecolia (1990-2020)', fontsize=16, fontweight='bold', color='navy')
axs[0].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[0].set_ylabel('CO2 Levels (ppm)', fontsize=12, fontweight='bold')

# Temperature Trend
axs[1].plot(years, avg_temperature, color='orange', marker='o', linestyle='-', linewidth=2)
axs[1].set_title('Average Temperature Trend in Ecolia (1990-2020)', fontsize=16, fontweight='bold', color='darkorange')
axs[1].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[1].set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')

annotations = ['Industrial Boom', 'Renewable Initiatives', 'Eco-Revolution', 'Green Technology Adoption']
annotation_years = [1995, 2005, 2010, 2020]
annotation_temps = avg_temperature[[1, 3, 4, 6]]
annotation_co2 = co2_levels[[1, 3, 4, 6]]

for i, text in enumerate(annotations):
    axs[0].annotate(text, (annotation_years[i], annotation_co2[i]), textcoords="offset points", xytext=(0,10), ha='center', color='navy', fontsize=10, bbox=dict(facecolor='white', alpha=0.6))
    axs[1].annotate(text, (annotation_years[i], annotation_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', color='darkorange', fontsize=10, bbox=dict(facecolor='white', alpha=0.6))

plt.show()