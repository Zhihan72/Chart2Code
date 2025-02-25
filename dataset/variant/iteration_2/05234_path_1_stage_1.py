import matplotlib.pyplot as plt
import numpy as np

# Data:
hobbies = ['Reading', 'Gaming', 'Exercising', 'Cooking', 'Traveling']
hours_spent = np.array([5, 15, 7, 10, 12])
happiness_levels = np.array([70, 50, 85, 75, 90])

# Create Scatter Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot with modified markers and styles
scatter = ax.scatter(hours_spent, happiness_levels, c=happiness_levels, cmap='viridis', s=250, edgecolor='w', marker='d')

# Annotating the points with different offset
for i, hobby in enumerate(hobbies):
    ax.annotate(hobby, (hours_spent[i], happiness_levels[i]), textcoords="offset points", xytext=(10,-10), ha='right', fontsize=10, fontweight='normal')

# Adding a best fit line with a different style
m, b = np.polyfit(hours_spent, happiness_levels, 1)
ax.plot(hours_spent, m*hours_spent + b, color='orange', linewidth=1.5, linestyle='-', label='Trend Line')

# Title and Labels with different font sizes and styles
ax.set_title('Hobbies and Happiness Correlation', fontsize=18, fontweight='normal', pad=10)
ax.set_xlabel('Avg. Hours/Week', fontsize=12)
ax.set_ylabel('Happiness Score', fontsize=12)

# Adding color bar with altered label size
cbar = plt.colorbar(scatter)
cbar.set_label('Happiness Score', fontsize=10)

# Modified grid style and removed legend
ax.grid(True, linestyle=':', alpha=0.5)

# Enhance visibility
plt.tight_layout()

# Show the plot
plt.show()