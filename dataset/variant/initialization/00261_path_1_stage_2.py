import matplotlib.pyplot as plt
import numpy as np

# Define categories and household data with altered values
categories = ['Energy\nConsumption', 'Waste\nReduction', 'Water\nUsage', 'Transport\nHabits', 'Green\nPurchases']
household_data = {
    'Household A': [9, 6, 8, 7, 7],  # Altered
    'Household B': [8, 7, 6, 8, 9],  # Altered
    'Household C': [9, 6, 7, 6, 8],  # Altered
    'Household D': [8, 6, 9, 7, 5],  # Altered
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
ax.set_yticklabels([])  
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  

plt.tight_layout()
plt.show()