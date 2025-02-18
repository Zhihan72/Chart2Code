import matplotlib.pyplot as plt
import numpy as np

# Define the fantasy creatures and attributes
creatures = ['Dragon', 'Elf', 'Orc', 'Wizard']
attributes = ['Strength', 'Intelligence', 'Agility', 'Magic Power', 'Stealth']

# Data for each creature as competency levels (scale of 1-10)
data = {
    'Dragon': [9, 7, 6, 10, 5],
    'Elf': [5, 8, 9, 6, 8],
    'Orc': [10, 5, 7, 3, 6],
    'Wizard': [4, 10, 5, 9, 7]
}

# Number of variables
num_vars = len(attributes)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Function to create radar charts
def radar_chart(ax, values, creature_name, color):
    values += values[:1]  # Complete the loop
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, color='grey', fontsize=12)
    ax.set_yticklabels([])

    ax.set_title(creature_name, size=15, color=color, pad=20)

# Colors for each creature
colors = ['#FF4500', '#32CD32', '#8B0000', '#1E90FF']

# Create the radar chart
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# Plot each creature
for ax, (creature, color) in zip(axs.flat, zip(creatures, colors)):
    radar_chart(ax, data[creature], creature, color)

# Add a super title
plt.suptitle("Fantasy Creatures' Competency Assessment Across Various Attributes", 
             fontsize=18, fontweight='bold', color='darkslateblue')

# Automatically adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the radar charts
plt.show()