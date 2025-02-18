import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

north_america = {
    'solar': [2, 3, 5, 10, 15, 18, 20],
    'wind': [3, 5, 10, 15, 20, 25, 28],
    'hydro': [15, 16, 17, 18, 19, 20, 21],
    'other': [1, 2, 3, 5, 7, 9, 10]
}

south_america = {
    'solar': [1, 2, 4, 8, 12, 15, 18],
    'wind': [2, 3, 5, 7, 10, 13, 15],
    'hydro': [20, 22, 23, 24, 25, 26, 27],
    'other': [2, 3, 5, 6, 7, 8, 9]
}

europe = {
    'solar': [5, 10, 15, 20, 25, 30, 35],
    'wind': [5, 10, 15, 20, 25, 30, 35],
    'hydro': [10, 12, 14, 16, 18, 20, 22],
    'other': [2, 3, 4, 5, 6, 7, 8]
}

asia = {
    'solar': [1, 2, 3, 7, 11, 14, 18],
    'wind': [1, 3, 5, 9, 14, 18, 22],
    'hydro': [10, 11, 13, 15, 16, 18, 20],
    'other': [1, 2, 3, 5, 7, 9, 11]
}

africa = {
    'solar': [2, 4, 7, 12, 18, 25, 30],
    'wind': [1, 2, 4, 6, 9, 12, 15],
    'hydro': [5, 6, 7, 8, 9, 10, 11],
    'other': [2, 3, 4, 5, 6, 7, 8]
}

def plot_renewable_energy_adoption(years, continent_data, continent_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    solar = continent_data['solar']
    wind = continent_data['wind']
    hydro = continent_data['hydro']
    other = continent_data['other']

    ax.stackplot(years, solar, wind, hydro, other, 
                 colors=['#f9c74f', '#90be6d', '#43aa8b', '#577590'], 
                 alpha=0.8)

    ax.set_title(f'Renewable Energy Adoption in {continent_name}\n(2000-2030)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Percentage of Total Energy Consumption', fontsize=12)
    
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45)
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.show()

plot_renewable_energy_adoption(years, north_america, "North America")
plot_renewable_energy_adoption(years, south_america, "South America")
plot_renewable_energy_adoption(years, europe, "Europe")
plot_renewable_energy_adoption(years, asia, "Asia")
plot_renewable_energy_adoption(years, africa, "Africa")