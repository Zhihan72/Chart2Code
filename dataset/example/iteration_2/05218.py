import matplotlib.pyplot as plt
import numpy as np

# Backstory: A fictional report on the fuel efficiency of different spacecraft models across various space missions
# aiming to highlight advancements in fuel technologies and efficiency improvements.

# Data representing spacecraft models and average fuel consumptions (in kg per mission)
spacecraft_models = ['Explorer-X1', 'Pioneer-3G', 'Voyager-A2', 'Titan-Z10', 'Aurora-F5']
fuel_efficiency_2020 = [1400, 1300, 1350, 1500, 1450]
fuel_efficiency_2021 = [1350, 1250, 1300, 1450, 1400]
fuel_efficiency_2022 = [1300, 1200, 1250, 1400, 1350]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot bar charts for each year
bar_width = 0.25
x = np.arange(len(spacecraft_models))

bars1 = ax1.bar(x - bar_width, fuel_efficiency_2020, bar_width, label='2020', color='skyblue')
bars2 = ax1.bar(x, fuel_efficiency_2021, bar_width, label='2021', color='lightgreen')
bars3 = ax1.bar(x + bar_width, fuel_efficiency_2022, bar_width, label='2022', color='salmon')

# Title and labels
ax1.set_title('Space Exploration Institute: Annual Fuel Efficiency by Spacecraft Model\n(2020-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Spacecraft Model', fontsize=12)
ax1.set_ylabel('Average Fuel Consumption (kg/mission)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(spacecraft_models, fontsize=11)
ax1.set_ylim(1000, 1600)

# Add data labels on top of each bar
def add_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 20, f'{yval}', ha='center', va='bottom', fontsize=10, color='black')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Legend
ax1.legend(loc='upper right', fontsize=10)

# Grid for better readability
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout to fit all elements
plt.tight_layout()

# Display the bar chart
plt.show()