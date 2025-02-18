import matplotlib.pyplot as plt

# Data
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
contributions = [35, 25, 20, 10, 10]

# Colors for each segment
colors = ['#ffcc00', '#66b3ff', '#99ff99', '#ffb3e6', '#ff6666']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,  # Changed start angle
    wedgeprops=dict(edgecolor='gray', linestyle='--', linewidth=1.5),  # Changed border style
    explode=[0.1 if x == 'Solar' else 0 for x in energy_sources],
    shadow=False,  # Removed the shadow for a cleaner look
    textprops={'fontsize': 10, 'family': 'serif'}  # Changed text properties
)

# Remove equal aspect ratio to distort the circle slightly
ax.axis('auto')

# Customize text appearance
plt.setp(autotexts, size=10, weight='bold', color='blue')  # Changed color to blue
plt.setp(texts, size=10, style='italic')  # Italicized text labels

# Add title
plt.title(
    "Renewable Energy Contribution (2023)",
    fontsize=14, weight='bold', color='darkgreen', pad=15  # Altered color and padding
)

# Modify legend position and appearance
ax.legend(
    wedges, energy_sources,
    title="Sources",
    loc="upper right",  # Changed legend location
    fontsize=9,
    frameon=False  # Removed frame around legend
)

# Added grid for stylistic purposes
plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5, color='gray')

# Automatically adjust subplot parameters for a cleaner layout
plt.tight_layout()

# Display the pie chart
plt.show()