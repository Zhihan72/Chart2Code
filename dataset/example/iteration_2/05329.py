import matplotlib.pyplot as plt
import numpy as np

# Let's imagine a fictional storyline where different civilizations in a fantasy world 
# have specialized in unique skills to survive. Each civilization has honed specific abilities 
# related to survival, such as Hunting, Gathering, Magic, Combat, Diplomacy, and Technology.

# Define the civilizations and their corresponding skills' values
civilizations = ['Elves', 'Dwarves', 'Humans', 'Orcs', 'Goblins']
attributes = ['Hunting', 'Gathering', 'Magic', 'Combat', 'Diplomacy', 'Technology']

elves = [7, 8, 10, 4, 9, 6]
dwarves = [5, 4, 6, 10, 8, 9]
humans = [6, 7, 5, 7, 10, 8]
orcs = [8, 3, 2, 10, 5, 4]
goblins = [6, 7, 3, 8, 4, 6]

data = np.array([elves, dwarves, humans, orcs, goblins])

# Number of attributes (spokes in the radar chart)
num_vars = len(attributes)

# Compute angle for each attribute on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
# The radar chart requires us to "close the loop" by appending the start to the end
angles += angles[:1]

# Append the first value to each civilization's data to close the radar chart's loop
data = np.concatenate((data, data[:, [0]]), axis=1)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
plt.title('Survival Skills of Fantasy Civilizations', size=18, weight='bold', pad=20, color='peru')

# Plot each civilization's data on the radar chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for idx, (label, color) in enumerate(zip(civilizations, colors)):
    ax.plot(angles, data[idx], linewidth=2, linestyle='solid', label=label, color=color)
    ax.fill(angles, data[idx], color=color, alpha=0.25)

# Customize the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=13, fontweight='bold', color='darkslategray')

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Civilizations')

# Ensure everything fits within the plot area
plt.tight_layout()

# Show the radar chart
plt.show()