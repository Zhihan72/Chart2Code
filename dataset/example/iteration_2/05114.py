import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This plot visualizes the relationship between daily fluid intake and hydration levels among different age groups. 
# The study was conducted to understand how different age groups maintain hydration based on their daily fluid consumption.

# Creating artificial data based on the backstory
age_groups = ['Children', 'Teens', 'Adults', 'Seniors']
daily_fluid_intake_liters = {
    'Children': [1.0, 1.2, 1.1, 1.4, 1.3, 1.2, 1.1, 1.5, 1.2, 1.3, 1.4],
    'Teens': [1.8, 2.0, 1.9, 2.1, 2.2, 2.1, 2.3, 1.9, 2.0, 2.1, 2.2],
    'Adults': [2.5, 2.8, 2.7, 2.9, 3.0, 3.1, 3.0, 3.2, 2.8, 3.1, 3.0],
    'Seniors': [1.8, 1.9, 1.7, 1.6, 1.8, 1.7, 1.9, 1.8, 1.6, 1.7, 1.8]
}
hydration_levels = {
    'Children': [70, 75, 73, 80, 78, 75, 73, 82, 76, 79, 81],
    'Teens': [65, 68, 67, 70, 72, 71, 74, 66, 68, 70, 72],
    'Adults': [80, 83, 82, 85, 87, 88, 86, 90, 84, 87, 88],
    'Seniors': [65, 68, 67, 66, 65, 67, 70, 68, 66, 67, 69]
}

# Colors for different age groups
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

# Create the scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data for each age group
for age_group, color in zip(age_groups, colors):
    fluid_intake = daily_fluid_intake_liters[age_group]
    hydration = hydration_levels[age_group]
    ax.scatter(fluid_intake, hydration, color=color, alpha=0.7, edgecolors='black', linewidth=0.5, s=100, label=age_group)

# Title and labels
plt.title("Drink Up: How Different Age Groups Maintain Hydration\nBased on Daily Fluid Intake", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Daily Fluid Intake (Liters)", fontsize=14)
plt.ylabel("Hydration Levels (%)", fontsize=14)

# Customize ticks for better clarity
plt.xticks(np.arange(1.0, 3.5, 0.5))
plt.yticks(np.arange(60, 100, 5))

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Legends
plt.legend(title="Age Groups", fontsize=12, title_fontsize='13')

# Annotate specific observations
plt.annotate('High hydration in Adults', xy=(3.1, 88), xytext=(2.6, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black', fontweight='bold')

plt.annotate('Lower hydration in Teens', xy=(1.9, 66), xytext=(2.1, 62),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black', fontweight='bold')

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()