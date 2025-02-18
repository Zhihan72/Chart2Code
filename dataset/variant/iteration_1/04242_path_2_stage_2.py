import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array(list(range(2013, 2023)))

# Heroic activities data (in number of incidents handled)
superaqua_activities = np.array([120, 130, 135, 142, 150, 160, 170, 175, 185, 200])
pyroman_activities = np.array([100, 105, 110, 115, 120, 125, 130, 140, 155, 165])
windwoman_activities = np.array([90, 92, 95, 97, 100, 105, 110, 115, 120, 130])

# Create the plot
plt.figure(figsize=(12, 6))

# Plot each superhero's activities excluding EarthGuardian
plt.plot(years, superaqua_activities, marker='o', linestyle='-', color='cyan', linewidth=2, label='SuperAqua')
plt.plot(years, pyroman_activities, marker='s', linestyle='--', color='orange', linewidth=2, label='PyroMan')
plt.plot(years, windwoman_activities, marker='x', linestyle=':', color='pink', linewidth=2, label='WindWoman')

# Annotate data points for clarity
for (x, y) in zip(years, superaqua_activities):
    plt.text(x, y + 2, f'{y}', color='cyan', fontsize=8, ha='center')

for (x, y) in zip(years, pyroman_activities):
    plt.text(x, y + 2, f'{y}', color='orange', fontsize=8, ha='center')

for (x, y) in zip(years, windwoman_activities):
    plt.text(x, y + 2, f'{y}', color='pink', fontsize=8, ha='center')

# Title and labels
plt.title('Evolution of Superhero Activity Levels\n(2013-2022)', fontsize=14, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Incidents Handled', fontsize=12)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(range(0, 251, 25))

# Add a legend
plt.legend(title='Superheroes', fontsize=10, loc='upper left')

# Grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()