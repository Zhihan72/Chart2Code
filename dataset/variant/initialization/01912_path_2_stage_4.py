import matplotlib.pyplot as plt

decades = ['2000s', '2010s', '2020s', '2030s', '2040s']
discoveries = [60, 80, 45, 30, 15]
breakthroughs = [
    "Black Hole Img",
    "Interstellar Obj",
    "Exoplanet Atm",
    "Grav Waves",
    "Ast Mining"
]
breakthrough_years = ['2019', '2047', '2004', '2015', '2035']
missions = [10, 20, 35, 55, 75]

fig, ax = plt.subplots(figsize=(14, 8))

# Change marker types and line styles
ax.plot(decades, discoveries, marker='^', linestyle='-.', color='forestgreen', linewidth=2, label='Discov', markersize=8)
ax.plot(decades, missions, marker='x', linestyle=':', color='crimson', linewidth=2, label='Missions', markersize=8)

# Alter grid style
ax.grid(True, linestyle='-.', color='navy', alpha=0.7)

for i, txt in enumerate(breakthroughs):
    ax.annotate(
        f'{txt} ({breakthrough_years[i]})',
        xy=(decades[i], discoveries[i]),
        xytext=(0, 10 if i % 2 == 0 else -30),
        textcoords='offset points',
        arrowprops=dict(facecolor='darkred', arrowstyle='->', lw=0.8),
        fontsize=9,
        ha='center',
        bbox=dict(boxstyle="round,pad=0.3", edgecolor='darkblue', facecolor='lavender', alpha=0.8)
    )

ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Num of Discov/Missions', fontsize=12, labelpad=10)
ax.set_title('Astronomy: Discoveries & Missions', fontsize=16, pad=20)

# Modify legend style
ax.legend(loc='upper right', fontsize=10, frameon=True, shadow=False, fancybox=False)
ax.set_facecolor('aliceblue')
plt.tight_layout()
plt.show()