import matplotlib.pyplot as plt
import numpy as np

# Missions and their corresponding votes (in thousands)
missions = [
    'Moon Landing - Apollo 11',
    'Mars Rover - Curiosity',
    'International Space Station (ISS)',
    'Voyager Probes',
    'Hubble Space Telescope',
    'SpaceX Falcon 9 Launch',
    'Rosetta Comet Mission',
    'New Horizons Pluto Flyby',
    'Galileo Jupiter Mission',
    'James Webb Space Telescope',
    'Imaginary Mission - Alpha Centauri',
    'Fictional Endeavor - Andromeda Galaxy'
]

# Number of votes in thousands
votes = np.array([850, 760, 900, 650, 715, 680, 620, 690, 640, 780, 500, 450])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Choosing a color palette for the missions
colors = plt.cm.viridis(np.linspace(0, 1, len(missions)))

# Plot horizontal bar chart
bars = ax.barh(missions, votes, color=colors, edgecolor='black', height=0.6)

# Set title and labels
ax.set_title("Global Popularity of Space Exploration Missions\n(Votes in Thousands)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Votes (Thousands)', fontsize=12)
ax.set_ylabel('Missions', fontsize=12)

# Add value labels on each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width}', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

# Customize y-axis: invert and align ticks with bar centers
ax.invert_yaxis()

# Add horizontal grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

# Make a subplot with a pie chart demonstrating the distribution of missions by type
fig.subplots_adjust(right=0.7)
ax2 = fig.add_axes([0.75, 0.2, 0.25, 0.6])

# Defining mission types and their corresponding counts
types = ['Manned', 'Unmanned']
counts = [1, 11]  # Updated for additional unmanned missions

# Plot pie chart
ax2.pie(counts, labels=types, colors=['#1f77b4', '#ff7f0e'], autopct='%1.1f%%', startangle=90, counterclock=False)

# Set title for subplot
ax2.set_title('Mission Types Distribution', fontsize=12)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()