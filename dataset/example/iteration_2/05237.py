import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Imagine a series of adventurous voyages undertaken by legendary sea captains. Each captain is evaluated based on their skills in different maritime areas. This radar chart compares their performances across various maritime skills to determine the ultimate sea captain of the 'Ocean Rovers' guild.

# Define the categories/skills for the radar chart
categories = ['Navigation', 'Combat Tactics', 'Resource Management', 'Weather Prediction', 'Team Leadership']
num_vars = len(categories)

# Data for each sea captain, values out of a score of 10
captain_blackbeard = [8, 9, 6, 7, 9]
captain_kidd = [7, 8, 8, 6, 7]
captain_teach = [9, 7, 9, 8, 8]
captain_morgan = [6, 8, 7, 9, 9]
captain_drake = [8, 9, 7, 8, 8]

# Extend the data to close the radar chart
captains = [captain_blackbeard, captain_kidd, captain_teach, captain_morgan, captain_drake]
for captain in captains:
    captain += captain[:1]

# Calculate the angles for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart with polar coordinates
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Define a function to plot data on the radar chart
def plot_radar(data, label, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, label=label, color=color, linewidth=2)

# Plot the data for each sea captain
plot_radar(captain_blackbeard, 'Captain Blackbeard', 'midnightblue')
plot_radar(captain_kidd, 'Captain Kidd', 'firebrick')
plot_radar(captain_teach, 'Captain Teach', 'forestgreen')
plot_radar(captain_morgan, 'Captain Morgan', 'goldenrod')
plot_radar(captain_drake, 'Captain Drake', 'darkorchid')

# Customize the chart
ax.set_yticklabels([])  # Remove y-axis labels for cleaner appearance
ax.set_xticks(angles[:-1])  # Position the category labels
ax.set_xticklabels(categories, fontsize=11, color='darkblue')  # Set category labels

# Add a title with styling
plt.title('Performance Analysis of Ocean Rovers Guild Captains\nAcross Key Maritime Skills', fontsize=16, fontweight='bold', pad=20, color='navy')

# Configure the legend and layout adjustments
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Sea Captains', title_fontsize='13', frameon=True, borderpad=1)
plt.tight_layout()  # Adjust layout to ensure everything fits nicely
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Add gridlines for better readability

# Display the radar chart
plt.show()