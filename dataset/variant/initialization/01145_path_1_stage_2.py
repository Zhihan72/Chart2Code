import matplotlib.pyplot as plt

# Define data
groups = ['Sumerians', 'Egyptians', 'Aztecs', 'Incas', 'Romans']
wonders_count = [10, 15, 7, 4, 20]

# Shuffled colors
colors = ['#ffcc99', '#c2c2f0', '#66b3ff', '#ff9999', '#99ff99']

# Explode the slice for better emphasis
explode = (0.1, 0.1, 0, 0, 0.1)

# Create the pie chart with 'donut' effect
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    wonders_count,
    labels=groups,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=160,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Draw a circle to create the 'donut' effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title
plt.title(
    'Mystical Constructs Across Continents:\nLegacy of Forgotten Eras',
    fontsize=14,
    fontweight='bold',
    color='navy',
    pad=20
)

# Enhance visual appearance
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10, weight='bold')

# Add a legend
ax.legend(
    wedges, groups,
    title="Cultures",
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10,
    frameon=False
)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()