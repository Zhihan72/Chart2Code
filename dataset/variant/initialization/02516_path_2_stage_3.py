import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Machine Learning',
    'Data Visualization',
    'Communication',
    'Programming',
    'Domain Knowledge',
    'Statistical Analysis'
]

proficiency_healthcare = [7, 8, 6, 5, 9, 7]
proficiency_finance = [6, 8, 7, 9, 7, 8]
proficiency_technology = [8, 9, 8, 6, 7, 9]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
proficiency_healthcare += proficiency_healthcare[:1]
proficiency_finance += proficiency_finance[:1]
proficiency_technology += proficiency_technology[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.subplots_adjust(wspace=0.5)

ax.set_title('Skills Proficiency Radar Chart\nfor Data Scientists in 2025', fontsize=14, fontweight='bold', pad=20)

# Changed line styles and markers
ax.plot(angles, proficiency_healthcare, linewidth=1.5, linestyle='dashed', marker='o', label='Healthcare', color='#1f77b4')
ax.fill(angles, proficiency_healthcare, alpha=0.15, color='#1f77b4')

ax.plot(angles, proficiency_finance, linewidth=1.5, linestyle='dashdot', marker='s', label='Finance', color='#ff7f0e')
ax.fill(angles, proficiency_finance, alpha=0.15, color='#ff7f0e')

ax.plot(angles, proficiency_technology, linewidth=1.5, linestyle='dotted', marker='^', label='Technology', color='#2ca02c')
ax.fill(angles, proficiency_technology, alpha=0.15, color='#2ca02c')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='navy')

# Altered legend position and added grid lines
ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.15), fontsize=9, title='Industry')
ax.grid(color='gray', linestyle='-', linewidth=0.5)

# Removed plt.tight_layout() as it may not be necessary after adjusting appearance
plt.show()