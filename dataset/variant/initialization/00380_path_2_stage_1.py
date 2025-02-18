import matplotlib.pyplot as plt
import numpy as np

# Data for exoplanets
exoplanet_names = ['Kepler-452b', 'Proxima Centauri b', 'TRAPPIST-1d', 'LHS 1140b', 'GJ 667 Cc', 'HD 40307 g']
potential_habitability = [200, 250, 150, 180, 300, 270]  # Aggregate habitability index

# Plot data
fig, ax = plt.subplots(figsize=(10, 6))

# Create a horizontal bar chart
bars = ax.barh(exoplanet_names, potential_habitability, color='skyblue', edgecolor='w', alpha=0.7)

# Add title and labels
ax.set_title("Potential Habitability of Exoplanets", fontsize=16, fontweight='bold')
ax.set_xlabel("Potential Habitability Index", fontsize=12)

# Add numerical labels to the right of each bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # 3 points horizontal offset
                textcoords="offset points",
                va='center', ha='left', fontsize=9)

# Display the plot
plt.tight_layout()
plt.show()