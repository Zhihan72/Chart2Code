import matplotlib.pyplot as plt
import numpy as np

activities = [
    'Heating & Cooling', 'Water Heating', 'Lighting', 'Appliances', 'Electronics',
    'Other', 'Renewable Energy', 'Insulation', 'Cooking', 'Refrigerators', 
    'Washing Machines', 'Smart Home Systems', 'Solar Panels', 'Electric Cars'
]

contributions = np.array([5, -4, 3, -1, 2, -0.5, 1, -2, 0.5, -0.3, 0.2, 1.5, -1.2, 2.5])

# Shuffled color palette
colors = [
    '#ffb3e6', '#99ff99', '#ffcc99', '#66b3ff', '#ff9999',
    '#ff6666', '#c2f0c2', '#c2c2f0', '#99c2ff', '#b3b3cc',
    '#ffeb99', '#99ccff', '#66ffb3', '#ffcccb'
]

fig, ax = plt.subplots(figsize=(14, 10))
ax.axvline(x=0, color='gray', linewidth=0.8)
bars = ax.barh(activities, contributions, color=colors)

for bar, contribution in zip(bars, contributions):
    label_position = bar.get_width() - 0.5 if contribution > 0 else bar.get_width() + 0.5
    ax.text(label_position, bar.get_y() + bar.get_height()/2, f'{contribution:.1f}', 
            va='center', ha='center', color='black', fontsize=9)

ax.set_title('Diverging Bar Chart: Impact on Energy Consumption', fontsize=16, pad=20)
ax.set_xlabel('Contribution to Total Energy Consumption', fontsize=12)
ax.set_xlim(-10, 10)

plt.tight_layout()
plt.show()