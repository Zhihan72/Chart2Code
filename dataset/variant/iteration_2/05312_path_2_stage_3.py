import matplotlib.pyplot as plt

creatures = ['Dragon', 'Elf', 'Troll', 'Fairy', 'Human']

scores = {
    'Dragon': [95, 85, 90, 92, 85],
    'Elf': [70, 95, 80, 60, 90],
    'Troll': [80, 60, 75, 85, 50],
    'Fairy': [60, 85, 95, 70, 90],
    'Human': [75, 80, 70, 75, 85]
}

box_plot_data = [scores[creature] for creature in creatures]

fig, ax = plt.subplots(figsize=(14, 8))

uniform_color = 'blue'
boxprops = dict(linestyle='--', linewidth=1.5, color=uniform_color, facecolor='lightyellow')
medianprops = dict(linestyle='-', linewidth=2, color=uniform_color)
whiskerprops = dict(linestyle=':', linewidth=1.2, color=uniform_color)
capprops = dict(linestyle='-.', linewidth=2, color=uniform_color)

ax.boxplot(box_plot_data, labels=creatures, patch_artist=True, vert=False,
           boxprops=boxprops, medianprops=medianprops,
           whiskerprops=whiskerprops, capprops=capprops,
           flierprops=dict(marker='^', color='red', markersize=7, alpha=0.7),
           notch=True)

ax.set_title("Mystic World Survey: Attributes Score of Magical Creatures", fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Attribute Score (0-100)', fontsize=12)
ax.set_ylabel('Magical Creatures', fontsize=12)
ax.grid(axis='x', linestyle='-.', alpha=0.5)

ax.annotate('Highest Vitality', xy=(scores['Dragon'][3], 1), xytext=(scores['Dragon'][3] + 5, 1.2),
            arrowprops=dict(facecolor='black', arrowstyle='-|>'), fontsize=10, color='purple')
ax.annotate('Exceptional Charisma', xy=(scores['Elf'][4], 2), xytext=(scores['Elf'][4] + 5, 2.2),
            arrowprops=dict(facecolor='black', arrowstyle='-|>'), fontsize=10, color='red')

plt.tight_layout()
plt.show()