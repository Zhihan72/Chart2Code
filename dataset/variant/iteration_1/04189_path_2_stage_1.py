import matplotlib.pyplot as plt
import numpy as np

# Age Groups
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']

# Data inputs
ai_assistants = [120, 150, 130, 100, 60, 30]
smart_homes = [80, 140, 120, 110, 70, 40]
electric_vehicles = [50, 100, 110, 90, 50, 20]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Bar heights
height = 0.25

# Set the positions of the bars on the y-axis
bar1 = np.arange(len(age_groups))
bar2 = [y + height for y in bar1]
bar3 = [y + height for y in bar2]

# Plotting the horizontal bars
ax.barh(bar1, ai_assistants, height, label='AI Assistants', color='skyblue', edgecolor='black')
ax.barh(bar2, smart_homes, height, label='Smart Homes', color='lightgreen', edgecolor='black')
ax.barh(bar3, electric_vehicles, height, label='Electric Vehicles', color='lightcoral', edgecolor='black')

# Adding labels and title
ax.set_ylabel('Age Groups', fontsize=12, weight='bold')
ax.set_xlabel('Number of Adopters', fontsize=12, weight='bold')
ax.set_title('Tech Adoption in Different Age Groups for 2023', fontsize=14, weight='bold', pad=20)

# Customizing the y-axis values
ax.set_yticks([r + height for r in range(len(age_groups))])
ax.set_yticklabels(age_groups, fontsize=12)

# Adding value labels next to bars
def add_value_labels(y_positions, values):
    for y_pos, value in zip(y_positions, values):
        ax.text(value + 3, y_pos, str(value), va='center', color='black', fontsize=10)

add_value_labels(bar1, ai_assistants)
add_value_labels(bar2, smart_homes)
add_value_labels(bar3, electric_vehicles)

# Adding legend
ax.legend(title='Technologies', loc='upper right', fontsize=10)

# Add gridlines to x-axis for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Show plot with tight layout to avoid overlap
plt.tight_layout()
plt.show()