import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
demographics = ['Women', 'Men', 'Non-Binary', 'Underrepresented Minorities', 'Others']

data = {
    'Women': [35, 32, 30, 40, 38],
    'Men': [-45, -48, -50, -38, -40],
    'Non-Binary': [6, 4, 10, 2, 8],
    'Underrepresented Minorities': [-18, -20, -15, -22, -16],
    'Others': [4, 3.5, 5, 4.5, 3]
}

# New color set for the bars
colors = ['#FFB6C1', '#87CEFA', '#32CD32', '#FFA07A', '#DAA520']

fig, ax = plt.subplots(figsize=(12, 8))

for i, category in enumerate(demographics):
    values = data[category]
    ax.bar(years, values, label=category, color=colors[i], edgecolor='grey', linewidth=1.5)

ax.axhline(0, color='darkgrey', linewidth=1)
ax.xaxis.grid(True, linestyle='-.', which='major', color='darkgrey', alpha=0.7)

marker_styles = ['o', 'v', 's', 'p', 'D']
for i, category in enumerate(demographics):
    values = data[category]
    ax.plot(years, values, marker=marker_styles[i], color='none', markeredgecolor='black', markersize=8, linestyle='None')

ax.set_ylabel('Percentage')
ax.set_title('Diverging Bar Chart of Enrollment Data')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

plt.tight_layout()
plt.show()