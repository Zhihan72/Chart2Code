import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Global Effort to Reduce Carbon Emissions
# The line chart will display the carbon dioxide emission reductions (in billion tons) by different countries over a decade (2010-2020).

# Define countries and years
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

# Data: Carbon dioxide emission reductions (in billion tons)
co2_reductions = np.array([
    [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0],   # Country A
    [0.3, 0.32, 0.34, 0.37, 0.4, 0.42, 0.45, 0.48, 0.5, 0.52, 0.55], # Country B
    [0.2, 0.23, 0.25, 0.28, 0.3, 0.33, 0.35, 0.38, 0.4, 0.43, 0.45], # Country C
    [0.4, 0.42, 0.45, 0.47, 0.5, 0.53, 0.55, 0.58, 0.6, 0.63, 0.65], # Country D
    [0.1, 0.13, 0.15, 0.17, 0.2, 0.22, 0.25, 0.27, 0.3, 0.33, 0.35]  # Country E
])

# Create the plot
plt.figure(figsize=(14, 8))

# Plot lines for each country's CO2 emission reductions
for i, country in enumerate(countries):
    plt.plot(years, co2_reductions[i], marker='o', label=country)

# Annotations for significant milestones
milestones = {
    2012: ("Kyoto Protocol Extension", 0.7),
    2015: ("Paris Agreement", 0.75),
    2018: ("IPCC Special Report", 0.9)
}

for year, (text, level) in milestones.items():
    plt.annotate(text,
                 xy=(year, level),
                 xytext=(year, level + 0.1),
                 arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                 fontsize=10, color='black')

# Add additional textual information
for (x, country_data) in zip(years, co2_reductions):
    for (country, y) in zip(countries, country_data):
        plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=8)

# Title and labels
plt.title('Global CO2 Emission Reductions (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('CO2 Reduction (Billion Tons)', fontsize=14)
plt.xticks(years)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Countries', loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()