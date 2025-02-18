import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Germany', 'India', 'Brazil']
investments = np.array([
    [10, 25, 30],
    [35, 15, 20],
    [20, 5, 15],
    [15, 25, 10],
    [5, 10, 20]
])

total_investments = investments.sum(axis=1)
sorted_indices = np.argsort(-total_investments)
countries = np.array(countries)[sorted_indices]
investments = investments[sorted_indices]
cumulative_investments = investments.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(12, 7))

energy_types = ['Solar', 'Wind', 'Hydro']
styles = [('s', (0, (5, 1))), ('o', 'dotted'), ('v', (0, (3, 3, 1, 3)))]
colors = ['#4682B4', '#FFA07A', '#20B2AA']

for i, (marker, linestyle) in enumerate(styles):
    ax.barh(countries, investments[:, i], 
            left=(cumulative_investments[:, i] - investments[:, i]), 
            color=colors[i], edgecolor='grey', label=energy_types[i], 
            height=0.6, hatch=marker)

ax.set_title('Renewable Investments 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Investment (Billion USD)', fontsize=12)
ax.set_ylabel('Countries', fontsize=12)
ax.legend(title='Type', loc='lower right')
ax.xaxis.grid(True, linestyle='-.', alpha=0.8)

for i, country in enumerate(countries):
    for j in range(len(energy_types)):
        ax.text(cumulative_investments[i, j] - investments[i, j] / 2, i, 
                f"${investments[i, j]}B", color='black', ha='center', va='center', fontsize=10)

plt.tight_layout()
plt.show()