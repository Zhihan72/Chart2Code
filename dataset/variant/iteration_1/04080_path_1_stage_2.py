import matplotlib.pyplot as plt
import numpy as np

departments = ['Tech Dept', 'Resources', 'Maintenance', 'Events', 'Staff']

budget_2017 = [4.5, 2.5, 3.8, 1.8, 2.0]
budget_2018 = [4.8, 2.7, 4.1, 1.9, 2.1]
budget_2019 = [5.0, 2.8, 4.5, 2.0, 2.2]
budget_2020 = [5.3, 3.0, 4.6, 2.3, 2.3]
budget_2021 = [5.5, 3.2, 4.8, 2.5, 2.4]

data = np.array([budget_2017, budget_2018, budget_2019, budget_2020, budget_2021])

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(departments))
width = 0.15

for i in range(data.shape[0]):
    ax.bar(x + (i - 2) * width, data[i], width, edgecolor='black')

ax.set_xlabel('Dept Categories', fontsize=14)
ax.set_ylabel('Funds (in $M)', fontsize=14)
ax.set_title('Annual Funding for Library Groups (2017-2021)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(departments, rotation=30, ha='right')

ax.yaxis.grid(False)
ax.legend().remove()

for i in range(data.shape[0]):
    bars = ax.bar(x + (i - 2) * width, data[i], width)
    for bar, height in zip(bars, data[i]):
        ax.annotate(f'{height:.1f}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()