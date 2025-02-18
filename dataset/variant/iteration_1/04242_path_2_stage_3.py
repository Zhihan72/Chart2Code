import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array(list(range(2013, 2023)))

# Heroic activities data
superaqua_activities = np.array([120, 130, 135, 142, 150, 160, 170, 175, 185, 200])
pyroman_activities = np.array([100, 105, 110, 115, 120, 125, 130, 140, 155, 165])
windwoman_activities = np.array([90, 92, 95, 97, 100, 105, 110, 115, 120, 130])

# Create the plot
plt.figure(figsize=(12, 6))

# Plot each superhero's activities with varied styles
plt.plot(years, superaqua_activities, marker='^', linestyle='-.', color='blue', linewidth=2.5, label='SuperAqua')
plt.plot(years, pyroman_activities, marker='v', linestyle='-', color='green', linewidth=1.5, label='PyroMan')
plt.plot(years, windwoman_activities, marker='d', linestyle='--', color='magenta', linewidth=3, label='WindWoman')

# Annotate data points
for (x, y) in zip(years, superaqua_activities):
    plt.text(x, y + 2, f'{y}', color='blue', fontsize=10, ha='center')

for (x, y) in zip(years, pyroman_activities):
    plt.text(x, y + 2, f'{y}', color='green', fontsize=10, ha='center')

for (x, y) in zip(years, windwoman_activities):
    plt.text(x, y + 2, f'{y}', color='magenta', fontsize=10, ha='center')

# Title and labels
plt.title('Evolution of Superhero Activity Levels\n(2013-2022)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Incidents Handled', fontsize=12)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(range(0, 251, 25))

# Modify the legend
plt.legend(title='Superheroes', fontsize=10, loc='lower right', borderaxespad=0.5, frameon=False)

# Remove grid lines
plt.grid(False)

# Customize border
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.5)
    spine.set_color('gray')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()