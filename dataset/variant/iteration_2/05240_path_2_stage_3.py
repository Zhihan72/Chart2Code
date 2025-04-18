import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Africa', 'Asia', 'Europe', 'South America']

north_america = [1.2, 0, 0, 1.8, 0.5]
africa = [10, 0.7, 0, 0.2, 0]
asia = [0, 1.5, 1.2, 0, 0]
europe = [0, 0, 0, 0.4, 0]
south_america = [0, 0, 0, 0, 1.5]

data = [north_america, africa, asia, europe, south_america]
data_transposed = np.array(data).T

colors = ['#52c94c', '#c94c4c', '#8e44ad', '#c9b34c', '#4c8ec9']

fig, ax = plt.subplots(figsize=(12, 8))

bottom_values = np.zeros(len(regions))
for species_data, color in zip(data_transposed, colors):
    ax.bar(regions, species_data, color=color, bottom=bottom_values)
    bottom_values += species_data

plt.show()