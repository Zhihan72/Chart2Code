import matplotlib.pyplot as plt
import numpy as np

# Define backstory details
# Title: "Solar System Missions Achievements"
# This bar chart will present the number of significant scientific discoveries made by various space missions 
# to different planets and celestial bodies in our solar system over recent decades.

# Define the missions and number of discoveries made
missions = ["Voyager", "Galileo", "Cassini", "New Horizons", "Pioneer", "Rosetta", "Juno", "Crewed Missions"]
discoveries = [15, 22, 30, 10, 18, 8, 13, 6]

# Define the years when these missions were active for line plot demonstration
years_active = np.array([1977, 1989, 1997, 2006, 1973, 2004, 2011, 1961])
discoveries_per_year = np.array(discoveries) / np.array(
    [40, 10, 20, 15, 12, 12, 10, 60])

# Create the figure and primary Bar chart subplot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the bar chart for discoveries
bars = ax1.bar(missions, discoveries, color='skyblue', edgecolor='k')

# Adding title and labels
ax1.set_xlabel("Space Missions", fontsize=14)
ax1.set_ylabel("Number of Discoveries", fontsize=14)
ax1.set_title("Solar System Missions Achievements", fontsize=16, fontweight='bold')

# Adding value labels above bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height),
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# Creating a secondary Y-axis to plot the years active and discoveries per year
ax2 = ax1.twinx()
ax2.plot(missions, discoveries_per_year, color='darkorange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Discoveries per Year')
ax2.set_ylabel('Discoveries per Year', fontsize=14, color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

# Adding a legend for the line plot
ax2.legend(loc='upper right')

# Annotate significant missions to highlight certain accomplishments
annotations = {
    "Voyager": "Interstellar\nMission",
    "Galileo": "Jupiter\nSystem",
    "Cassini": "Saturn\nSystem",
    "New Horizons": "Pluto & Beyond"
}

for mission, label in annotations.items():
    idx = missions.index(mission)
    ax1.annotate(label, (missions[idx], discoveries[idx]), xytext=(0, 10), textcoords='offset points', 
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 ha='center', fontsize=10, color='maroon')

# Improve layout and presentation
plt.tight_layout()

# Show the plot
plt.show()