import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

north_america = {'solar': [2, 3, 5, 10, 15, 18, 20], 'wind': [3, 5, 10, 15, 20, 25, 28], 'hydro': [15, 16, 17, 18, 19, 20, 21], 'other': [1, 2, 3, 5, 7, 9, 10]}
south_america = {'solar': [1, 2, 4, 8, 12, 15, 18], 'wind': [2, 3, 5, 7, 10, 13, 15], 'hydro': [20, 22, 23, 24, 25, 26, 27], 'other': [2, 3, 5, 6, 7, 8, 9]}
europe = {'solar': [5, 10, 15, 20, 25, 30, 35], 'wind': [5, 10, 15, 20, 25, 30, 35], 'hydro': [10, 12, 14, 16, 18, 20, 22], 'other': [2, 3, 4, 5, 6, 7, 8]}
asia = {'solar': [1, 2, 3, 7, 11, 14, 18], 'wind': [1, 3, 5, 9, 14, 18, 22], 'hydro': [10, 11, 13, 15, 16, 18, 20], 'other': [1, 2, 3, 5, 7, 9, 11]}
africa = {'solar': [2, 4, 7, 12, 18, 25, 30], 'wind': [1, 2, 4, 6, 9, 12, 15], 'hydro': [5, 6, 7, 8, 9, 10, 11], 'other': [2, 3, 4, 5, 6, 7, 8]}

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