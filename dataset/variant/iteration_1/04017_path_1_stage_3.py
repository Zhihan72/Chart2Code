import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2022)
regions = ['N. America', 'Europe', 'Asia']

solar_projects = {
    'North America': [5, 7, 9, 12, 15, 17, 20, 22, 24, 26, 29, 31],
    'Europe': [8, 10, 12, 15, 17, 19, 22, 25, 27, 30, 32, 35],
    'Asia': [10, 15, 20, 25, 28, 30, 32, 34, 36, 38, 40, 45]
}

wind_projects = {
    'North America': [6, 8, 10, 14, 18, 20, 22, 24, 26, 28, 30, 32],
    'Europe': [9, 11, 14, 16, 19, 21, 24, 27, 29, 31, 34, 36],
    'Asia': [7, 9, 11, 16, 20, 22, 24, 26, 28, 30, 33, 36]
}

hydro_projects = {
    'North America': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    'Europe': [4, 5, 6, 8, 9, 11, 13, 14, 15, 16, 17, 18],
    'Asia': [3, 6, 9, 11, 14, 15, 16, 18, 19, 21, 23, 25]
}

fig, ax = plt.subplots(3, 1, figsize=(14, 18))
height = 0.2

for idx, region in enumerate(regions):
    ax[idx].barh(years - height, solar_projects[region if region != 'N. America' else 'North America'], height=height, label='Solar', color='darkorange', hatch='//')
    ax[idx].barh(years, wind_projects[region if region != 'N. America' else 'North America'], height=height, label='Wind', color='deepskyblue', hatch='x')
    ax[idx].barh(years + height, hydro_projects[region if region != 'N. America' else 'North America'], height=height, label='Hydro', color='darkseagreen', hatch='o')
    
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