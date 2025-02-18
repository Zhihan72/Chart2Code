import matplotlib.pyplot as plt
import numpy as np

# Data
hobbies = ['Reading', 'Gaming', 'Exercising', 'Cooking', 'Traveling']
hours_spent = np.array([5, 15, 7, 10, 12])
happiness_levels = np.array([70, 50, 85, 75, 90])

# New set of color values for each hobby
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFC300']

# Create Scatter Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot with modified colors
scatter = ax.scatter(hours_spent, happiness_levels, c=colors, s=250, edgecolor='w', marker='d')

# Annotating the points
for i, hobby in enumerate(hobbies):
    ax.annotate(hobby, (hours_spent[i], happiness_levels[i]), textcoords="offset points", xytext=(10, -10), ha='right', fontsize=10, fontweight='normal')

# Adding a best fit line
m, b = np.polyfit(hours_spent, happiness_levels, 1)
ax.plot(hours_spent, m*hours_spent + b, color='orange', linewidth=1.5, linestyle='-', label='Trend Line')

# Title and Labels
ax.set_title('Hobbies and Happiness Correlation', fontsize=18, fontweight='normal', pad=10)
ax.set_xlabel('Avg. Hours/Week', fontsize=12)
ax.set_ylabel('Happiness Score', fontsize=12)

# Adding color bar (not necessary anymore since colors are not tied to a colormap)
# ax.grid(True, linestyle=':', alpha=0.5)

# Enhance visibility
plt.tight_layout()

# Show the plot
plt.show()