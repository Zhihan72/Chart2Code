import matplotlib.pyplot as plt
import numpy as np

# Combined delivery times for all platforms
combined_delivery_times = [2, 3, 5, 2, 3, 4, 5, 2, 3, 6, 2, 3, 4, 
                           4, 3, 5, 6, 4, 7, 3, 6, 4, 5, 7, 6, 8, 20, 
                           1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2, 
                           3, 5, 4, 6, 5, 3, 4, 5, 6, 4, 5, 7, 3, 4, 
                           6, 8, 7, 9, 8, 10, 7, 6, 7, 11, 12, 10]

# Create a vertical box plot
fig, ax = plt.subplots(figsize=(6, 8))
bplot = ax.boxplot(combined_delivery_times, vert=True, patch_artist=True, 
                   boxprops=dict(facecolor='skyblue', color='darkblue'),
                   whiskerprops=dict(color='darkblue'),
                   capprops=dict(color='darkblue'),
                   medianprops=dict(color='orange', linewidth=2),
                   flierprops=dict(marker='o', color='red', markersize=7))

# Set the labels and title
ax.set_title('Distribution of Delivery Times\nfor E-commerce Orders', 
             fontsize=16, fontweight='bold')
ax.set_ylabel('Delivery Time (Days)', fontsize=12)

# Gridlines for clarity
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()