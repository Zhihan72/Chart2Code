import matplotlib.pyplot as plt
import numpy as np

# Fictional worlds and their corresponding number of languages
worlds = ['Middle-earth', 'Westeros', 'Star Wars', 'Star Trek', 'Harry Potter', 'Narnia', 'Discworld']
languages = [12, 8, 21, 12, 6, 7, 10]

# Consistent color for all bars
single_color = '#4363d8'

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Create horizontal bars
ax.barh(worlds, languages, color=single_color, edgecolor='black')

# Add data labels at the end of each bar
for i, (value, world) in enumerate(zip(languages, worlds)):
    ax.text(value + 0.5, i, f'{value}', va='center', fontsize=10, fontweight='bold', color='black')

# Customize plot appearance
ax.set_xlabel('Languages', fontsize=12, weight='bold')
ax.set_ylabel('Worlds', fontsize=12, weight='bold')
ax.set_title('Linguistic Diversity', fontsize=16, fontweight='bold', ha='center')
ax.set_xlim(0, max(languages) + 5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Enhance the y-axis labels
ax.set_yticklabels(worlds, fontsize=11, weight='bold', color='navy')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()