import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Women', 'Men', 'Non-Binary', 'Underrepresented Minorities', 'Others']

data = {
    'Women': [30, 32, 35, 38, 40],
    'Men': [50, 48, 45, 40, 38],
    'Non-Binary': [2, 4, 6, 8, 10],
    'Underrepresented Minorities': [15, 16, 18, 20, 22],
    'Others': [3, 3.5, 4, 4.5, 5]
}

colors = ['#f58231', '#4363d8', '#ffe119', '#3cb44b', '#e6194b']

def prepare_data(data, years):
    n_years = len(years)
    n_groups = len(data)
    y_offsets = np.zeros(n_years)
    y_data = []
    
    for key, values in data.items():
        y_data.append((y_offsets.copy(), values, key))
        y_offsets += values
    return y_data

y_data = prepare_data(data, years)

fig, ax = plt.subplots(figsize=(10, 6))

for y_offset, values, label in y_data:
    ax.bar(years, values, bottom=y_offset, label=label, color=colors.pop(0), edgecolor='black', linestyle='-.')

ax.set_title('Techville Diversity in Tech Education Enrollment (2018-2022)', fontsize=14, pad=15)
ax.set_ylabel('Enrollment (%)', fontsize=10)
ax.set_xlabel('Year', fontsize=10)

ax.legend(title='Demographics', loc='lower left', fontsize=8)

for i, year in enumerate(years):
    for y_offset, values, label in y_data:
        ax.text(i, y_offset[i] + values[i] / 2, f'{values[i]}%', ha='center', va='center', 
                color='white', fontsize=8)

ax.text(4.5, 105, 'Note: Diversity initiatives are impactful.', fontsize=10,
        style='italic', ha='right', va='center', bbox={'facecolor': 'white', 'alpha': 0.75, 'pad': 5})

ax.yaxis.grid(True, linestyle='-', color='lightgray', alpha=0.7)

plt.tight_layout()
plt.show()