import matplotlib.pyplot as plt
import numpy as np

# Retreat locations
retreats = ['Mars V.', 'Jup. H.', 'Ven. O.', 'Sat. R.', 'Nep. S.']

# Data: intellectual diversity, environmental diversity, creative output, number of attendees
intellectual_diversity = np.array([80, 60, 70, 85, 55])
environmental_diversity = np.array([75, 50, 90, 65, 80])
creative_output = np.array([88, 65, 92, 78, 70])
attendees = np.array([120, 90, 150, 110, 95])

# Normalize bubble size for better visualization
bubble_size = attendees / np.max(attendees) * 500

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
scatter = ax.scatter(intellectual_diversity, environmental_diversity, creative_output, 
                     s=bubble_size, c='dodgerblue', alpha=0.8, edgecolors='w')

# Adding labels and titles
ax.set_title('Writers\' Retreats', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Intellectual Div.', fontsize=12, labelpad=10)
ax.set_ylabel('Environmental Div.', fontsize=12, labelpad=10)
ax.set_zlabel('Creative Out.', fontsize=12, labelpad=10)

# Annotate each retreat with its name
for i, retreat in enumerate(retreats):
    ax.text(intellectual_diversity[i], environmental_diversity[i], creative_output[i],
            retreat, fontsize=10, ha='right')

# Enhance visual style
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
ax.view_init(elev=30, azim=45)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()