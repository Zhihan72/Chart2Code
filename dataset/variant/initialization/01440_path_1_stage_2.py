import matplotlib.pyplot as plt

# Define the data for the architectural styles
styles = [
    'Mod', 'Class', 'ArtDeco', 'Gothic', 'Futur', 
    'Baroque', 'Renaiss', 'NeoClass', 'Minim', 
    'Brutal', 'Rom', 'Vict', 'Colon', 'Tudor'
]
percentages = [18.0, 14.0, 9.0, 8.0, 6.5, 6.0, 5.0, 5.0, 5.5, 
               6.0, 5.5, 4.5, 4.0, 3.5]

# Adjust the percentages to ensure they sum to 100
total = sum(percentages)
correction = 100 - total
percentages[-1] += correction

colors = plt.cm.viridis([
    0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 
    0.15, 0.25, 0.35, 0.45, 0.55
])

explode = tuple(0.1 if p >= 10 else 0 for p in percentages)

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=styles,
    autopct=lambda pct: f'{pct:.1f}%',
    startangle=140,
    colors=colors,
    explode=explode
)

plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

# Concise title
ax.set_title(
    'Arch Styles in Architectura City (2020s)',
    fontsize=14,
    fontweight='bold'
)

ax.legend(
    wedges,
    styles,
    title='Styles',
    loc='upper left',
    bbox_to_anchor=(1, 1)
)

plt.tight_layout()
plt.show()