import matplotlib.pyplot as plt
import numpy as np

# Backstory and Context:
# We're presenting data on various renewable energy sources and their contribution to the global energy mix.
# This study compares the percentage of energy coming from different renewable sources in the year 2022.

# Data representing the global energy mix percentages for various renewable energy sources in 2022
energy_sources = ['Wind', 'Solar', 'Hydropower', 'Biomass', 'Geothermal', 'Other']
percentages = [27, 23, 18, 12, 8, 12]  # Percentages adding up to 100%

# Colors chosen to represent each renewable energy source
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Explode configuration to emphasize 'Wind' sector
explode = (0.1, 0, 0, 0, 0, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Add title and styling adjustments
ax.set_title(
    "Global Renewable Energy Mix in 2022",
    fontsize=18, fontweight='bold', pad=20
)
plt.setp(autotexts, size=12, weight='bold', color='white')
plt.setp(texts, size=12)

# Ensure the pie chart is a circle
ax.axis('equal')

# Create an inset bar chart showing renewable energy growth over the past decade
# Hypothetical data for the global increase in renewable energy usage from 2012 to 2022
years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]  # Data in percentage of total energy

# Create an inset axes at the specified position within the main chart
ax_inset = fig.add_axes([0.8, 0.1, 0.15, 0.3])
ax_inset.bar(years, growth, color='skyblue')
ax_inset.set_title("Renewable Energy Growth (2012-2022)", fontsize=10)
ax_inset.set_ylabel("Energy (%)", fontsize=8)
ax_inset.set_xlabel("Years", fontsize=8)
ax_inset.tick_params(axis='both', labelsize=8)

# Legend with additional spacing
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Adjust layout to fit everything neatly
plt.tight_layout()

# Show plot
plt.show()