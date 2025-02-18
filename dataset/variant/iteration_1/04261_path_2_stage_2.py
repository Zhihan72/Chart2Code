import matplotlib.pyplot as plt

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

# Shuffled colors for each appliance
colors = ['#FFD700', '#FF9999', '#40E0D0', '#66B2FF', '#8A2BE2', '#FFCC99', '#FF4500', '#99FF99']

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot energy consumption as horizontal bar chart
ax1.barh(appliances, energy_consumption, color=colors, edgecolor='black')

# Plot expected cost-saving as horizontal bar chart
ax2.barh(appliances, cost_saving, color=colors, edgecolor='black')

# Ensure a tight layout
plt.tight_layout()

# Display the charts
plt.show()