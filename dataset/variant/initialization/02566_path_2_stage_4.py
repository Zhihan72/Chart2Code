import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
parks = np.array([10, 15, 25, 35, 45, 55, 65, 75, 90, 100, 120])
gardens = np.array([5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60])
reserves = np.array([2, 4, 6, 10, 15, 20, 25, 30, 35, 40, 50])
urban_forests = np.array([1, 2, 3, 5, 7, 10, 15, 25, 30, 35, 40])

parks_cumulative = np.cumsum(parks)
gardens_cumulative = np.cumsum(gardens)
reserves_cumulative = np.cumsum(reserves)
urban_forests_cumulative = np.cumsum(urban_forests)

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, 
             parks_cumulative, 
             gardens_cumulative, 
             reserves_cumulative,
             urban_forests_cumulative,
             labels=['Community Gardens', 'Natural Reserves', 'Parks', 'Urban Forests'],
             colors=['#fc8d62', '#8da0cb', '#66c2a5', '#e78ac3'], alpha=0.8)

ax.set_title('A Decade of Greener Living: Urban Green Space Expansion\nEcoVille, 2020-2030', 
             fontsize=16, fontweight='bold', pad=20, style='italic')
ax.set_xlabel('Years', fontsize=12, color='green')
ax.set_ylabel('Total Green Space Area (Hectares)', fontsize=12, color='purple', rotation=0, labelpad=40)
ax.legend(loc='upper right', title='Green Space Types', fontsize=10, fancybox=True, shadow=True)
ax.set_xticks(np.arange(2020, 2035, 2))
ax.set_xticklabels(np.arange(2020, 2035, 2), rotation=45, ha='right', fontsize=8, color='blue')
ax.grid(axis='both', linestyle='-.', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.annotate('Significant Growth\nin 2025', xy=(2025, 180), xytext=(2024, 450),
            arrowprops=dict(facecolor='red', arrowstyle='wedge'), fontsize=12, ha='center')

plt.tight_layout()
plt.show()