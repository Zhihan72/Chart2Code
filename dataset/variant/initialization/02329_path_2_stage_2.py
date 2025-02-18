import matplotlib.pyplot as plt
import numpy as np

decades = ['1980', '1990', '2000', '2010', '2020']
coal = [50, 45, 40, 30, 20]
nuclear = [10, 15, 20, 20, 15]
natural_gas = [20, 20, 25, 30, 25]
hydro = [15, 12, 10, 10, 10]
renewables = [5, 8, 5, 10, 30]

data = np.array([coal, nuclear, natural_gas, hydro, renewables])

plt.figure(figsize=(12, 8))
plt.stackplot(decades, coal, nuclear, natural_gas, hydro, renewables,
              colors=['#A52A2A', '#FFFF00', '#00BFFF', '#00FF7F', '#FF4500'], 
              alpha=0.7)

plt.legend(loc='lower left', bbox_to_anchor=(0, 0))

plt.grid(True, linestyle=':', linewidth=0.5)
plt.tight_layout()

plt.show()