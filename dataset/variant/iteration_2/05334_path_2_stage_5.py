import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
categories = ['IT Infrastructure', 'Marketing', 'Research & Development', 'Miscellaneous', 
              'Salaries', 'Operational Costs', 'Training & Development']

data = np.array([
    [8, 10, 12, 14, 16],        # IT Infrastructure
    [20, 25, 30, 35, 40],       # Marketing
    [15, 20, 25, 30, 35],       # Research & Development
    [5, 6, 7, 8, 9],            # Miscellaneous
    [50, 55, 60, 65, 70],       # Salaries
    [10, 15, 20, 25, 30],       # Operational Costs
    [3, 4, 5, 6, 7]             # Training & Development
])

sorted_indices = [5, 1, 2, 4, 0, 3, 6]
data = data[sorted_indices]
categories = np.array(categories)[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(categories, data[:, -1], color='#377eb8', edgecolor='k', linewidth=0.6)

ax.set_xlabel("Sections", fontsize=14)
ax.set_ylabel("Funding Allocations (millions)", fontsize=14)

for i, value in enumerate(data[:, -1]):
    ax.text(i, value / 2, f'{value}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

plt.tight_layout()
plt.show()