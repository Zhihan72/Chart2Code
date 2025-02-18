import matplotlib.pyplot as plt
import numpy as np

decades = ['1980', '1990', '2000', '2010', '2020']
coal = [50, 45, 40, 30, 20]
nuclear = [10, 15, 20, 20, 15]
natural_gas = [20, 20, 25, 30, 25]
hydro = [15, 12, 10, 10, 10]
renewables = [5, 8, 5, 10, 30]

# Add new made-up data series
biomass = [2, 3, 5, 8, 12]
geothermal = [1, 2, 3, 4, 5]

data = np.array([coal, nuclear, natural_gas, hydro, renewables, biomass, geothermal])

plt.figure(figsize=(12, 8))
plt.stackplot(decades, coal, nuclear, natural_gas, hydro, renewables, biomass, geothermal,
              colors=['#8A2BE2', '#5F9EA0', '#D2691E', '#FF1493', '#7FFF00', '#FFD700', '#7FFFD4'], 
              alpha=0.7)

plt.legend(['Coal', 'Nuclear', 'Natural Gas', 'Hydro', 'Renewables', 'Biomass', 'Geothermal'], 
           loc='lower left', bbox_to_anchor=(0, 0))

plt.grid(True, linestyle=':', linewidth=0.5)
plt.tight_layout()

plt.show()