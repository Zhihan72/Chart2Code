import matplotlib.pyplot as plt
import numpy as np

age_grps = ['Kids', 'Teens', 'Y. Adults', 'Mid-Aged', 'Old']
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute', 'Trumpet', 'Sax']

preferences = np.array([
    [25, 45, 40, 15, 15, 10, 30],
    [25, 50, 30, 40, 15, 30, 35],
    [40, 30, 40, 35, 20, 25, 25],
    [55, 45, 35, 30, 20, 15, 20],
    [30, 20, 25, 15, 55, 25, 35]
])

fig, ax = plt.subplots(figsize=(14, 9))

indices = np.arange(len(age_grps))

# Manually shuffled colors
colors = ['#8c564b', '#e377c2', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#1f77b4']

# Creating a stacked bar chart
bottom_vals = np.zeros(len(age_grps))
for i, instrument in enumerate(instruments):
    bar = ax.bar(
        indices, 
        preferences[:, i], 
        label=instrument, 
        color=colors[i],
        bottom=bottom_vals,
        edgecolor='k'
    )
    bottom_vals += preferences[:, i]  # Update the bottom position for stacking

ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Pop', fontsize=12)
ax.set_title('Music Preferences by Age', fontsize=16, fontweight='bold')
ax.set_xticks(indices)
ax.set_xticklabels(age_grps, fontsize=10)

ax.legend(title='Instruments', fontsize=9, loc='upper left')
ax.yaxis.grid(True, linestyle=':', which='major', color='purple', alpha=0.7)

plt.tight_layout()
plt.show()