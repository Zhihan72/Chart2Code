import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart represents the breakdown of energy consumption by different home appliances in an average household. 
# The other subplot shows the expected cost-saving from energy-efficient upgrades for each appliance type.

# Define appliances and their energy consumption in kilowatt-hours (kWh) per year
appliances = [
    'Refrigerator', 
    'Washing Machine', 
    'Dryer', 
    'Dishwasher', 
    'Oven', 
    'Microwave', 
    'Lighting', 
    'Television'
]
energy_consumption = [500, 275, 400, 300, 450, 100, 475, 250]  # kWh per year

# Expected annual cost-saving (in dollars) from energy-efficient upgrades
cost_saving = [75, 45, 60, 55, 70, 30, 80, 35]  # USD per year

# Colors for each appliance
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF4500', '#40E0D0', '#8A2BE2']

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot energy consumption as horizontal bar chart
bars1 = ax1.barh(appliances, energy_consumption, color=colors, edgecolor='black')

# Annotate the bars with energy consumption values
for bar, consumption in zip(bars1, energy_consumption):
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{consumption} kWh', va='center', ha='left', fontsize=12, color='black')

# Set the title and labels for the first subplot
ax1.set_title('Annual Energy Consumption by Home Appliances', fontsize=16, fontweight='bold')
ax1.set_xlabel('Energy Consumption (kWh/year)', fontsize=14)
ax1.set_ylabel('Appliances', fontsize=14)

# Remove grid lines for clarity
ax1.xaxis.grid(False)
ax1.yaxis.grid(False)

# Plot expected cost-saving as horizontal bar chart
bars2 = ax2.barh(appliances, cost_saving, color=colors, edgecolor='black')

# Annotate the bars with cost-saving values
for bar, saving in zip(bars2, cost_saving):
    ax2.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'${saving}', va='center', ha='left', fontsize=12, color='black')

# Set the title and labels for the second subplot
ax2.set_title('Expected Annual Cost-Saving from Energy-Efficient Upgrades', fontsize=16, fontweight='bold')
ax2.set_xlabel('Cost-Saving (USD/year)', fontsize=14)
ax2.set_ylabel('')

# Remove grid lines for clarity
ax2.xaxis.grid(False)
ax2.yaxis.grid(False)

# Ensure a tight layout
plt.tight_layout()

# Display the charts
plt.show()