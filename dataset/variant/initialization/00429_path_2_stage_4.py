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

std_devs = np.array([
    [4, 4, 5, 3, 2, 3, 4],
    [5, 4, 3, 4, 3, 3, 5],
    [4, 3, 4, 3, 3, 4, 3],
    [3, 4, 3, 3, 2, 4, 3],
    [4, 3, 5, 3, 4, 4, 5]
])

fig, ax = plt.subplots(figsize=(14, 9))

bar_width = 0.12
indices = np.arange(len(age_grps))

# Manually shuffled colors
colors = ['#8c564b', '#e377c2', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#1f77b4']

for i, instrument in enumerate(instruments):
    bar = ax.bar(
        indices + i * bar_width, 
        preferences[:, i], 
        width=bar_width, 
        yerr=std_devs[:, i], 
        label=instrument, 
        color=colors[i],
        capsize=4,
        edgecolor='k',
        linestyle='-' if i % 2 == 0 else '--'
    )
    ax.bar_label(bar, label_type='edge', padding=3, fontsize=9)

ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Pop', fontsize=12)
ax.set_title('Music Preferences by Age', fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * (len(instruments) / 2))
ax.set_xticklabels(age_grps, fontsize=10)

average_preferences = preferences.mean(axis=1)
ax.plot(indices + bar_width * (len(instruments) / 2 - 0.5), average_preferences, label='Avg Pref', color='black', linestyle='-.', marker='s')

ax.legend(title='Instruments & Avg', fontsize=9, loc='upper left')

ax.yaxis.grid(True, linestyle=':', which='major', color='purple', alpha=0.7)

plt.tight_layout()
plt.show()