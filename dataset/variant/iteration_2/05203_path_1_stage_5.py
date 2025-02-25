import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'San Francisco']
months = ['January', 'February', 'March', 'April', 'May', 'June']

ny_emissions = [180, 190, 200, 210, 220, 230]
la_emissions = [170, 180, 190, 195, 205, 215]
chicago_emissions = [160, 170, 180, 190, 185, 195]
houston_emissions = [200, 205, 210, 215, 225, 230]
phoenix_emissions = [150, 155, 160, 165, 170, 180]
miami_emissions = [130, 140, 150, 160, 170, 180]
sf_emissions = [140, 145, 155, 165, 175, 185]

emissions_data = np.array([ny_emissions, la_emissions, chicago_emissions, houston_emissions,
                           phoenix_emissions, miami_emissions, sf_emissions])

fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# New color set chosen manually
colors = ['#00bfa5', '#d50000', '#ffd600', '#304ffe', '#76ff03', '#f50057', '#6200ea']
total_emissions = emissions_data.sum(axis=1)

axs[0].barh(cities, total_emissions, color=colors, edgecolor='black')

for i, city in enumerate(cities):
    axs[1].bar(np.arange(len(months)) + i * 0.15, emissions_data[i], width=0.15, color=colors[i])

plt.tight_layout()
plt.show()