import numpy as np
import matplotlib.pyplot as plt

agencies = ['ESA', 'Roscosmos', 'ISRO', 'NASA']  # Randomly altered order
years = ['2020', '2015', '2010']  # Randomly altered order

success_rates = np.array([
    [95, 90, 85],  # Altered column order to match the years
    [88, 85, 75],
    [89, 83, 80],
    [85, 78, 70]
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['seagreen', 'tomato', 'mediumslateblue', 'darkorange']  # Randomly altered order
hatches = ['//', '\\', '', '/']  # Randomly altered order

bar_width = 0.25
for i, year in enumerate(years):
    ax.barh(np.arange(len(agencies)) + i * bar_width, success_rates[:, i], height=bar_width,
            color=colors[i % len(colors)], edgecolor='black', hatch=hatches[i % len(hatches)], alpha=0.7)

ax.set_yticks(np.arange(len(agencies)) + bar_width)
ax.set_yticklabels(agencies, fontsize=11, style='italic')
ax.set_xlim(0, 100)
ax.set_xlabel('Mission Success (%)', fontsize=10)  # Randomly altered text
ax.set_title("Historical Data Review of Space Agencies' Success\nAchievement Rates (2010-2020)",
             fontsize=14, weight='bold')  # Randomly altered text

ax.legend(years, loc='lower left', title='Launch Year', fontsize=9, title_fontsize='10')  # Randomly altered text

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(axis='x', linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()