import matplotlib.pyplot as plt
import numpy as np

# Backstory: Explore the Energy Consumption Breakdown in a Hypothetical Eco-Friendly Community in 2023
# The community focuses on different energy sources and intends to monitor their consumption.

# Define energy sources and their consumption percentages
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Others']
consumption_percentages = [35, 25, 15, 10, 10, 5]

# Colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the 'Solar' slice to emphasize it
explode = (0.1, 0, 0, 0, 0, 0)

# Create figure and axis for the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages, 
    explode=explode, 
    labels=energy_sources, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85,
    textprops={'fontsize': 12},
    shadow=True
)

# Draw a circle in the center of the pie chart to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie chart is drawn as a circle
ax.axis('equal')  

# Add a title with two lines
plt.title('Energy Consumption Breakdown in 2023\nEco-Friendly Community', fontsize=16, fontweight='bold', pad=20)

# Position legend to the right of the chart
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust the layout to make better space for the legend and other elements
plt.tight_layout()

# Display the chart
plt.show()