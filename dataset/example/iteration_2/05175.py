import matplotlib.pyplot as plt
import numpy as np

# Topic: Distribution of Energy Sources in a Futuristic City (2050)
# Story: Presenting different energy sources used by the city to achieve a fully sustainable environment.

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Nuclear', 'Biomass']
energy_percentages = [40, 30, 12, 8, 6, 4]

# Colors representing each energy source
colors = ['#FFD700', '#1E90FF', '#00CED1', '#FF4500', '#9400D3', '#8B4513']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

# Creating the pie chart with a slight explosion for the 'Solar' slice to highlight it
explode = (0.1, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='black', linewidth=1.5),
    shadow=True
)

# Title with a narrative backstory
plt.title(
    "Energy Source Distribution in Futuristic City (2050):\n"
    "Striving for a Fully Sustainable Environment",
    fontsize=14, fontweight='bold', pad=20
)

# Customizing the appearance of the texts
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10, weight='bold')

# Adding a legend to the side
ax.legend(
    wedges, energy_sources,
    title="Energy Sources",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

# Adjusting layout to prevent overlap
plt.tight_layout()

# Displaying the chart
plt.show()