import matplotlib.pyplot as plt

# Data
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
contributions = [35, 25, 20, 10, 10]

# Colors for each segment
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
    wedgeprops=dict(edgecolor='gray', linewidth=3, linestyle='--', width=0.25),  # Changed linestyle
    explode=[0.15 if x == 'Wind' else 0 for x in energy_sources],  # Changed exploded segment
    shadow=False,  # Removed shadow for a flat style
    textprops={'fontsize': 11, 'color': 'blue'}  # Changed font color
)

# Aspect ratio
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=11, color='darkred', weight='bold')  # Changed text style
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

# Disable automatic adjustment for a slightly more compact layout
# plt.tight_layout()

# Display the donut chart
plt.show()