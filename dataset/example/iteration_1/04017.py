import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Green Energy Projects Initiated Over the Years
# This chart represents the number of solar, wind, and hydro projects started from 2010 to 2021 
# in different regions: North America, Europe, and Asia

# Define the years and regions
years = np.arange(2010, 2022)
regions = ['North America', 'Europe', 'Asia']

# Number of projects for each type in each region
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

# Initialize the subplots
fig, ax = plt.subplots(3, 1, figsize=(14, 18))

# Define bar width
width = 0.2

# Iterate through each region and plot the data
for idx, region in enumerate(regions):
    ax[idx].bar(years - width, solar_projects[region], width=width, label='Solar Projects', color='goldenrod')
    ax[idx].bar(years, wind_projects[region], width=width, label='Wind Projects', color='skyblue')
    ax[idx].bar(years + width, hydro_projects[region], width=width, label='Hydro Projects', color='seagreen')
    
    # Labeling the chart
    ax[idx].set_title(f'{region} - Green Energy Projects Initiated Over the Years', fontsize=14, fontweight='bold', pad=10)
    ax[idx].set_xlabel('Year', fontsize=12)
    ax[idx].set_ylabel('Number of Projects', fontsize=12)
    ax[idx].set_xticks(years)
    ax[idx].set_xticklabels(years, rotation=45, fontsize=10)
    ax[idx].legend(title='Energy Type', loc='upper left', fontsize=10)

# Main title for the entire figure
fig.suptitle('Evolution of Green Energy Initiatives (2010-2021)', fontsize=16, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the combined plot
plt.show()