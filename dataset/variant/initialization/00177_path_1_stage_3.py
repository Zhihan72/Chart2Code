import numpy as np
import matplotlib.pyplot as plt

agencies = ['NASA', 'ESA', 'Roscosmos']
years = ['2010', '2015', '2020']
success_rates = np.array([
    [85, 90, 95],
    [75, 85, 88],
    [80, 83, 89]
])

fig, ax = plt.subplots(figsize=(12, 8))

# Shuffle the colors for each data group or type
colors = ['tomato', 'mediumslateblue', 'seagreen']
hatches = ['', '/', '//']

bar_width = 0.25
for i, year in enumerate(years):
    ax.barh(np.arange(len(agencies)) + i * bar_width, success_rates[:, i], height=bar_width, 
            color=colors[i], edgecolor='black', hatch=hatches[i], alpha=0.7)

ax.set_yticks(np.arange(len(agencies)) + bar_width)
ax.set_yticklabels(agencies, fontsize=11, style='italic')
ax.set_xlim(0, 100)
ax.set_xlabel('Success Rate (%)', fontsize=10)
ax.set_title("Space Exploration Success Rates (2010-2020)\nMission Outcomes by Leading Space Agencies",
             fontsize=14, weight='bold')

ax.legend(years, loc='lower left', title='Year', fontsize=9, title_fontsize='10')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(axis='x', linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()