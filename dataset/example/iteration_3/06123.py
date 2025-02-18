import matplotlib.pyplot as plt
import numpy as np

# Backstory: In recent years, the world has seen an unprecedented rise in technology startups innovating across various sectors. This chart presents the distribution of technology startups by their primary focus areas in 2023.
focus_areas = ['Artificial Intelligence', 'Fintech', 'HealthTech', 'EdTech', 'Blockchain', 'IoT', 'Cybersecurity']
percentages = [25, 20, 18, 15, 12, 7, 3]  # Hypothetical percentage distribution

# Define colors for each segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C71585', '#7B68EE']

# Customizing the pie chart
fig, ax = plt.subplots(figsize=(10, 8))

# Explode the segments slightly for emphasis
explode = (0.05, 0.05, 0, 0, 0, 0, 0)

# Plotting the pie chart with some segments exploded
wedges, texts, autotexts = ax.pie(percentages, labels=focus_areas, autopct='%1.1f%%',
                                  startangle=140, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'), explode=explode, shadow=True)

# Draw the circle for the donut hole
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Title of the chart
ax.set_title("Technology Startups by Focus Area in 2023", fontsize=16, fontweight='bold', pad=20)

# Adding a legend
ax.legend(wedges, focus_areas, title="Focus Areas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Customize the autotexts to enhance readability
for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()