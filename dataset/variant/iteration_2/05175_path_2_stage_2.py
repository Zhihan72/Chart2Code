import matplotlib.pyplot as plt

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Nuclear', 'Biomass']
energy_percentages = [40, 30, 12, 8, 6, 4]

# Colors for the energy sources
colors = ['#1E90FF', '#00CED1', '#8B4513', '#FFD700', '#9400D3', '#FF4500']

# Plotting the donut chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

# Creating the donut chart with a slight explosion for the 'Solar' slice to highlight it
explode = (0.1, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='black', linewidth=1.5, width=0.3),
    shadow=True
)

# Title
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

# Adjusting layout
plt.tight_layout()

# Displaying the chart
plt.show()