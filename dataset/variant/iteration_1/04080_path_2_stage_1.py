import matplotlib.pyplot as plt
import numpy as np

departments = ['Resources', 'Programs & Events', 'Technology', 'Staff Development', 'Maintenance']
budget_2017 = [4.5, 2.5, 3.8, 1.8, 2.0]
budget_2018 = [4.8, 2.7, 4.1, 1.9, 2.1]
budget_2019 = [5.0, 2.8, 4.5, 2.0, 2.2]
budget_2020 = [5.3, 3.0, 4.6, 2.3, 2.3]
budget_2021 = [5.5, 3.2, 4.8, 2.5, 2.4]

data = np.array([budget_2017, budget_2018, budget_2019, budget_2020, budget_2021])
years = ['2017', '2018', '2019', '2020', '2021']

fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(departments))
width = 0.15 

# Randomly altered stylistic elements: line styles, marker types, grid styles
marker_styles = ['o', 'v', '^', '<', '>']  # Circle, triangle down, triangle up, triangle left, triangle right
line_styles = ['-', '--', '-.', ':', '-']  # Solid, dashed, dash-dot, dotted, solid
bar_colors = ['#FFA07A', '#20B2AA', '#778899', '#FFFACD', '#DDA0DD']  # Coral, Light Sea Green, Light Slate Gray, Lemon Chiffon, Plum

for i, year in enumerate(years):
    ax.bar(x + (i - 2) * width, data[i], width, label=year, edgecolor='black', color=bar_colors[i])

ax.set_xlabel('Library Departments', fontsize=14)
ax.set_ylabel('Budget Allocation (in Millions USD)', fontsize=14)
ax.set_title('Yearly Library Budget Allocation Across Departments (2017-2021)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(departments, rotation=30, ha='right')
ax.legend(title='Year', frameon=False, fontsize=12, loc='upper left')  # Randomly change legend location and frame

ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='gray')  # Set grid color

def annotate_bars(rects, data_values):
    for i, rect in enumerate(rects):
        for j, bar in enumerate(rect):
            height = data_values[i][j]
            ax.annotate(f'{height:.1f}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, color='black')

rects_list = [ax.bar(x + (i - 2) * width, data[i], width, edgecolor='black') for i in range(len(years))]
annotate_bars(rects_list, data)

plt.tight_layout()
plt.show()