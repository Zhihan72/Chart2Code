import matplotlib.pyplot as plt

# Modified data for the pie chart
energy_sources = ['Hydropower', 'Biomass', 'Solar', 'Wind', 'Geothermal']
energy_shares = [20, 10, 35, 30, 5]  # Same percentage shares with shuffled order

# Colors for each energy source
colors = ['#4682B4', '#8B4513', '#FFD700', '#87CEEB', '#556B2F']

# Explode the second largest segment (Wind) instead of the largest for emphasis
explode = (0, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(
    energy_shares, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=100, 
    colors=colors, 
    explode=explode, 
    shadow=True
)

# Enhance text properties
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

# Randomized chart title
ax.set_title(
    'Energy Division of Renewables\nfor 2023', 
    fontsize=16, 
    fontweight='bold', 
    pad=30
)

# Ensure the pie chart is a perfect circle
ax.axis('equal')

# Place the legend outside the pie chart with altered title
plt.legend(
    wedges, energy_sources,
    title="Source Categories",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=12
)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()