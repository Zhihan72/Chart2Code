import matplotlib.pyplot as plt
import numpy as np

# Define the missions and number of discoveries made
missions = ["Voyager", "Galileo", "Cassini", "New Horizons", "Rosetta", "Juno", "Crewed Missions"]
discoveries = [15, 22, 30, 10, 8, 13, 6]

# Define the years when these missions were active for line plot demonstration
discoveries_per_year = np.array(discoveries) / np.array(
    [40, 10, 20, 15, 12, 10, 60])

# Create the figure and primary Bar chart subplot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the horizontal bar chart for discoveries with a consistent color
bars = ax1.barh(missions, discoveries, color='steelblue', edgecolor='k')

# Adding value labels next to bars
for bar in bars:
    width = bar.get_width()
    ax1.text(width, bar.get_y() + bar.get_height() / 2.0, '%d' % int(width),
             va='center', ha='left', fontsize=10, fontweight='bold')

# Creating a secondary X-axis to plot the years active and discoveries per year
ax2 = ax1.twiny()
ax2.plot(discoveries_per_year, missions, color='steelblue', marker='o', linestyle='-', linewidth=2, markersize=8, label='Discoveries per Year')
ax2.set_xlabel('Discoveries per Year', fontsize=14, color='steelblue')
ax2.tick_params(axis='x', labelcolor='steelblue')

# Adding a legend for the line plot
ax2.legend(loc='lower right')

# Annotate significant missions to highlight certain accomplishments
annotations = {
    "Voyager": "Interstellar\nMission",
    "Galileo": "Jupiter\nSystem",
    "Cassini": "Saturn\nSystem",
    "New Horizons": "Pluto & Beyond"
}

for mission, label in annotations.items():
    idx = missions.index(mission)
    ax1.annotate(label, (discoveries[idx], missions[idx]), xytext=(10, 0), textcoords='offset points', 
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 va='center', fontsize=10, color='maroon')

# Improve layout and presentation
plt.tight_layout()

# Show the plot
plt.show()