import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In Planet GreenEarth, a future self-sustained farming project is being launched. The project involves several zones dedicated to different types of crop cultivation. The pie chart illustrates the distribution of these cultivation zones.

# Data: Distribution of cultivation zones in acres
zones = ['Vegetables', 'Fruits', 'Grains', 'Legumes', 'Herbs', 'Flowers']
zone_acres = np.array([25, 20, 30, 15, 5, 5])

# Colors associated with each zone
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']

# Explode the 'Grains' slice for emphasis
explode = (0, 0, 0.1, 0, 0, 0)  # Emphasize the third slice (i.e., Grains)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    zone_acres, 
    explode=explode, 
    labels=zones, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85
)

# Format autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Draw a circle at the center of the pie chart to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')  

# Title for the pie chart
plt.title(
    'Future Farming on GreenEarth:\nDistribution of Cultivation Zones', 
    fontsize=16, 
    weight='bold', 
    pad=20
)

# Add a legend outside the chart
ax.legend(wedges, zones, title="Cultivation Zones", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to avoid text overlap
plt.tight_layout()

# Show the plot
plt.show()