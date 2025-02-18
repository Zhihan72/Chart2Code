import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

co2_emissions = np.array([7000, 9000, 11000, 13000, 15000, 16000])
ch4_emissions = np.array([1500, 1700, 1800, 1900, 2000, 2100])
n2o_emissions = np.array([300, 350, 400, 450, 500, 550])

emissions_data = np.vstack([co2_emissions, ch4_emissions, n2o_emissions])

colors = ['#e41a1c', '#377eb8', '#4daf4a']  # Updated to match the remaining data series

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(decades, emissions_data, colors=colors, alpha=0.85, 
             edgecolor='black', linewidth=0.5, hatch='/')
ax.yaxis.grid(True, linestyle='-', alpha=0.4)

ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=30)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_linestyle('--')
ax.spines['bottom'].set_linestyle('--')

ax.plot(decades, co2_emissions, linestyle='--', marker='o', color='black', label='CO2 Emissions')
ax.plot(decades, ch4_emissions, linestyle='-.', marker='s', color='grey', label='CH4 Emissions')
ax.plot(decades, n2o_emissions, linestyle=':', marker='^', color='brown', label='N2O Emissions')

ax.legend(loc='upper left', ncol=2, bbox_to_anchor=(0, -0.1))

plt.tight_layout()
plt.show()