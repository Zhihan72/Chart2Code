import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

deforestation = np.array([15, 14.8, 14.5, 14.1, 13.8, 13.6, 13.5, 13.2, 13.0, 12.8, 12.5, 12.5, 12.3, 12.0, 11.8, 11.5, 11.3, 11.0, 10.8, 10.5, 10.3])
reforestation = np.array([1, 1.2, 1.5, 1.8, 2.0, 2.3, 2.6, 3.0, 3.3, 3.7, 4.1, 4.5, 5.0, 5.5, 6.0, 6.5, 7.1, 7.6, 8.2, 8.8, 9.5])
afforestation = np.array([0, 0.5, 0.5, 0.7, 0.9, 1.0, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 2.9, 3.0, 3.2, 3.5, 3.8, 4.0, 4.2, 4.6, 5.0])

net_deforestation = deforestation - (reforestation + afforestation)
initial_forest_coverage = 100
forest_coverage = initial_forest_coverage - np.cumsum(net_deforestation)

data_stack = np.vstack([deforestation, reforestation, afforestation])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data_stack, labels=['Deforestation', 'Reforestation', 'Afforest.'], colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.7)

ax2 = ax.twinx()
ax2.plot(years, forest_coverage, label='Forest Cover', color='#1f77b4', linestyle='-', linewidth=2)

ax.set_title("Forest Change (2000-20)", fontsize=18, fontweight='bold')
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('Area (M ha)', fontsize=14)
ax2.set_ylabel('Cover (M ha)', fontsize=14, color='#1f77b4')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax.minorticks_on()
ax.grid(visible=True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)

ax.legend(loc='upper left', title='Data')
ax2.legend(loc='upper right')

ax.annotate('More Efforts', xy=(2010, 3.7), xytext=(2005, 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, backgroundcolor='w')

plt.tight_layout()
plt.show()