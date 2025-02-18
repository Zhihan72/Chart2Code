import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A medieval tournament themed festival was held where different kingdoms competed in various events over the course of the month
# We will visualize the total victories each kingdom achieved in distinct categories (Jousting, Archery, Melee Combat, Strategy Games, Performance Arts)

# Kingdoms and events
kingdoms = ['Avalon', 'Eldoria', 'Valoria', 'Drakonia']
events = ['Jousting', 'Archery', 'Melee Combat', 'Strategy Games', 'Performance Arts']

# Data for victories in each event for the kingdoms (rows: kingdoms, columns: events)
victories = np.array([
    [10, 15, 5, 7, 12],   # Avalon
    [12, 8, 9, 10, 5],    # Eldoria
    [7, 14, 11, 8, 6],    # Valoria
    [9, 12, 10, 6, 10]    # Drakonia
])

# Colors map for each kingdom
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Setting up the figure and changing the structure to contain subplots
fig, ax = plt.subplots(figsize=(15, 9))

# Bar width
bar_width = 0.2

# Positions of bars on X-axis
indices = np.arange(len(events))

# Plotting bar by bar for each kingdom
for i, kingdom in enumerate(kingdoms):
    ax.bar(indices + i * bar_width, victories[i], bar_width, label=kingdom, color=colors[i])

# Adding labels and title
ax.set_xlabel('Festival Events', fontsize=14)
ax.set_ylabel('Number of Victories', fontsize=14)
ax.set_title('Medieval Tournament: Kingdoms\' Victories in Various Events', fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * (len(kingdoms)-1) / 2)
ax.set_xticklabels(events, fontsize=12)

# Adding a legend to the plot
ax.legend(title='Kingdoms', fontsize=12)

# Customizing the background grid
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate the bars with the victory numbers
for i in range(len(events)):
    for j in range(len(kingdoms)):
        ax.text(indices[i] + j * bar_width, victories[j][i] + 0.5, str(victories[j][i]), ha='center', va='bottom', fontsize=10, color='black')

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()