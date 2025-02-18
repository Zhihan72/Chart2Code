import matplotlib.pyplot as plt

efficiency_data = [
    75, 85, 80, 88, 90, 95, 93, 77, 82, 78,  # Solar
    60, 72, 68, 66, 74, 75, 73, 71, 70, 69,  # Wind
    85, 87, 90, 92, 88, 85, 89, 91, 86, 84,  # Hydroelectric
    55, 60, 58, 62, 59, 57, 61, 63, 64, 56,  # Biomass
    70, 72, 73, 78, 80, 75, 77, 76, 74, 71,  # Geothermal
]

fig, ax = plt.subplots(figsize=(8, 12))

bp = ax.boxplot(efficiency_data, vert=True, patch_artist=True, notch=True, showmeans=True,
                meanline=True, meanprops=dict(linestyle='-', linewidth=2.5, color='blue'))

# Apply a single color consistently across the box plot
single_color = '#FFC300'
bp['boxes'][0].set(facecolor=single_color, alpha=0.6)

for element in ['whiskers', 'caps', 'medians']:
    plt.setp(bp[element], color=single_color, linewidth=2)

ax.set_title('Global Renewable Energy Efficiency Evaluation', fontsize=16, fontweight='bold')
ax.set_ylabel('Efficiency Score (%)', fontsize=13)
ax.set_xticklabels(['Renewable Energy'], fontsize=12)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_ylim(50, 100)

plt.tight_layout()
plt.show()