import matplotlib.pyplot as plt

# Data
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
contributions = [35, 25, 20, 10, 10]

# Colors for each segment
colors = ['#ffcc00', '#66b3ff', '#99ff99', '#ffb3e6', '#ff6666']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the donut chart
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='white', linewidth=2, width=0.3),  # Reduced width for donut effect
    explode=[0.1 if x == 'Solar' else 0 for x in energy_sources],
    shadow=True,
    textprops={'fontsize': 12}
)

# Equal aspect ratio ensures the donut is drawn as a circle
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=12, weight='bold', color='black')
plt.setp(texts, size=12)

# Add title with line break for readability
plt.title(
    "Renewable Energy Breakdown:\nContribution to Total Energy Production (2023)",
    fontsize=16, weight='bold', color='darkblue', pad=20
)

# Add a legend outside the pie to describe each segment
ax.legend(
    wedges, energy_sources,
    title="Energy Sources",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

# Automatically adjust subplot parameters for a cleaner layout
plt.tight_layout()

# Display the donut chart
plt.show()