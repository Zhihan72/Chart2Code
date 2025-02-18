import matplotlib.pyplot as plt

# Data
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
contributions = [35, 25, 20, 10, 10]

# Shuffled colors for each segment
colors = ['#99ff99', '#ffb3e6', '#ff6666', '#66b3ff', '#ffcc00']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='gray', linestyle='--', linewidth=1.5),
    explode=[0.1 if x == 'Solar' else 0 for x in energy_sources],
    shadow=False,
    textprops={'fontsize': 10, 'family': 'serif'}
)

# Remove equal aspect ratio
ax.axis('auto')

# Customize text appearance
plt.setp(autotexts, size=10, weight='bold', color='blue')
plt.setp(texts, size=10, style='italic')

# Add title
plt.title(
    "Renewable Energy Contribution (2023)",
    fontsize=14, weight='bold', color='darkgreen', pad=15
)

# Modify legend position and appearance
ax.legend(
    wedges, energy_sources,
    title="Sources",
    loc="upper right",
    fontsize=9,
    frameon=False
)

# Added grid for stylistic purposes
plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5, color='gray')

# Automatically adjust subplot parameters
plt.tight_layout()

# Display the pie chart
plt.show()