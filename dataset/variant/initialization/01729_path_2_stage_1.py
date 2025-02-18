import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Germany', 'India', 'Brazil']
investments = np.array([
    [30, 25, 10],
    [20, 35, 15],
    [15, 20, 5],
    [25, 15, 10],
    [10, 5, 20]
])

energy_types = ['Solar', 'Wind', 'Hydro']
colors = ['#FFA07A', '#20B2AA', '#4682B4']

cumulative_investments = investments.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(12, 7))

for i in range(len(energy_types)):
    ax.barh(countries, investments[:, i], left=(cumulative_investments[:, i] - investments[:, i]),
            color=colors[i], edgecolor='black', label=energy_types[i], height=0.6)

ax.set_title('2023 RE Investments', fontsize=16, fontweight='bold')
ax.set_xlabel('Investments (B USD)', fontsize=12)
ax.set_ylabel('Countries', fontsize=12)

ax.legend(title='Energy', loc='upper right')

for i, country in enumerate(countries):
    for j in range(len(energy_types)):
        ax.text(cumulative_investments[i, j] - investments[i, j] / 2, i, 
                f"${investments[i, j]}B", color='black', ha='center', va='center', fontsize=10)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()