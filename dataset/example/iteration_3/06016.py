import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart depicts the device usage share in a tech-savvy town called "TechVille". 
# It shows the percentage distribution of various smart devices among residents and demonstrates the diversity in their tech preferences.

# Data for the chart
devices = ['Smartphones', 'Tablets', 'Laptops', 'Smart TVs', 'Wearables', 'Gaming Consoles']
usage_percentage = [35, 15, 25, 10, 8, 7]  # Device usage share in percentage
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c0c0c0']
explode = (0.1, 0, 0, 0, 0, 0.1)

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

# Draw a circle at the center of the pie to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Title with line breaks for better visibility
ax.set_title("TechVille Device Usage Share:\nDistribution of Smart Devices Among Residents", fontsize=16, fontweight='bold', pad=20)

# Customize the text on the wedges
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12)

# Add a central text inside the donut
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