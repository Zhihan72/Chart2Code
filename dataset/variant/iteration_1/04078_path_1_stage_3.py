import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

co2_emissions = np.array([7000, 9000, 11000, 13000, 15000, 16000])
ch4_emissions = np.array([1500, 1700, 1800, 1900, 2000, 2100])
n2o_emissions = np.array([300, 350, 400, 450, 500, 550])
fgases_emissions = np.array([50, 100, 150, 200, 250, 300])

emissions_data = np.vstack([co2_emissions, ch4_emissions, n2o_emissions, fgases_emissions])

# Altered colors and added line alpha parameters for stylistic variations
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']  # Different colors

fig, ax = plt.subplots(figsize=(12, 8))

# Added different hatch patterns
ax.stackplot(decades, emissions_data, colors=colors, alpha=0.85, 
             edgecolor='black', linewidth=0.5, hatch='/')
ax.yaxis.grid(True, linestyle='-', alpha=0.4)  # Changed grid style

# Altered x-ticks for extended readability
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=30)

# Altered border/axis lines for stylistic variations
ax.spines['top'].set_color('none')  # Removed top border
ax.spines['right'].set_color('none')  # Removed right border
ax.spines['left'].set_linestyle('--')
ax.spines['bottom'].set_linestyle('--')

# Added different marker type manually without utilizing any function
years = decades
ax.plot(years, co2_emissions, linestyle='--', marker='o', color='black', label='CO2 Emissions')
ax.plot(years, ch4_emissions, linestyle='-.', marker='s', color='grey', label='CH4 Emissions')
ax.plot(years, n2o_emissions, linestyle=':', marker='^', color='brown', label='N2O Emissions')
ax.plot(years, fgases_emissions, linestyle='-', marker='d', color='green', label='FGases Emissions')

# Changing the position and number of legends
ax.legend(loc='upper left', ncol=2, bbox_to_anchor=(0, -0.1))

plt.tight_layout()
plt.show()