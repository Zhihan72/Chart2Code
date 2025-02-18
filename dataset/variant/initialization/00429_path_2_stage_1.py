import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Children', 'Teenagers', 'Young Adults', 'Middle-Aged', 'Seniors']
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute', 'Trumpet', 'Saxophone']

preferences = np.array([
    [30, 40, 45, 20, 10, 15, 25],
    [20, 55, 35, 45, 20, 25, 30],
    [50, 35, 30, 40, 15, 30, 20],
    [60, 50, 30, 25, 10, 20, 15],
    [20, 25, 20, 10, 50, 20, 40]
])

std_devs = np.array([
    [5, 3, 4, 2, 1, 2, 3],
    [4, 5, 2, 3, 2, 2, 4],
    [3, 4, 3, 4, 2, 3, 3],
    [4, 3, 2, 3, 1, 2, 2],
    [3, 2, 4, 2, 3, 3, 4]
])

fig, ax = plt.subplots(figsize=(14, 9))

bar_width = 0.12
indices = np.arange(len(age_groups))

# Colors for the instruments
colors = ['#e377c2', '#8c564b', '#2ca02c', '#ff7f0e', '#9467bd', '#1f77b4', '#d62728']

# Plotting with different marker types and line styles
for i, instrument in enumerate(instruments):
    bar = ax.bar(
        indices + i * bar_width, 
        preferences[:, i], 
        width=bar_width, 
        yerr=std_devs[:, i], 
        label=instrument, 
        color=colors[i],
        capsize=4,
        edgecolor='k',  # Add border to bars
        linestyle='-' if i % 2 == 0 else '--'  # Randomly shuffled line styles
    )
    ax.bar_label(bar, label_type='edge', padding=3, fontsize=9)

ax.set_xlabel('Age Groups', fontsize=12)
ax.set_ylabel('Number of People', fontsize=12)
ax.set_title('Musical Instrument Preference Among Age Groups', fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * (len(instruments) / 2))
ax.set_xticklabels(age_groups, fontsize=10)

average_preferences = preferences.mean(axis=1)
ax.plot(indices + bar_width * (len(instruments) / 2 - 0.5), average_preferences, label='Average Preference', color='black', linestyle='-.', marker='s')  # Changed to dash-dot line with square markers

# Alter the legend
ax.legend(title='Instruments & Overall Trend', fontsize=9, loc='upper left')  # Changed position of legend

# Modify grid style
ax.yaxis.grid(True, linestyle=':', which='major', color='purple', alpha=0.7)  # Altered grid color and style

plt.tight_layout()
plt.show()