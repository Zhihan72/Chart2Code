import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Africa', 'Europe', 'South America']

north_america = [1.2, 0, -1.8, -0.5]
africa = [-10, 0.7, -0.2, 0]
europe = [0, 0, 0.4, 0]
south_america = [0, 0, 0, -1.5]

data = [north_america, africa, europe, south_america]
data_transposed = np.array(data).T

colors = ['#52c94c', '#c94c4c', '#c9b34c', '#4c8ec9']

fig, ax = plt.subplots(figsize=(12, 8))

for idx, (species_data, color) in enumerate(zip(data_transposed, colors)):
    ax.barh(regions, species_data, color=color, left=[0]*len(species_data), 
            edgecolor='grey', linewidth=0.7, label=f'Dataset {idx+1}')

ax.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()