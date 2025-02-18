import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = ['2018', '2019', '2020', '2021', '2022']

# CO2 emissions data (in million tons) for continents, now sorted in ascending order for each year
emissions_data = {
    '2018': [('Africa', 1300), ('South America', 2000), ('Europe', 4300), ('North America', 5900), ('Asia', 17000)],
    '2019': [('Africa', 1400), ('South America', 2100), ('Europe', 4200), ('North America', 5800), ('Asia', 17500)],
    '2020': [('Africa', 1500), ('South America', 2200), ('Europe', 4100), ('North America', 5700), ('Asia', 18000)],
    '2021': [('Africa', 1600), ('South America', 2300), ('Europe', 4000), ('North America', 5600), ('Asia', 18500)],
    '2022': [('Africa', 1700), ('South America', 2400), ('Europe', 3900), ('North America', 5500), ('Asia', 19000)]
}

# Extract sorted emissions and labels for each year
sorted_years = {year: sorted(data, key=lambda x: x[1]) for year, data in emissions_data.items()}

# Prepare the figure and axis
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))

# Main sorted bar chart for CO2 emissions
for i, year in enumerate(years):
    axs[0, 0].bar(
        [label for label, _ in sorted_years[year]],
        [emission for _, emission in sorted_years[year]],
        alpha=0.7,
        label=year
    )

axs[0, 0].set_title('Annual Carbon Output (2018-2022)', fontsize=16)
axs[0, 0].set_xlabel('Continent', fontsize=14)
axs[0, 0].set_ylabel('Emission Levels (MT)', fontsize=14)
axs[0, 0].legend(loc='upper left')
axs[0, 0].grid(True, linestyle='--', alpha=0.5)

# Subplot for North America
axs[1, 0].pie([80, 15, 5], labels=['USA', 'Canada', 'Mexico'], autopct='%1.1f%%', colors=['navy', 'lightblue', 'lightgrey'])
axs[1, 0].set_title('NA CO2 Division (2022)', fontsize=14)

# Subplot for Europe
axs[0, 1].pie([40, 30, 30], labels=['Germany', 'UK', 'France'], autopct='%1.1f%%', colors=['green', 'limegreen', 'lightgreen'])
axs[0, 1].set_title('EU CO2 Split (2022)', fontsize=14)

# Subplot for Asia
axs[0, 2].pie([50, 30, 20], labels=['China', 'India', 'Japan'], autopct='%1.1f%%', colors=['darkred', 'orangered', 'pink'])
axs[0, 2].set_title('AS Region CO2 (2022)', fontsize=14)

# Subplot for Africa
axs[1, 1].pie([30, 25, 20], labels=['South Africa', 'Nigeria', 'Egypt'], autopct='%1.1f%%', colors=['sienna', 'peru', 'navajowhite'])
axs[1, 1].set_title('AF Emissions Share (2022)', fontsize=14)

# Subplot for South America
axs[1, 2].pie([50, 30, 20], labels=['Brazil', 'Argentina', 'Colombia'], autopct='%1.1f%%', colors=['purple', 'violet', 'lavender'])
axs[1, 2].set_title('SA CO2 Distribution (2022)', fontsize=14)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()