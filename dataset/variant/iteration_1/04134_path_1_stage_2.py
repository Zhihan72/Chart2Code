import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

deforestation = np.array([15, 14.8, 14.5, 14.1, 13.8, 13.6, 13.5, 13.2, 13.0, 12.8, 12.5, 12.5, 12.3, 12.0, 11.8, 11.5, 11.3, 11.0, 10.8, 10.5, 10.3])
reforestation = np.array([1, 1.2, 1.5, 1.8, 2.0, 2.3, 2.6, 3.0, 3.3, 3.7, 4.1, 4.5, 5.0, 5.5, 6.0, 6.5, 7.1, 7.6, 8.2, 8.8, 9.5])

initial_forest_coverage = 100
net_deforestation = deforestation - reforestation
forest_coverage = initial_forest_coverage - np.cumsum(net_deforestation)

data_stack = np.vstack([deforestation, reforestation])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data_stack, labels=['Deforestation', 'Reforestation'], colors=['#8B4513', '#2E8B57'], alpha=0.6)

ax2 = ax.twinx()
ax2.plot(years, forest_coverage, label='Total Forest Coverage', color='darkorange', linestyle='--', linewidth=3, marker='o')

ax.set_title("Global Forest Coverage (2000-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Area (Million Hectares)', fontsize=14)
ax2.set_ylabel('Remaining Forest Coverage (Million Hectares)', fontsize=14, color='darkorange')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.grid(visible=True, which='major', linestyle='-', linewidth=0.7, color='lightgray', alpha=0.9)

ax.legend(loc='lower left', title='Activities')
ax2.legend(loc='lower right')

ax.annotate('Global Efforts Intensify', xy=(2010, 3.7), xytext=(2006, 11),
            arrowprops=dict(facecolor='red', arrowstyle='->', linewidth=1.5), fontsize=11, backgroundcolor='w')

plt.tight_layout()
plt.show()