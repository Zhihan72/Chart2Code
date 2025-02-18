import matplotlib.pyplot as plt

# Data: Randomly changed the contributions while maintaining their nature
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
contributions = [30, 30, 15, 15, 10]

# Colors for each segment (kept unchanged for clarity)
colors = ['#66b3ff', '#ffcc00', '#ff6666', '#99ff99', '#ffb3e6']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(9, 7))

# Plot the donut chart
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=None,
    colors=colors,
    autopct='%1.1f%%',
    startangle=120,
    wedgeprops=dict(edgecolor='gray', linewidth=3, linestyle='--', width=0.25),
    explode=[0.15 if x == 'Geothermal' else 0 for x in energy_sources],
    shadow=False,
    textprops={'fontsize': 11, 'color': 'blue'}
)

# Aspect ratio
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=11, color='darkred', weight='bold')
plt.setp(texts, size=10)

# Add title
plt.title(
    "Energy Source Contributions (2023)",
    fontsize=17, color='purple', pad=15
)

# Add a legend inside the pie
ax.legend(
    wedges, energy_sources,
    title="Sources",
    loc="upper left",
    bbox_to_anchor=(0.1, 0.1),
    fontsize=9
)

# Display the donut chart
plt.show()