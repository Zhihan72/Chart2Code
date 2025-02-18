import matplotlib.pyplot as plt
import numpy as np

departments = ['Health', 'Education', 'Infrastructure', 'Public Safety', 'Arts & Culture']
budget_2020 = [210, 180, 60, 150, 170]
budget_2021 = [220, 65, 155, 190, 180]
budget_2022 = [230, 70, 160, 200, 190]

# Sort data by budget for 2022 in descending order
sorted_indices = np.argsort(budget_2022)[::-1]
sorted_departments = [departments[i] for i in sorted_indices]
sorted_budget_2020 = [budget_2020[i] for i in sorted_indices]
sorted_budget_2021 = [budget_2021[i] for i in sorted_indices]
sorted_budget_2022 = [budget_2022[i] for i in sorted_indices]

x = np.arange(len(sorted_departments))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

bars_2020 = ax.bar(x - width, sorted_budget_2020, width, label='Year 2020', color='navy', linewidth=2, edgecolor='black')
bars_2021 = ax.bar(x, sorted_budget_2021, width, label='The Year 2021', color='gold', hatch='/', linewidth=2, edgecolor='gray')
bars_2022 = ax.bar(x + width, sorted_budget_2022, width, label='Fiscal 2022', color='darkred', linestyle='-', linewidth=2, edgecolor='darkred')

ax.set_title('City Budget Distribution Across Different Departments (2020-2022)', fontsize=14, fontweight='medium', pad=15)
ax.set_xlabel('Sector', fontsize=11)
ax.set_ylabel('Allocation (Million USD)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(['Culture & Arts', 'Safety and Enforcement', 'Urban Development', 'Schooling', 'Healthcare'])
ax.grid(axis='y', linestyle=':', color='grey', alpha=0.3)
ax.legend(title='Budget Year', fontsize=8, loc='upper left', frameon=False)

def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}', ha='center', va='bottom', fontsize=9, fontweight='regular')

add_labels(ax, bars_2020)
add_labels(ax, bars_2021)
add_labels(ax, bars_2022)

plt.tight_layout()
plt.show()