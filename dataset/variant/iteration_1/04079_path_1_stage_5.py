import matplotlib.pyplot as plt

# Data
energy_sources = ['Wind', 'Solar', 'Hydro', 'Biomass', 'Geothermal']  # Randomly changed order
contributions = [30, 30, 15, 10, 15]  # Match the altered order

# Single color for all segments
single_color = ['#66b3ff']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(9, 7))

# Plot the donut chart
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=None,
    colors=single_color * len(contributions),
    autopct='%1.1f%%',
    startangle=150,  # Changed the start angle to a new random value
    wedgeprops=dict(edgecolor='gray', linewidth=3, linestyle='--', width=0.25),
    explode=[0.15 if x == 'Biomass' else 0 for x in energy_sources],  # Changed exploded segment
    shadow=False,
    textprops={'fontsize': 12, 'color': 'green'}  # Changed some text properties
)

# Aspect ratio
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=12, color='navy', weight='bold')  # Changed color
plt.setp(texts, size=11)  # Changed text size

# Add title
plt.title(
    "Contribution by Energy Types (2023)",  # Modified title text
    fontsize=18, color='orange', pad=15  # Changed some title properties
)

# Add a legend inside the pie
ax.legend(
    wedges, energy_sources,
    title="Energy Types",  # Modified legend title text
    loc="upper left",
    bbox_to_anchor=(0.1, 0.1),
    fontsize=10  # Changed font size
)

# Display the donut chart
plt.show()