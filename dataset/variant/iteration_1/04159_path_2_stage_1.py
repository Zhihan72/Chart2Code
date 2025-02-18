import matplotlib.pyplot as plt
import numpy as np

# Artwork Analysis: Most Popular Artistic Movements as Depicted in Museums Worldwide

# Define the artistic movements and corresponding number of museums showcasing them
art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Modernism', 'Contemporary']
museum_counts = [150, 100, 80, 120, 90, 60]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Color settings for each bar
colors = ['#FFD700', '#C0C0C0', '#D3A9A9', '#A2D9A2', '#87CEEB', '#800080']

# Create horizontal bars for artistic movements
bars = ax.barh(art_movements, museum_counts, color=colors, edgecolor='black')

# Annotate the bars with their respective values
for bar in bars:
    xval = bar.get_width()
    ax.text(
        xval,
        bar.get_y() + bar.get_height()/2,
        f'{xval} Museums',
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold'
    )

# Add chart title and axis labels
ax.set_title(
    'Global Art Display Trends:\nPopular Artistic Movements in Museums Worldwide',
    fontsize=16, fontweight='bold'
)
ax.set_xlabel('Number of Museums', fontsize=12)
ax.set_ylabel('Art Movements', fontsize=12)

# Adjust y-ticks for better readability
plt.yticks(rotation=0)

# Add a legend to explain the colors used for each bar
ax.legend(bars, art_movements, title='Art Movements', title_fontsize='13', loc='lower right', fontsize='10')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5, axis='x')

# Automatic adjustment of subplot parameters for better layout
plt.tight_layout()

# Display the chart
plt.show()