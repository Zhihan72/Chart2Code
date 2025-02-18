import matplotlib.pyplot as plt

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

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

consistent_color = 'teal'

# Create a horizontal boxplot
ax[0].boxplot(yield_data, patch_artist=True, notch=True, vert=False,
              boxprops=dict(facecolor=consistent_color, color=consistent_color, linewidth=1.5),
              whiskerprops=dict(color=consistent_color, linewidth=1.5),
              capprops=dict(color=consistent_color, linewidth=1.5),
              medianprops=dict(color='orange', linewidth=2.5),
              flierprops=dict(marker='+', color=consistent_color, alpha=0.7))

ax[0].grid(axis='x', linestyle='-.', alpha=0.8)

years = list(range(2010, 2024))
average_yields_per_year = [
    sum(yields) / len(yields) for yields in zip(*yield_data)
]

# Line plot with consistent color
ax[1].plot(years, average_yields_per_year, marker='x', color=consistent_color, linewidth=2.8, linestyle='-.')

ax[1].set_xticks(years)
ax[1].grid(linestyle=':', alpha=0.9)

plt.tight_layout()
plt.show()