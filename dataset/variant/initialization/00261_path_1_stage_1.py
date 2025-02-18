import matplotlib.pyplot as plt
import numpy as np

# Define categories and household data
categories = ['Energy\nConsumption', 'Waste\nReduction', 'Water\nUsage', 'Transport\nHabits', 'Green\nPurchases']
household_data = {
    'Household A': [7, 9, 8, 6, 7],
    'Household B': [8, 6, 7, 9, 8],
    'Household C': [6, 7, 9, 8, 6],
    'Household D': [5, 8, 6, 7, 9],
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

average_data = np.mean([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()
average_data += average_data[:1]
variability = np.std([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()
variability += variability[:1]

for household, values in household_data.items():
    values += values[:1]
    ax.plot(angles, values, linewidth=1.5, linestyle='-')
    ax.fill(angles, values, alpha=0.15)

ax.plot(angles, average_data, linewidth=2, linestyle='--', color='red')
ax.errorbar(angles, average_data, yerr=variability, fmt='o', color='red', capsize=5)

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([])  # Remove y-axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Remove x-axis labels

plt.tight_layout()
plt.show()