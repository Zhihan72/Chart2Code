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
              colors=['#8B0000', '#FFD700', '#1E90FF', '#32CD32', '#FF8C00'], 
              alpha=0.8)

plt.xlabel('Decade', fontsize=12)
plt.ylabel('Percentage Share (%)', fontsize=12)

plt.show()