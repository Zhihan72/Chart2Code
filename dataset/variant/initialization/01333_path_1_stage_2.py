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

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

ax[0].boxplot(yield_data, patch_artist=True, notch=True, vert=False,
              boxprops=dict(facecolor='lightgreen', color='darkgreen', linewidth=1.5),
              whiskerprops=dict(color='darkgreen', linewidth=1.5),
              capprops=dict(color='darkgreen', linewidth=1.5),
              medianprops=dict(color='red', linewidth=2),
              flierprops=dict(marker='o', color='darkgreen', alpha=0.5))

ax[0].set_title('Annual Distribution of Harvest Yields in Various Wine Regions\n(2010-2023)', fontsize=14, fontweight='bold', pad=15)
ax[0].set_xlabel('Grape Yields (Tons)', fontsize=12)
ax[0].set_ylabel('Wine Regions', fontsize=12)
ax[0].set_yticklabels(regions)
ax[0].grid(axis='x', linestyle='--', alpha=0.6)

years = list(range(2010, 2024))
average_yields_per_year = [
    sum(yields) / len(yields) for yields in zip(*yield_data)
]

ax[1].plot(years, average_yields_per_year, marker='o', color='darkblue', linewidth=2, label='Average Yields')
ax[1].set_title('Average Grape Yields Over the Years', fontsize=12, fontweight='bold', pad=10)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Average Grape Yields (Tons)', fontsize=12)
ax[1].set_xticks(years)
ax[1].legend()
ax[1].grid(linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()