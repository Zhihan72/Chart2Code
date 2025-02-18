import matplotlib.pyplot as plt
import numpy as np

# Define data for ancient civilizations
civilizations = ['Egyptian Empire', 'Roman Empire', 'Greek City-States', 'Persian Empire', 'Chinese Han Dynasty', 'Indus Valley Civilization']

# Influence scale (0-100) for horizontal bar chart
influence = np.array([85, 95, 70, 90, 88, 65])

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(civilizations))

# Create horizontal bars
ax.barh(y_pos, influence, color='yellow', alpha=0.7)

# Customize the axes and title
ax.set_yticks(y_pos)
ax.set_yticklabels(civilizations)
ax.set_xlabel('Influence (0-100)', fontsize=12)
ax.set_title('Influence of Ancient Civilizations', fontsize=14, fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()