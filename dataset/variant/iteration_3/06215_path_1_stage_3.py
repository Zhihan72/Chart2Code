import matplotlib.pyplot as plt
import numpy as np

cities = ['Los Angeles', 'New York', 'Chicago']
utilities = ['Water', 'Internet', 'Electricity', 'Gas']

electricity_cost = [150, 135, 145]
water_cost = [50, 55, 45]
internet_cost = [70, 65, 75]
gas_cost = [60, 70, 65]  # New gas cost data

# Updated data arrays with new utility
positive_data = np.array([water_cost, internet_cost, electricity_cost, gas_cost])
negative_data = -1 * positive_data

index = np.arange(len(cities))

colors = ['#ff7f0e', '#2ca02c', '#1f77b4', '#d62728']  # Added new color for Gas

fig, ax = plt.subplots(figsize=(14, 8))

# Modified loop to incorporate new utility
for i, (utility, color) in enumerate(zip(utilities, colors)):
    ax.bar(index, positive_data[i], 0.5, label=utility + ' (Above)', color=color)
    ax.bar(index, negative_data[i], 0.5, color=color, alpha=0.5)

ax.set_xlabel('Major Cities', fontsize=12)
ax.set_ylabel('Monthly Average Spending (USD)', fontsize=12)
ax.set_title('Utility Expenses Variation Across Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xticks(index)
ax.set_xticklabels(cities)

# Extended loop to add labels for the new data
for i in range(len(utilities)):
    for j in range(len(cities)):
        ax.text(index[j], positive_data[i][j] + 2, 
                f'${positive_data[i][j]:.0f}', ha='center', va='bottom', fontsize=10)
        ax.text(index[j], negative_data[i][j] - 5, 
                f'${-negative_data[i][j]:.0f}', ha='center', va='top', fontsize=10, alpha=0.5)

ax.legend(title='Utility Types', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()

plt.show()