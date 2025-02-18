import matplotlib.pyplot as plt
import numpy as np

# Data:
hobbies = ['Exercise', 'Cook', 'Read', 'Travel', 'Game']
hours_spent = np.array([5, 15, 7, 10, 12])  # Average hours spent per week
happiness_levels = np.array([70, 50, 85, 75, 90])

# Create Scatter Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot for hours spent and happiness levels
scatter = ax.scatter(hours_spent, happiness_levels, c=happiness_levels, cmap='coolwarm', s=300, edgecolor='k')

# Annotating the points
for i, hobby in enumerate(hobbies):
    ax.annotate(hobby, (hours_spent[i], happiness_levels[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, fontweight='bold')

# Adding a best fit line
m, b = np.polyfit(hours_spent, happiness_levels, 1)
ax.plot(hours_spent, m*hours_spent + b, color='gray', linewidth=2, linestyle='--', label='Trend Line')

# Titles and Labels
ax.set_title('Exploring Happiness Vs. Hobby Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hours per Week Engaged', fontsize=14)
ax.set_ylabel('Happiness (max 100)', fontsize=14)

# Adding color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Joyfulness Scale', fontsize=12)

# Grid and Legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='lower right', fontsize=12)

plt.tight_layout()

# Show the plot
plt.show()