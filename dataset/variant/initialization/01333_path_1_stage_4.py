import matplotlib.pyplot as plt

bordeaux_yields = [13, 16, 15, 18, 14, 20, 16, 19, 17, 18, 15, 19, 20, 18]
napa_valley_yields = [21, 23, 22, 24, 23, 26, 25, 24, 27, 26, 25, 28, 29, 27]
tuscany_yields = [12, 14, 13, 16, 15, 17, 14, 16, 15, 17, 16, 18, 17, 18]
rioja_yields = [11, 13, 12, 15, 12, 14, 13, 15, 14, 16, 13, 17, 15, 16]
marlborough_yields = [16, 18, 17, 19, 18, 20, 17, 19, 18, 21, 20, 22, 19, 21]
barossa_valley_yields = [14, 15, 14, 17, 15, 18, 14, 18, 16, 19, 17, 20, 18, 17]

yield_data = [
    bordeaux_yields,
    napa_valley_yields,
    tuscany_yields,
    rioja_yields,
    marlborough_yields,
    barossa_valley_yields
]

regions = ['Bordeaux', 'Napa Valley', 'Tuscany', 'Rioja', 'Marlborough', 'Barossa Valley']

colors = ['lightgreen', 'lightcoral', 'lightblue', 'lightyellow', 'lightcyan', 'lightsalmon']

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

# Assign different face colors for each region's box
ax[0].boxplot(yield_data, patch_artist=True, notch=False, vert=True,
              boxprops=dict(facecolor='white', color='navy', linewidth=2),
              whiskerprops=dict(color='navy', linewidth=2),
              capprops=dict(color='navy', linewidth=2),
              medianprops=dict(color='orange', linewidth=3),
              flierprops=dict(marker='s', color='navy', alpha=0.8))

for patch, color in zip(ax[0].artists, colors):
    patch.set_facecolor(color)

ax[0].set_title('Distribution of Harvest Yields in Wine Regions\n(2010-2023)', fontsize=16, fontweight='bold', pad=20)
ax[0].set_xlabel('Wine Regions', fontsize=12)
ax[0].set_ylabel('Grape Yields (Tons)', fontsize=12)
ax[0].set_xticklabels(regions, rotation=45, ha='right')
ax[0].grid(axis='y', linestyle='-', alpha=0.9)

years = list(range(2010, 2024))
average_yields_per_year = [
    sum(yields) / len(yields) for yields in zip(*yield_data)
]

ax[1].plot(years, average_yields_per_year, marker='x', color='crimson', linestyle='--', linewidth=2.5, label='Avg Yields')
ax[1].set_title('Average Grape Yields Over Time', fontsize=13, fontweight='bold', pad=12)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Avg Yields (Tons)', fontsize=12)
ax[1].set_xticks(years)
ax[1].legend(loc='upper left', frameon=False)
ax[1].grid(linestyle=':', alpha=0.8)

plt.tight_layout()
plt.show()