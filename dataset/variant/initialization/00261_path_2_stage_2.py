import matplotlib.pyplot as plt
import numpy as np

categories = ['Water\nConsumption', 'Transport\nReduction', 'Energy\nUsage', 'Purchasing\nHabits', 'Waste\nManagement']
household_data = {
    'Family X': [7, 9, 8, 6, 7],
    'Family Y': [8, 6, 7, 9, 8],
    'Family Z': [6, 7, 9, 8, 6],
    'Family W': [5, 8, 6, 7, 9],
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

average_data = np.mean([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()
average_data += average_data[:1]
variability = np.std([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()
variability += variability[:1]

colors = ['green', 'blue', 'orange', 'purple']

for idx, (household, values) in enumerate(household_data.items()):
    values += values[:1]
    ax.plot(angles, values, linewidth=1.5, linestyle='-', label=household, color=colors[idx])
    ax.fill(angles, values, alpha=0.15, color=colors[idx])

ax.plot(angles, average_data, linewidth=2, linestyle='--', color='red', label='Average')
ax.errorbar(angles, average_data, yerr=variability, fmt='o', color='red', capsize=5)

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=8)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='teal')

plt.title('Eco-Conscious Actions\nComparison of Four Families and General Average', size=16, weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.tight_layout()
plt.show()