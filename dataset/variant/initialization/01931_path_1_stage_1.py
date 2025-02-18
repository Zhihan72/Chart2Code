import matplotlib.pyplot as plt
import numpy as np

# Fictional worlds and their corresponding number of languages
worlds = ['Middle-earth', 'Westeros', 'Star Wars Galaxy', 'Star Trek Universe', 'Harry Potter World', 'Narnia', 'Discworld']
languages = [12, 8, 21, 12, 6, 7, 10]

# Horizontal bar colors for each world
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0']

# Sorting the data by number of languages in descending order
sorted_indices = np.argsort(languages)[::-1]
sorted_worlds = [worlds[i] for i in sorted_indices]
sorted_languages = [languages[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
ax.barh(sorted_worlds, sorted_languages, color=sorted_colors, edgecolor='black')

# Add data labels at the end of each bar
for i, value in enumerate(sorted_languages):
    ax.text(value + 0.5, i, f'{value}', va='center', fontsize=10, fontweight='bold', color='black')

# Customize plot appearance
ax.set_xlabel('Number of Languages', fontsize=12, weight='bold')
ax.set_ylabel('Fictional Worlds', fontsize=12, weight='bold')
ax.set_title('Linguistic Diversity in Popular Fictional Worlds', fontsize=16, fontweight='bold', ha='center')
ax.set_xlim(0, max(sorted_languages) + 5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Enhance the y-axis labels
ax.set_yticklabels(sorted_worlds, fontsize=11, weight='bold', color='navy')

# Optional: Adding a legend
legend_labels = ['Number of Languages']
ax.legend(legend_labels, loc='upper right', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()