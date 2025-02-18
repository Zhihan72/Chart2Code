import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

north_america = {'solar': [3, 2, 10, 5, 15, 20, 18], 'wind': [10, 3, 28, 15, 5, 20, 25], 'hydro': [17, 16, 18, 15, 21, 19, 20], 'other': [5, 2, 9, 7, 10, 1, 3]}
south_america = {'solar': [12, 8, 15, 4, 1, 2, 18], 'wind': [5, 2, 13, 3, 10, 7, 15], 'hydro': [24, 23, 25, 20, 27, 22, 26], 'other': [5, 2, 7, 9, 6, 8, 3]}
europe = {'solar': [25, 15, 35, 20, 30, 5, 10], 'wind': [25, 15, 35, 20, 5, 30, 10], 'hydro': [14, 12, 20, 16, 10, 22, 18], 'other': [2, 3, 8, 5, 4, 6, 7]}
asia = {'solar': [11, 18, 1, 2, 7, 3, 14], 'wind': [9, 5, 3, 14, 22, 18, 1], 'hydro': [15, 13, 11, 18, 16, 10, 20], 'other': [1, 5, 7, 2, 3, 9, 11]}
africa = {'solar': [30, 7, 18, 12, 4, 2, 25], 'wind': [12, 9, 2, 1, 4, 15, 6], 'hydro': [7, 9, 5, 6, 8, 10, 11], 'other': [8, 6, 4, 7, 5, 2, 3]}

def plot_renewable_adoption(years, data, name):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.stackplot(years, data['solar'], data['wind'], data['hydro'], data['other'],
                 labels=['Solar', 'Other', 'Wind', 'Hydro'], colors=['#e63946', '#f4a261', '#2a9d8f', '#264653'], alpha=0.9)

    ax.set_title(f'{name} Renewable Energy Adoption (2000-2030)', fontsize=14, fontweight='normal', color='darkblue')
    ax.set_xlabel('Year', fontsize=11, color='teal')
    ax.set_ylabel('% of Energy', fontsize=11, color='teal')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=30)
    ax.set_ylim(0, 100)
    
    ax.legend(loc='lower left', fontsize=8, markerscale=1.2)
    ax.grid(True, linestyle='--', linewidth=0.5, color='gray')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_linewidth(0.5)
    ax.spines['right'].set_color('gray')

    plt.tight_layout()
    plt.show()

plot_renewable_adoption(years, north_america, "N. America")
plot_renewable_adoption(years, south_america, "S. America")
plot_renewable_adoption(years, europe, "Europe")
plot_renewable_adoption(years, asia, "Asia")
plot_renewable_adoption(years, africa, "Africa")