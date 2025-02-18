import matplotlib.pyplot as plt
import numpy as np

cities = ['Los Angeles', 'New York', 'Chicago']
utilities = ['Water', 'Internet', 'Electricity', 'Gas']

electricity_cost = [150, 135, 145]
water_cost = [50, 55, 45]
internet_cost = [70, 65, 75]
gas_cost = [60, 70, 65]

positive_data = np.array([water_cost, internet_cost, electricity_cost, gas_cost])
negative_data = -1 * positive_data

index = np.arange(len(cities))

# New set of colors to replace the original ones
colors = ['#6a0dad', '#ff6347', '#3cb371', '#4682b4']  # Replaced colors

fig, ax = plt.subplots(figsize=(14, 8))

for i, (utility, color) in enumerate(zip(utilities, colors)):
    ax.bar(index, positive_data[i], 0.5, label=utility + ' (Above)', color=color)
    ax.bar(index, negative_data[i], 0.5, color=color, alpha=0.5)

ax.set_xlabel('Major Cities', fontsize=12)
ax.set_ylabel('Monthly Average Spending (USD)', fontsize=12)
ax.set_title('Utility Expenses Variation Across Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xticks(index)
ax.set_xticklabels(cities)

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