import matplotlib.pyplot as plt
import numpy as np

# Artwork Analysis: Most Popular Artistic Movements as Depicted in Museums Worldwide

# Define the artistic movements and corresponding number of museums showcasing them
art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Modernism', 'Contemporary']
museum_counts = [150, 100, 80, 120, 90, 60]

# Cumulative sums to determine the positions for each bar
cumulative_counts = np.cumsum(museum_counts)

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Color settings for each bar
colors = ['#FFD700', '#C0C0C0', '#D3A9A9', '#A2D9A2', '#87CEEB', '#800080']

# Create bars for artistic movements
bars = ax.bar(art_movements, museum_counts, color=colors, width=0.5, edgecolor='black')

# Annotate the bars with their respective values
for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        yval,
        f'{yval} Museums',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Add chart title and axis labels
ax.set_title(
    'Global Art Display Trends:\nPopular Artistic Movements in Museums Worldwide',
    fontsize=16, fontweight='bold'
)
ax.set_ylabel('Number of Museums', fontsize=12)
ax.set_xlabel('Art Movements', fontsize=12)

# Adjust x-ticks for better readability
plt.xticks(rotation=30, ha='right')

# Add a legend to explain the colors used for each bar
ax.legend(bars, art_movements, title='Art Movements', title_fontsize='13', loc='upper right', fontsize='10')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5, axis='y')

# Automatic adjustment of subplot parameters for better layout
plt.tight_layout()

# Display the chart
plt.show()