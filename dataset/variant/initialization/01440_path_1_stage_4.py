import matplotlib.pyplot as plt

styles = [
    'Mod', 'Class', 'ArtDeco', 'Gothic', 'Futur',
    'Baroque', 'Renaiss', 'NeoClass', 'Minim',
    'Brutal', 'Rom', 'Vict', 'Colon', 'Tudor'
]
percentages = [18.0, 14.0, 9.0, 8.0, 6.5, 6.0, 5.0, 5.0, 5.5, 
               6.0, 5.5, 4.5, 4.0, 3.5]

# Correct percentages to sum to 100
total = sum(percentages)
correction = 100 - total
percentages[-1] += correction

# Change colors for visual variation
colors = plt.cm.plasma([
    0.9, 0.1, 0.5, 0.7, 0.2, 0.8, 0.3, 0.4, 0.6,
    0.65, 0.55, 0.35, 0.45, 0.75
])

explode = tuple(0.05 if p >= 8 else 0 for p in percentages)

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=styles,
    autopct=lambda pct: f'{pct:.1f}%',
    startangle=50,
    colors=colors,
    explode=explode,
    shadow=True
)

# Alter stylistic elements of text
plt.setp(autotexts, size=9, weight='normal', color='black')
plt.setp(texts, size=9)

ax.set_title(
    'Architectural Styles Distribution',
    fontsize=16,
    fontweight='light',
    style='italic'
)

# Modify legend properties
ax.legend(
    wedges,
    styles,
    title='Styles',
    loc='center left',
    bbox_to_anchor=(-0.1, 0.5),
    frameon=False,  # Remove border from legend
    markerscale=0.8
)

plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()