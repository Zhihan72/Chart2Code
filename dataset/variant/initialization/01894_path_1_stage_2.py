import matplotlib.pyplot as plt
import numpy as np

# Energy sources and their corresponding usage percentages
energy_sources = ['Wind', 'Fossil Fuels', 'Solar', 'Geothermal', 'Fusion', 'Hydrogen']
energy_usage = np.array([15, 10, 25, 10, 20, 20])

# Colors for each section of the pie chart
colors = ['#4682B4', '#D2691E', '#FFD700', '#32CD32', '#FF6347', '#9400D3']

# Explode the first and second slice
explode = (0, 0, 0.1, 0, 0.1, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=190,
    colors=colors,
    explode=explode,
    shadow=True
)

# Customize text size and style
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10, weight='bold')

# Title for the chart
plt.title(
    'Interstellar Power Distribution:\nCosmic Probe into Energy Capacities by 2077',
    fontsize=16, weight='bold', pad=20
)

# Legend
ax.legend(
    wedges, energy_sources, title="Power Origins",
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()