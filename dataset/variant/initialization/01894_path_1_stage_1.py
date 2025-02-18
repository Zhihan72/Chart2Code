import matplotlib.pyplot as plt
import numpy as np

# Energy sources and their corresponding usage percentages
energy_sources = ['Solar', 'Fusion', 'Wind', 'Geothermal', 'Hydrogen', 'Fossil Fuels']
energy_usage = np.array([25, 20, 15, 10, 20, 10])

# Colors for each section of the pie chart
colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9400D3', '#D2691E']

# Explode the first and second slice
explode = (0.1, 0.1, 0, 0, 0, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the standard pie chart
wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True
)

# Customize text size and style
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10, weight='bold')

# Title for the chart
plt.title(
    'Galactic Energy Consumption:\nA Stellar Analysis of Energy Resources in 2050',
    fontsize=16, weight='bold', pad=20
)

# Legend
ax.legend(
    wedges, energy_sources, title="Energy Sources",
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()