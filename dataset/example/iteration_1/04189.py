import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking Tech Adoption in Different Age Groups
# The dataset represents the number of people in different age groups 
# who have adopted three major technologies: AI Assistants, Smart Homes, and Electric Vehicles.

# Age Groups
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']

# Data inputs
ai_assistants = [120, 150, 130, 100, 60, 30]
smart_homes = [80, 140, 120, 110, 70, 40]
electric_vehicles = [50, 100, 110, 90, 50, 20]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Bar widths
width = 0.25

# Set the positions of the bars on the x-axis
bar1 = np.arange(len(age_groups))
bar2 = [x + width for x in bar1]
bar3 = [x + width for x in bar2]

# Plotting the bars
ax.bar(bar1, ai_assistants, width, label='AI Assistants', color='skyblue', edgecolor='black')
ax.bar(bar2, smart_homes, width, label='Smart Homes', color='lightgreen', edgecolor='black')
ax.bar(bar3, electric_vehicles, width, label='Electric Vehicles', color='lightcoral', edgecolor='black')

# Adding labels and title
ax.set_xlabel('Age Groups', fontsize=12, weight='bold')
ax.set_ylabel('Number of Adopters', fontsize=12, weight='bold')
ax.set_title('Tech Adoption in Different Age Groups for 2023', fontsize=14, weight='bold', pad=20)

# Customizing the x-axis values
ax.set_xticks([r + width for r in range(len(age_groups))])
ax.set_xticklabels(age_groups, fontsize=12)

# Adding value labels on top of bars
def add_value_labels(bars, values):
    for bar, value in zip(bars, values):
        ax.text(bar, value + 3, str(value), ha='center', color='black', fontsize=10)

add_value_labels(bar1, ai_assistants)
add_value_labels(bar2, smart_homes)
add_value_labels(bar3, electric_vehicles)

# Adding legend
ax.legend(title='Technologies', loc='upper right', fontsize=10)

# Add gridlines to y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Show plot with tight layout to avoid overlap
plt.tight_layout()
plt.show()