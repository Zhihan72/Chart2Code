import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2022)
regions = ['N. America', 'Europe']

solar_projects = {
    'North America': [5, 7, 9, 12, 15, 17, 20, 22, 24, 26, 29, 31],
    'Europe': [8, 10, 12, 15, 17, 19, 22, 25, 27, 30, 32, 35],
}

wind_projects = {
    'North America': [6, 8, 10, 14, 18, 20, 22, 24, 26, 28, 30, 32],
    'Europe': [9, 11, 14, 16, 19, 21, 24, 27, 29, 31, 34, 36],
}

hydro_projects = {
    'North America': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    'Europe': [4, 5, 6, 8, 9, 11, 13, 14, 15, 16, 17, 18],
}

fig, ax = plt.subplots(2, 1, figsize=(14, 12))
height = 0.2
consistent_color = 'mediumseagreen'

for idx, region in enumerate(regions):
    ax[idx].barh(years - height, solar_projects[region if region != 'N. America' else 'North America'], 
                 height=height, label='Solar', color=consistent_color)
    ax[idx].barh(years, wind_projects[region if region != 'N. America' else 'North America'], 
                 height=height, label='Wind', color=consistent_color)
    ax[idx].barh(years + height, hydro_projects[region if region != 'N. America' else 'North America'], 
                 height=height, label='Hydro', color=consistent_color)
    
    ax[idx].set_title(f'{region} - Projects', fontsize=14, fontweight='bold', pad=15)
    ax[idx].set_ylabel('Year', fontsize=12)
    ax[idx].set_xlabel('No. of Projects', fontsize=12)
    ax[idx].set_yticks(years)
    ax[idx].set_yticklabels(years, fontsize=10)
    ax[idx].legend(title='Type', loc='best', fontsize=10)
    ax[idx].grid(True, linestyle='--', linewidth=0.7)

fig.suptitle('Energy Projects (2010-2021)', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()