import matplotlib.pyplot as plt

# Manually altered data for grape yields in tons (shuffled within each group)
bordeaux_yields = [18, 14, 16, 13, 19, 15, 20, 18, 16, 17, 19, 13, 15, 18]
napa_valley_yields = [23, 24, 25, 21, 27, 23, 26, 28, 22, 24, 29, 25, 27, 26]
tuscany_yields = [14, 17, 16, 12, 17, 13, 15, 16, 18, 14, 15, 12, 18, 13]
rioja_yields = [13, 15, 16, 11, 17, 12, 14, 15, 16, 13, 12, 14, 11, 15]
marlborough_yields = [18, 21, 22, 16, 19, 17, 20, 18, 19, 21, 17, 20, 18, 19]
barossa_valley_yields = [15, 18, 14, 19, 17, 14, 18, 15, 17, 14, 18, 16, 20, 17]
piedmont_yields = [15, 18, 12, 16, 17, 15, 16, 15, 18, 17, 14, 17, 19, 12]

yield_data = [
    bordeaux_yields,
    napa_valley_yields,
    tuscany_yields,
    rioja_yields,
    marlborough_yields,
    barossa_valley_yields,
    piedmont_yields
]

regions = ['Bordeaux', 'Napa Valley', 'Tuscany', 'Rioja', 'Marlborough', 'Barossa Valley', 'Piedmont']

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

ax[0].boxplot(yield_data, patch_artist=True, notch=True,
              boxprops=dict(facecolor='lightgreen', color='darkgreen', linewidth=1.5),
              whiskerprops=dict(color='darkgreen', linewidth=1.5),
              capprops=dict(color='darkgreen', linewidth=1.5),
              medianprops=dict(color='red', linewidth=2),
              flierprops=dict(marker='o', color='darkgreen', alpha=0.5))

ax[0].set_title('Annual Distribution of Harvest Yields in Various Wine Regions\n(2010-2023)', fontsize=14, fontweight='bold', pad=15)
ax[0].set_xlabel('Wine Regions', fontsize=12)
ax[0].set_ylabel('Grape Yields (Tons)', fontsize=12)
ax[0].set_xticklabels(regions, rotation=15)
ax[0].grid(axis='y', linestyle='--', alpha=0.6)

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