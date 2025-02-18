import matplotlib.pyplot as plt
import numpy as np

# Programming languages and their popularity
languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]
orbis_popularity = [92, 72, 80, 85, 68]

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))
r = np.arange(len(languages))
ax.bar(r, xenon_popularity, color='b', edgecolor='grey', label='Xenon')
ax.bar(r, zephyr_popularity, color='g', edgecolor='grey', label='Zephyr', bottom=xenon_popularity)
ax.bar(r, orbis_popularity, color='m', edgecolor='grey', label='Orbis', bottom=np.array(xenon_popularity) + np.array(zephyr_popularity))

# Adding labels and title
ax.set_xlabel('Programming Languages', fontweight='bold', fontsize=12)
ax.set_ylabel('Popularity (%)', fontweight='bold', fontsize=12)
ax.set_title('Programming Language Popularity\nAcross Alien Planets', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(r)
ax.set_xticklabels(languages)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Rotate x-axis labels for readability
plt.xticks(rotation=30, ha='right')

# Adding a legend
plt.legend(title='Planets', loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()