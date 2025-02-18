import matplotlib.pyplot as plt
import numpy as np

cities = ['Chicago', 'New York', 'Los Angeles']
utilities = ['Internet', 'Electricity', 'Water']

electricity_cost = [150, 135, 145]
water_cost = [50, 55, 45]
internet_cost = [70, 65, 75]

data = np.array([internet_cost, electricity_cost, water_cost])

bar_width = 0.25
index = np.arange(len(cities))

# Use a single color for all utilities
uniform_color = '#1f77b4'

fig, ax = plt.subplots(figsize=(14, 8))

# Plot each utility's data with the same color
for i in range(len(utilities)):
    ax.bar(index + i * bar_width, data[i], bar_width, label=utilities[i], color=uniform_color)

ax.set_xlabel('Major U.S. Cities', fontsize=12)
ax.set_ylabel('Utility Costs per Month (in USD)', fontsize=12)
ax.set_title('2023 Utility Costs in Urban Areas: A Randomized Analysis', fontsize=16, fontweight='bold')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(cities)

for i in range(len(utilities)):
    for j in range(len(cities)):
        ax.text(index[j] + i * bar_width, data[i][j] + 2, 
                f'${data[i][j]:.0f}', ha='center', va='bottom', fontsize=10)

ax.legend(title='Utility Categories', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

plt.tight_layout()
plt.show()