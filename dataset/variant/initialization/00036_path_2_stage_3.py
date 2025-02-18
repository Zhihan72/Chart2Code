import matplotlib.pyplot as plt
import numpy as np

activities = [
    'Heating & Cooling', 'Water Heating', 'Lighting', 'Appliances', 'Electronics',
    'Other', 'Renewable Energy', 'Insulation', 'Cooking', 'Refrigerators', 'Washing Machines',
    'Smart Home Devices', 'Electric Vehicles', 'Home Office'
]

positive_side = np.array([2500, 1000, 800, 300, 600, 400])
negative_side = np.array([1500, 1200, 500, 1000, 500, 200, 300])

consumption = np.concatenate([-negative_side, positive_side])

activities_expanded = activities[:len(negative_side)] + activities[len(activities)-len(positive_side):]

# Shuffled colors
colors = ['#ffcc99', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0', '#ffb3e6', '#66b3ff', '#99ff99', '#ff9999', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff9999']

fig, ax = plt.subplots(figsize=(12, 10))
y_pos = np.arange(len(activities_expanded))

ax.barh(y_pos, consumption, color=colors, edgecolor='gray')

for i in range(len(consumption)):
    ax.text(consumption[i], y_pos[i], f'{abs(consumption[i]):d}', va='center', ha='center', color='black', fontsize=9)

ax.set_title('Diverging Breakdown of Household Energy Consumption', fontsize=16, pad=20)
ax.set_xlabel('Consumption (kWh)', fontsize=12)
ax.set_yticks(y_pos)
ax.set_yticklabels(activities_expanded)

plt.tight_layout()
plt.show()