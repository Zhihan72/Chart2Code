import matplotlib.pyplot as plt

# Define data
groups = ['Sumerians', 'Egyptians', 'Aztecs', 'Incas', 'Romans']
wonders_count = [10, 15, 7, 4, 20]

# New color scheme
colors = ['#ff6699', '#99ccff', '#ffcc00', '#66ff66', '#ff6666']

# Explode the slice for better emphasis
explode = (0, 0.2, 0, 0, 0.1)

# Create the pie chart with 'donut' effect
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    wonders_count,
    labels=groups,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.75,
    wedgeprops=dict(width=0.3, linestyle='--', edgecolor='grey'),
    shadow=False
)

# Draw a circle to create the 'donut' effect
centre_circle = plt.Circle((0, 0), 0.70, fc='lightgrey')
fig.gca().add_artist(centre_circle)

# Title with updated styling
plt.title(
    'Mystical Constructs Legacy',
    fontsize=16,
    fontweight='regular',
    color='darkred',
    pad=15
)

# Enhance text appearance
plt.setp(autotexts, size=11, weight='bold', color='navy')
plt.setp(texts, size=11, weight='normal', color='darkgreen')

# Add a legend with box
ax.legend(
    wedges, groups,
    title="Cultures",
    loc='right',
    fontsize=9,
    frameon=True,
    fancybox=True,
    framealpha=0.5
)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()