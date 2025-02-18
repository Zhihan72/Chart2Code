import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
devices = ['Smartphones', 'Tablets', 'Laptops', 'Smart TVs', 'Wearables', 'Gaming Consoles', 'E-Readers']
usage_percentage = [35, 15, 25, 10, 8, 7, 5]
colors = ['#66b3ff', '#c0c0c0', '#ff6666', '#99ff99', '#ffcc99', '#ff9999', '#9966ff']
explode = (0.1, 0, 0, 0, 0, 0.1, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    usage_percentage,
    labels=devices,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    wedgeprops=dict(edgecolor='white', linewidth=2),
    pctdistance=0.85
)

# Draw a circle at the center to make a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

ax.set_title("TechVille Device Usage Share:\nDistribution of Smart Devices Among Residents", fontsize=16, fontweight='bold', pad=20)

# Customize the text on the wedges
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12)

ax.text(
    0, 0, 
    'Smart Device\nUsage\n2023', 
    ha='center', va='center', 
    fontsize=12, color='black', weight='bold'
)

# Add a legend outside the chart
ax.legend(
    wedges, devices,
    title="Devices", 
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()