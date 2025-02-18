import matplotlib.pyplot as plt
import numpy as np

# Backstory: We will create a radar chart to compare the affinity levels and compatibility of different cuisines based on various sensory attributes.

# Define the sensory attributes
attributes = ['Sweetness', 'Sourness', 'Saltiness', 'Bitterness', 'Umami', 'Aroma']

# Number of variables
num_vars = len(attributes)

# Define the data for different cuisines
cuisine_italian = [7, 3, 6, 2, 8, 9]
cuisine_japanese = [5, 7, 4, 3, 9, 8]
cuisine_indian = [8, 4, 9, 5, 7, 7]
cuisine_french = [6, 5, 5, 3, 7, 9]

# Complete the data loop by adding the first value again to each list
cuisine_italian += cuisine_italian[:1]
cuisine_japanese += cuisine_japanese[:1]
cuisine_indian += cuisine_indian[:1]
cuisine_french += cuisine_french[:1]

# Calculate the angle for each attribute
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Enhance the grid and axes visibility
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Draw one axis per variable and add labels
plt.xticks(angles[:-1], attributes, color='darkslategray', size=12)

# Draw y-axis labels and set limits
ax.set_yticklabels(["1", "3", "5", "7", "9"], color='grey', size=10)
ax.set_ylim(0, 10)

# Define color schemes and markers for cuisines
colors = ['#FF6347', '#4682B4', '#8FBC8B', '#DB7093']
markers = ['o', 's', '^', 'd']

# Define the cuisines and their data for looping
cuisines = [cuisine_italian, cuisine_japanese, cuisine_indian, cuisine_french]
cuisine_names = ['Italian', 'Japanese', 'Indian', 'French']

# Plot each cuisine data on the radar chart
for data, name, color, marker in zip(cuisines, cuisine_names, colors, markers):
    ax.plot(angles, data, linewidth=2, linestyle='-', label=name, color=color, marker=marker)
    ax.fill(angles, data, color=color, alpha=0.1)

# Title and legend
plt.title('Sensory Attributes of Various Cuisines', size=20, color='navy', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)

# Adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the radar chart
plt.show()