import matplotlib.pyplot as plt
import numpy as np

# Define city names and months
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'San Francisco']
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Data representing monthly CO2 emissions (in metric tons) for each city
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

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
total_emissions = emissions_data.sum(axis=1)

axs[0].barh(cities, total_emissions, color=colors, edgecolor='black')
axs[0].set_title('Total CO2 Emissions by City Over Six Months', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Total CO2 Emissions (metric tons)', fontsize=14)
axs[0].set_ylabel('Cities', fontsize=14)

for i, city in enumerate(cities):
    axs[1].bar(np.arange(len(months)) + i * 0.15, emissions_data[i], width=0.15, color=colors[i])

axs[1].set_title('Monthly CO2 Emissions Distribution Across Major US Cities (in metric tons)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Month', fontsize=14)
axs[1].set_ylabel('CO2 Emissions (metric tons)', fontsize=14)
axs[1].set_xticks(np.arange(len(months)))
axs[1].set_xticklabels(months, rotation=15, ha='right')

plt.tight_layout()
plt.show()