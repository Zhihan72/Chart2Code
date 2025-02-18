import matplotlib.pyplot as plt
import numpy as np

# Years spanning three decades (1990-2020)
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])

# Artificial data for average temperature, precipitation, and CO2 levels
avg_temperature = np.array([15.2, 15.4, 15.6, 15.9, 16.0, 16.2, 16.4])
avg_precipitation = np.array([1100, 1120, 1090, 1150, 1180, 1200, 1225])
co2_levels = np.array([350, 360, 370, 380, 390, 400, 410])

# Plotting setup
fig, axs = plt.subplots(1, 3, figsize=(18, 5), constrained_layout=True)

# Temperature Trend
axs[0].plot(years, avg_temperature, color='red', marker='o', linestyle='-', linewidth=2)
axs[0].set_title('Temperature (°C)', fontsize=14, fontweight='bold', color='darkred')
axs[0].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[0].set_ylabel('°C', fontsize=12, fontweight='bold')
axs[0].grid(True, linestyle='--', alpha=0.5)

# Precipitation Trend
axs[1].plot(years, avg_precipitation, color='blue', marker='s', linestyle='-', linewidth=2)
axs[1].set_title('Precipitation (mm)', fontsize=14, fontweight='bold', color='navy')
axs[1].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[1].set_ylabel('mm', fontsize=12, fontweight='bold')
axs[1].grid(True, linestyle='--', alpha=0.5)

# CO2 Levels Trend
axs[2].plot(years, co2_levels, color='green', marker='^', linestyle='-', linewidth=2)
axs[2].set_title('CO2 Levels (ppm)', fontsize=14, fontweight='bold', color='darkgreen')
axs[2].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[2].set_ylabel('ppm', fontsize=12, fontweight='bold')
axs[2].grid(True, linestyle='--', alpha=0.5)

# Annotate significant years
annotations = ['Industrial Boom', 'Renewable Initiatives', 'Eco-Revolution', 'Green Technology Adoption']
annotation_years = [1995, 2005, 2010, 2020]
annotation_temps = avg_temperature[[1, 3, 4, 6]]
annotation_precip = avg_precipitation[[1, 3, 4, 6]]
annotation_co2 = co2_levels[[1, 3, 4, 6]]

for i, text in enumerate(annotations):
    axs[0].annotate(text, (annotation_years[i], annotation_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', color='darkred', fontsize=10, bbox=dict(facecolor='white', alpha=0.6))
    axs[1].annotate(text, (annotation_years[i], annotation_precip[i]), textcoords="offset points", xytext=(0,10), ha='center', color='navy', fontsize=10, bbox=dict(facecolor='white', alpha=0.6))
    axs[2].annotate(text, (annotation_years[i], annotation_co2[i]), textcoords="offset points", xytext=(0,10), ha='center', color='darkgreen', fontsize=10, bbox=dict(facecolor='white', alpha=0.6))

# Display the plot
plt.show()