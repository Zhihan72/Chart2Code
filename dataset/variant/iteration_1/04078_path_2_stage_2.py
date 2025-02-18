import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Emissions data
co2_emissions = np.array([7000, 9000, 11000, 13000, 15000, 16000])
ch4_emissions = np.array([1500, 1700, 1800, 1900, 2000, 2100])
n2o_emissions = np.array([300, 350, 400, 450, 500, 550])
fgases_emissions = np.array([50, 100, 150, 200, 250, 300])

emissions_data = np.vstack([co2_emissions, ch4_emissions, n2o_emissions, fgases_emissions])
new_colors = ['#377eb8', '#4daf4a', '#984ea3', '#ff7f00']  # New color set

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(decades, emissions_data, labels=['CO2', 'CH4', 'N2O', 'F-gases'], colors=new_colors, alpha=0.85)
ax.set_title('GHG Emissions (1970-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('MtCO2e', fontsize=14)

ax.legend(title='Gas', loc='upper left', bbox_to_anchor=(1.05, 1))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45)

ax.annotate('Kyoto Protocol', xy=(2000, 14000), xytext=(2005, 17000),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

plt.tight_layout()
plt.show()