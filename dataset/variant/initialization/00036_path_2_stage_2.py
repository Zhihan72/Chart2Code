import matplotlib.pyplot as plt
import numpy as np

# Activities and their corresponding energy consumption split into positive and negative sides
activities = [
    'Heating & Cooling', 'Water Heating', 'Lighting', 'Appliances', 'Electronics',
    'Other', 'Renewable Energy', 'Insulation', 'Cooking', 'Refrigerators', 'Washing Machines',
    'Smart Home Devices', 'Electric Vehicles', 'Home Office'
]

# Assuming some categories are expanded from the central axis to the left and some to the right
positive_side = np.array([2500, 1000, 800, 300, 600, 400])
negative_side = np.array([1500, 1200, 500, 1000, 500, 200, 300])

# Combine consumption values assuming two groups - one positive, one negative from the central axis
consumption = np.concatenate([-negative_side, positive_side])

# Extended activity labels and colors
activities_expanded = activities[:len(negative_side)] + activities[len(activities)-len(positive_side):]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6'] * 2

# Prepare figure
fig, ax = plt.subplots(figsize=(12, 10))

# Diverging bar chart
y_pos = np.arange(len(activities_expanded))
ax.barh(y_pos, consumption, color=colors, edgecolor='gray')

# Add labels inside bars
for i in range(len(consumption)):
    ax.text(consumption[i], y_pos[i], f'{abs(consumption[i]):d}', va='center', ha='center', 
            color='black', fontsize=9)

# Set title and labels
ax.set_title('Diverging Breakdown of Household Energy Consumption', fontsize=16, pad=20)
ax.set_xlabel('Consumption (kWh)', fontsize=12)

# Remove and refine the legend and y-ticks
ax.set_yticks(y_pos)
ax.set_yticklabels(activities_expanded)

# Improve layout spacing
plt.tight_layout()

# Display plot
plt.show()