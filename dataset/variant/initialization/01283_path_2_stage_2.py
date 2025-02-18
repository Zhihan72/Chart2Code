import matplotlib.pyplot as plt
import numpy as np

# Data representing communication latency times (in minutes) for different civilizations
# Split original data into three fictional groups for visualization

group_1 = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15, 13, 17]
group_2 = [25, 28, 30, 27, 22, 20, 24, 29, 26, 23, 28, 26]
group_3 = [5, 6, 7, 8, 7, 6, 5, 9, 10, 8, 9, 11]

# Plotting a vertical box plot
plt.figure(figsize=(8, 8))
plt.boxplot([group_1, group_2, group_3], vert=True, patch_artist=True,
            boxprops=dict(facecolor='skyblue', color='navy', linewidth=1.5),
            whiskerprops=dict(color='navy', linewidth=1.5),
            capprops=dict(color='navy', linewidth=1.5),
            medianprops=dict(color='firebrick', linewidth=2),
            flierprops=dict(marker='o', color='orange', markersize=6),
            notch=True)

# Adding titles and labels
plt.title('Galactic Messaging: Communication Latencies by Group', fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Latency Time (minutes)', fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=['Group 1', 'Group 2', 'Group 3'], fontsize=10)
plt.yticks(fontsize=10)

# Adding a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap and ensure clean appearance
plt.tight_layout()

# Display the plot
plt.show()