import matplotlib.pyplot as plt
import numpy as np

# Data setup
libraries = ['Eternal Tomes', 'Revival Archive', 'Contemporary Papers']
genres = ['Narrative', 'Factual', 'Verse', 'Script']
percentage_data = np.array([
    [40, 20, 30, 10],
    [35, 10, 25, 30],
    [20, 40, 20, 20],
])

# Define bar positions and colors
num_genres = len(genres)
new_colors = ['#8E44AD', '#2980B9', '#27AE60', '#E74C3C']

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot horizontal bars
for i in range(len(libraries)):
    ax.barh(np.arange(num_genres) + i*0.2, percentage_data[i], height=0.2, 
            color=new_colors, edgecolor='black')

# Customize the axes
ax.set_yticks(np.arange(num_genres) + 0.2)
ax.set_yticklabels(genres, fontsize=10)
ax.set_xlim(0, 50)
ax.set_xlabel('Proportion (%)', fontsize=12)
ax.set_title('Genre Allocation in Various Historical Archives', fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()