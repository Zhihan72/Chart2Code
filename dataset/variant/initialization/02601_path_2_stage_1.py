import matplotlib.pyplot as plt
import numpy as np

# Data for planetary exploration missions
celestial_bodies = ['Saturn', 'Comets', 'Jupiter', 'Mercury', 'Venus', 'Mars', 'Moon']
missions_count = [12, 10, 15, 8, 40, 55, 65]

# Define color palette
colors = ['#33FF57', '#AF33FF', '#75FF33', '#33FFF5', '#FFBD33', '#FF5733', '#335BFF']

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the sorted bar chart
bars = ax.bar(celestial_bodies, missions_count, color=colors, edgecolor='black', width=0.6)

# Annotate each bar with the mission count
for bar, count in zip(bars, missions_count):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, str(count), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Titles and labels
ax.set_title('Exploratory Missions Across the Solar System\nEarth\'s Focus on Celestial Bodies as of 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Celestial Bodies', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Missions', fontsize=12, labelpad=10)

# Customize x-axis labels
ax.set_xticks(np.arange(len(celestial_bodies)))
ax.set_xticklabels(celestial_bodies, rotation=45, ha='right')

# Set limits and grid
ax.set_ylim(0, 70)
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()