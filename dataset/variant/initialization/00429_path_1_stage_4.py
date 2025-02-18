import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Kids', 'Teens', 'Y. Adults', 'M. Aged', 'Seniors', 'Elders']
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute', 'Trumpet', 'Sax', 'Clarinet']

preferences = np.array([
    [30, 40, 45, 20, 10, 15, 25, 30],  
    [20, 55, 35, 45, 20, 25, 30, 20],
    [50, 35, 30, 40, 15, 30, 20, 25],
    [60, 50, 30, 25, 10, 20, 15, 10],
    [20, 25, 20, 10, 50, 20, 40, 30],
    [10, 15, 20, 15, 40, 25, 20, 15]   
])

preferences[:, :preferences.shape[1]//2] *= -1

fig, ax = plt.subplots(figsize=(14, 9))
bar_width = 0.15
indices = np.arange(len(age_groups))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#fdbf6f']
hatch_patterns = ['/', '\\', '|', '-', '+', 'x', 'o', '*']

for i, instrument in enumerate(instruments):
    ax.barh(
        indices + i * bar_width, 
        preferences[:, i], 
        height=bar_width, 
        label=instrument, 
        color=colors[i % len(colors)], 
        edgecolor='brown', 
        linestyle=(0, (5, 10)),  
        hatch=hatch_patterns[i % len(hatch_patterns)]
    )

ax.set_xlabel('# of People', fontsize=14, style='italic')
ax.set_title('Instrument Preferences by Age', fontsize=16, fontweight='bold')
ax.set_yticks(indices + bar_width * (len(instruments) - 1) / 2)
ax.set_yticklabels(age_groups, fontsize=12, color='purple')
ax.xaxis.grid(True, linestyle='-.', color='gray', alpha=0.7)
ax.legend(title='Instruments', fontsize=10, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=2, shadow=True)

plt.tight_layout()
plt.show()