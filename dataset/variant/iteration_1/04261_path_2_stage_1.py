import matplotlib.pyplot as plt
import numpy as np

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
energy_consumption = [500, 275, 400, 300, 450, 100, 475, 250]

# Expected annual cost-saving (in dollars) from energy-efficient upgrades
cost_saving = [75, 45, 60, 55, 70, 30, 80, 35]

# Colors for each appliance
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF4500', '#40E0D0', '#8A2BE2']

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot energy consumption as horizontal bar chart
ax1.barh(appliances, energy_consumption, color=colors, edgecolor='black')

# Remove grid lines for clarity
ax1.xaxis.grid(False)
ax1.yaxis.grid(False)

# Plot expected cost-saving as horizontal bar chart
ax2.barh(appliances, cost_saving, color=colors, edgecolor='black')

# Remove grid lines for clarity
ax2.xaxis.grid(False)
ax2.yaxis.grid(False)

# Ensure a tight layout
plt.tight_layout()

# Display the charts
plt.show()