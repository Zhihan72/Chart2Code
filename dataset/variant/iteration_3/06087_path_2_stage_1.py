import matplotlib.pyplot as plt
import numpy as np

# Caloric intake data (in kcal) for a single age group
children = [1600, 1700, 1800, 1750, 1650, 1550, 1800, 1900, 2000, 1700]

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the vertical box chart for a single group
bp = ax.boxplot(
    children, 
    vert=True, 
    patch_artist=True, 
    notch=True, 
    boxprops=dict(facecolor='#A0CBE8', color='#1F77B4'),
    whiskerprops=dict(color='#1F77B4'), 
    capprops=dict(color='#1F77B4'),
    medianprops=dict(color='red')
)

# Set titles and labels
ax.set_title('Caloric Intake of Children (6-12) for 2023', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Caloric Intake (kcal)', fontsize=12)
ax.set_xticks([1])
ax.set_xticklabels(['Children (6-12)'], fontsize=12)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()