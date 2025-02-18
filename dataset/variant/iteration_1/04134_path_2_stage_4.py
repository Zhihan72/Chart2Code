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

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, data_stack, labels=['Deforestation', 'Reforestation', 'Afforest.'], colors=['#98df8a', '#d62728', '#9467bd'], alpha=0.8)

ax2 = ax.twinx()
ax2.plot(years, forest_coverage, label='Forest Cover', color='#ff9896', linestyle='--', linewidth=2.5, marker='o', markersize=6)

ax.set_title("Forest Change Analysis (2000-2020)", fontsize=16, fontweight='regular')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Area (millions of hectares)', fontsize=12)
ax2.set_ylabel('Forest Cover (millions of hectares)', fontsize=12, color='#ff9896')

ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=30, ha='right')
ax.grid(visible=True, which='major', linestyle='-', linewidth=0.7, color='blue', alpha=0.6)

ax.legend(loc='lower left', title='Categories')
ax2.legend(loc='lower right')

ax.annotate('Increased Efforts', xy=(2010, 3.7), xytext=(2003, 10),
            arrowprops=dict(facecolor='blue', arrowstyle='fancy', linewidth=1.5), fontsize=10, backgroundcolor='yellow')

plt.tight_layout()
plt.show()