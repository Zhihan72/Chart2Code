import matplotlib.pyplot as plt
import numpy as np

stages = ["Idea", "Prototype", "Alpha", "Beta", "Launch", "Success"]
projects = np.array([500, 300, 200, 100, 50, 30])
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e4']

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))

# Randomize borders and grid lines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', color='gray')
ax.xaxis.grid(False)

ax.set_title('Innovation Funnel', fontsize=14, style='italic', pad=25)  # Change Title Style

# Removed axis visibility control

# Adjust layout
plt.tight_layout()

categories = ['Soft', 'Hard', 'Service', 'Hybrid']
category_counts = [250, 150, 75, 25]
pie_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

fig2, ax2 = plt.subplots(figsize=(8, 8))

# Randomize slice styling and labels
ax2.pie(category_counts, labels=[None]*len(categories), colors=pie_colors, autopct='%1.1f%%',
        startangle=100, wedgeprops={'edgecolor': 'navy', 'linestyle': '-', 'width': 0.4})

ax2.set_title('Idea Categories', fontsize=14, style='italic', pad=15)  # Change Title Style

# Modified legend to be outside the pie chart
ax2.legend(categories, loc='upper left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()