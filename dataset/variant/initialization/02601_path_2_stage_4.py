import matplotlib.pyplot as plt
import numpy as np

# Updated data for planetary missions
bodies = ['Saturn', 'Jupiter', 'Mercury', 'Venus', 'Mars', 'Moon']
counts = [12, 15, 8, 40, 55, 65]

# Updated color palette for bars
new_colors = ['#3498db', '#2ecc71', '#f1c40f', '#9b59b6', '#34495e', '#16a085']

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bar chart
bars = ax.bar(bodies, counts, color=new_colors, edgecolor='black', width=0.6)

# Annotate each bar
for bar, count in zip(bars, counts):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, str(count), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Titles and labels
ax.set_title('Exploratory Missions in Solar System', fontsize=16, fontweight='bold')
ax.set_xlabel('Bodies', fontsize=12, labelpad=10)
ax.set_ylabel('No. of Missions', fontsize=12, labelpad=10)

# Customize x-axis labels
ax.set_xticks(np.arange(len(bodies)))
ax.set_xticklabels(bodies, rotation=45, ha='right')

# Set limits and grid
ax.set_ylim(0, 70)
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()