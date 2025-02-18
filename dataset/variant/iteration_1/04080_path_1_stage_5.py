import matplotlib.pyplot as plt
import numpy as np

departments = ['Tech Dept', 'Resources', 'Events', 'Staff']

budget_2017 = [4.5, 2.5, 1.8, 2.0]
budget_2018 = [4.8, 2.7, 1.9, 2.1]
budget_2019 = [5.0, 2.8, 2.0, 2.2]
budget_2020 = [5.3, 3.0, 2.3, 2.3]
budget_2021 = [5.5, 3.2, 2.5, 2.4]

data = np.array([budget_2017, budget_2018, budget_2019, budget_2020, budget_2021])

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(departments))
height = 0.15

# Define a new set of colors for each year
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

for i in range(data.shape[0]):
    ax.barh(x + (i - 2) * height, data[i], height, edgecolor='black', color=colors[i])

ax.set_ylabel('Dept Categories', fontsize=14)
ax.set_xlabel('Funds (in $M)', fontsize=14)
ax.set_title('Annual Funding for Library Groups (2017-2021)', fontsize=16, fontweight='bold')
ax.set_yticks(x)
ax.set_yticklabels(departments)

ax.xaxis.grid(False)
ax.legend().remove()

for i in range(data.shape[0]):
    bars = ax.barh(x + (i - 2) * height, data[i], height, color=colors[i])
    for bar, width in zip(bars, data[i]):
        ax.annotate(f'{width:.1f}', 
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0), 
                    textcoords="offset points",
                    ha='left', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()