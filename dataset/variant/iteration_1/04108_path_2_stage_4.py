import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Females', 'Males', 'Non-Conforming', 'Minorities', 'Misc']

data = {
    'Females': [31, 30, 36, 37, 39],
    'Males': [49, 47, 44, 42, 36],
    'Non-Conforming': [3, 5, 7, 8, 9],
    'Minorities': [14, 15, 19, 21, 20],
    'Misc': [2, 4, 3.5, 5, 4.8]
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

ax.set_title('InTechville Enrollment Trends (2018-2022)', fontsize=14, pad=15)
ax.set_ylabel('Participants (%)', fontsize=10)
ax.set_xlabel('Timeline', fontsize=10)

ax.legend(title='Groups', loc='lower left', fontsize=8)

for i, year in enumerate(years):
    for y_offset, values, label in y_data:
        ax.text(i, y_offset[i] + values[i] / 2, f'{values[i]}%', ha='center', va='center', 
                color='white', fontsize=8)

ax.text(4.5, 105, 'Note: Initiatives yield positive results.', fontsize=10,
        style='italic', ha='right', va='center', bbox={'facecolor': 'white', 'alpha': 0.75, 'pad': 5})

ax.yaxis.grid(True, linestyle='-', color='lightgray', alpha=0.7)

plt.tight_layout()
plt.show()