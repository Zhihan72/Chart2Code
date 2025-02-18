import matplotlib.pyplot as plt

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
cost_saving = [75, 45, 60, 55, 70, 30, 80, 35]
colors = ['#FFD700', '#FF9999', '#40E0D0', '#66B2FF', '#8A2BE2', '#FFCC99', '#FF4500', '#99FF99']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.barh(appliances, energy_consumption, color=colors)
ax2.barh(appliances, cost_saving, color=colors)

ax1.set(xticks=[], yticks=[])  # Remove axis ticks
ax2.set(xticks=[], yticks=[])  # Remove axis ticks

plt.tight_layout()
plt.show()