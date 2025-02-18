import matplotlib.pyplot as plt
import numpy as np

# Define the years when the construction takes place
years = ['2022', '2023', '2024', '2025', '2026']

# Components construction progress (in percentage for positive and negative diverging)
hull_progress = np.array([60, 70, 80, 90, 100]) - 60
engine_progress = np.array([50, 65, 75, 85, 95]) - 60
control_systems_progress = np.array([40, 55, 70, 85, 95]) - 60
living_quarters_progress = np.array([30, 50, 65, 80, 90]) - 60

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Colors for different components
colors = ['#4682B4', '#98FB98', '#FFA07A', '#8B0000']

# Plotting diverging bars from center
ax.barh(years, hull_progress, label='Hulls', color=colors[0], left=0, edgecolor='black')
ax.barh(years, engine_progress, label='Engines', color=colors[1], left=hull_progress, edgecolor='black')
ax.barh(years, control_systems_progress, label='Control Systems', color=colors[2], left=hull_progress + engine_progress, edgecolor='black')
ax.barh(years, living_quarters_progress, 
        label='Living Quarters', 
        color=colors[3], 
        left=hull_progress + engine_progress + control_systems_progress, 
        edgecolor='black')

# Adding titles and labels
ax.set_title('Diverging Construction Progress Overview (2022-2026)', fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel('Construction Progress Divergence from Avergage (%)', fontsize=12)
ax.set_ylabel('Year', fontsize=12)

# Add a custom legend
ax.legend(title='Components', loc='lower right', fontsize=11)

# Enable a grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set x-axis limits
ax.set_xlim(-60, 40)

# Better layout adjustment
plt.tight_layout()

# Display the plot
plt.show()