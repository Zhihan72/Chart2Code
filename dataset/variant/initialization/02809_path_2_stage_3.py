import matplotlib.pyplot as plt
import numpy as np

# Data setup
libraries = ['Ancient Archives', 'Renaissance Repository', 'Modern Manuscript']
genres = ['Fiction', 'Non-Fiction', 'Poetry', 'Drama']
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
            color=new_colors, edgecolor='black', label=libraries[i] if i == 0 else "")

# Customize the axes
ax.set_yticks(np.arange(num_genres) + 0.2)
ax.set_yticklabels(genres, fontsize=10)
ax.set_xlim(0, 50)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_title('Literary Genre Distribution Across the Libraries of Time', fontsize=16, fontweight='bold')

# Add legend
ax.legend(title='Libraries', loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()