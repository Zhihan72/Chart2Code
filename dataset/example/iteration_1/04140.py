import matplotlib.pyplot as plt
import numpy as np

# Defining the years and power generation data in gigawatts (GW)
years = np.arange(2010, 2021)
solar_energy = [15, 22, 30, 45, 68, 95, 130, 170, 215, 265, 320]
wind_energy = [80, 95, 105, 120, 145, 160, 185, 215, 250, 290, 340]
hydro_energy = [900, 920, 935, 950, 965, 980, 995, 1005, 1015, 1025, 1035]
geothermal_energy = [10, 11, 12, 14, 16, 18, 21, 24, 28, 33, 39]

# Setting up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
ax.plot(years, solar_energy, marker='o', linestyle='-', color='#FFA07A', linewidth=2, label='Solar Energy')
ax.plot(years, wind_energy, marker='s', linestyle='-', color='#8FBC8F', linewidth=2, label='Wind Energy')
ax.plot(years, hydro_energy, marker='^', linestyle='-', color='#6495ED', linewidth=2, label='Hydro Energy')
ax.plot(years, geothermal_energy, marker='D', linestyle='-', color='#FFD700', linewidth=2, label='Geothermal Energy')

# Adding labels and title
plt.title('Trend of Power Generation from Renewable Energy Sources (2010 - 2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Power Generation Capacity (GW)', fontsize=14)

# Adding grid
plt.grid(True, linestyle='--', alpha=0.6)

# Adding legend
plt.legend(title='Energy Sources', title_fontsize='13', fontsize='12', loc='upper left')

# Annotations
ax.annotate('Significant Growth', xy=(2016, 18), xytext=(2013, 60),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkred')

# Adding context with text
plt.text(2010, 320, "The rise in renewable energy adoption\nis driven by technological advancements\nand global environmental policies.",
         fontsize=12, color='grey', bbox=dict(facecolor='white', alpha=0.5))

# Tight layout
plt.tight_layout()

# Show the plot
plt.show()