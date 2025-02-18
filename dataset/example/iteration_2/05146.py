import matplotlib.pyplot as plt
import numpy as np

# Backstory: Galactic Explorers have discovered various elements in different sectors of the galaxy. This chart represents the distribution of these elements.

# Define sectors and their respective proportions of discovered elements
sectors = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
elements_discovered = np.array([35, 20, 15, 18, 12])

# Define colors for each sector
colors = ['#1E90FF', '#FF69B4', '#32CD32', '#FFD700', '#8A2BE2']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    elements_discovered,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w'),
    explode=(0.1, 0, 0, 0, 0.2),  # Highlight Alpha and Epsilon sectors
    shadow=True
)

# Draw circle for donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Style labels
plt.setp(autotexts, size=12, weight="bold", color="black")
plt.setp(texts, size=12, color="darkblue")

# Add a legend outside the plot area
ax.legend(wedges, sectors, title="Galactic Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Title with backstory context
ax.set_title("Distribution of Elements in the Galaxy (2023)\nDiscoveries by Galactic Explorers", fontsize=16, fontweight='bold', color='royalblue', pad=20)

# Final adjustments to prevent label overlap and improve layout
plt.tight_layout()

# Show the plot
plt.show()