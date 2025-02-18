import matplotlib.pyplot as plt
import numpy as np

# Retreat locations and data
retreats = ['Mars V.', 'Jup. H.', 'Ven. O.', 'Sat. R.', 'Nep. S.']
intellectual_diversity = np.array([80, 60, 70, 85, 55])

# Sort the data
sorted_indices = np.argsort(intellectual_diversity)
retreats_sorted = [retreats[i] for i in sorted_indices]
intellectual_diversity_sorted = intellectual_diversity[sorted_indices]

# Create a bar chart with sorted intellectual diversity
plt.figure(figsize=(10, 6))
plt.barh(retreats_sorted, intellectual_diversity_sorted, color='dodgerblue')

# Adding labels and title
plt.title("Intellectual Diversity at Writers' Retreats", fontsize=14, fontweight='bold')
plt.xlabel('Intellectual Diversity', fontsize=12)
plt.ylabel('Retreat Locations', fontsize=12)

# Enhance visual style
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()