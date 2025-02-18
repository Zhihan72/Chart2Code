import matplotlib.pyplot as plt
import numpy as np

# The backstory: We are visualizing the yearly progress of an intergalactic spaceship construction project. Different components must be built and completed each year to keep the project on track. The types of components include Hulls, Engines, Control Systems, and Living Quarters.

# Define the years when the construction takes place
years = ['2022', '2023', '2024', '2025', '2026']

# Components construction progress (in percentage)
hull_progress = np.array([60, 70, 80, 90, 100])
engine_progress = np.array([50, 65, 75, 85, 95])
control_systems_progress = np.array([40, 55, 70, 85, 95])
living_quarters_progress = np.array([30, 50, 65, 80, 90])

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Colors for different components
colors = ['#8B0000', '#FFA07A', '#4682B4', '#98FB98']

# Plotting stacked bars
ax.bar(years, hull_progress, label='Hulls', color=colors[0], edgecolor='black')
ax.bar(years, engine_progress, bottom=hull_progress, label='Engines', color=colors[1], edgecolor='black')
ax.bar(years, control_systems_progress, bottom=hull_progress + engine_progress, label='Control Systems', color=colors[2], edgecolor='black')
ax.bar(years, living_quarters_progress, 
       bottom=hull_progress + engine_progress + control_systems_progress, 
       label='Living Quarters', 
       color=colors[3], 
       edgecolor='black')

# Adding titles and labels
ax.set_title('Intergalactic Spaceship Construction Progress (2022-2026)', fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Construction Progress (%)', fontsize=12)

# Add a custom legend
ax.legend(title='Components', loc='upper left', fontsize=11)

# Enable a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits
ax.set_ylim(0, 320)

# Better layout adjustment
plt.tight_layout()

# Display the plot
plt.show()