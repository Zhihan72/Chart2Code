import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

north_america = {
    'sunlight': [2, 3, 5, 10, 15, 18, 20],
    'breeze': [3, 5, 10, 15, 20, 25, 28],
    'water_flow': [15, 16, 17, 18, 19, 20, 21],
    'misc': [1, 2, 3, 5, 7, 9, 10]
}

south_america = {
    'sunlight': [1, 2, 4, 8, 12, 15, 18],
    'breeze': [2, 3, 5, 7, 10, 13, 15],
    'water_flow': [20, 22, 23, 24, 25, 26, 27],
    'misc': [2, 3, 5, 6, 7, 8, 9]
}

europe = {
    'solar_power': [5, 10, 15, 20, 25, 30, 35],
    'wind_power': [5, 10, 15, 20, 25, 30, 35],
    'hydro_power': [10, 12, 14, 16, 18, 20, 22],
    'other_means': [2, 3, 4, 5, 6, 7, 8]
}

asia = {
    'solar_energy': [1, 2, 3, 7, 11, 14, 18],
    'wind_energy': [1, 3, 5, 9, 14, 18, 22],
    'hydro_energy': [10, 11, 13, 15, 16, 18, 20],
    'other_sources': [1, 2, 3, 5, 7, 9, 11]
}

africa = {
    'sunlight_energy': [2, 4, 7, 12, 18, 25, 30],
    'wind_current': [1, 2, 4, 6, 9, 12, 15],
    'hydro_techno': [5, 6, 7, 8, 9, 10, 11],
    'assorted': [2, 3, 4, 5, 6, 7, 8]
}

def plot_renewable_energy_shift(years, continent_data, continent_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    sun = continent_data['sunlight'] if 'sunlight' in continent_data else continent_data['solar_power'] if 'solar_power' in continent_data else continent_data['solar_energy'] if 'solar_energy' in continent_data else continent_data['sunlight_energy']
    breeze = continent_data['breeze'] if 'breeze' in continent_data else continent_data['wind_power'] if 'wind_power' in continent_data else continent_data['wind_energy'] if 'wind_energy' in continent_data else continent_data['wind_current']
    water_flow = continent_data['water_flow'] if 'water_flow' in continent_data else continent_data['hydro_power'] if 'hydro_power' in continent_data else continent_data['hydro_energy'] if 'hydro_energy' in continent_data else continent_data['hydro_techno']
    assorted = continent_data['misc'] if 'misc' in continent_data else continent_data['other_means'] if 'other_means' in continent_data else continent_data['other_sources'] if 'other_sources' in continent_data else continent_data['assorted']

    ax.stackplot(years, sun, breeze, water_flow, assorted, 
                 colors=['#ff6f61', '#6b5b95', '#88b04b', '#ffcc5c'], 
                 alpha=0.8)

    ax.set_title(f'Energy Trend in {continent_name}\n(2000-2030)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Annual Progression', fontsize=12)
    ax.set_ylabel('Proportion of Energy', fontsize=12)
    
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45)
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.show()

plot_renewable_energy_shift(years, north_america, "The Americas North")
plot_renewable_energy_shift(years, south_america, "The Americas South City")
plot_renewable_energy_shift(years, europe, "Continental Europe")
plot_renewable_energy_shift(years, asia, "Asiatic Zone")
plot_renewable_energy_shift(years, africa, "African Territories")