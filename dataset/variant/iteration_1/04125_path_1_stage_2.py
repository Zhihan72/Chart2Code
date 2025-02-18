import matplotlib.pyplot as plt
import numpy as np

decades = np.array(['1980s', '1990s', '2000s', '2010s'])
caribbean_reef = np.array([35, 40, 25, 30])
pacific_reef = np.array([55, 60, 45, 50])
indian_ocean_reef = np.array([60, 70, 55, 65])
reef_data = np.vstack([caribbean_reef, pacific_reef, indian_ocean_reef])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(decades, reef_data, labels=['Caribbean', 'Pacific', 'Indian Ocean'],
             colors=['#CD5C5C', '#4682B4', '#6A5ACD'], alpha=0.85)

ax.set_title('Oceanic Adventures: Coral Reef Coverage Changes', fontsize=18, weight='heavy', pad=20)
ax.set_xlabel('Decade', fontsize=14, style='italic')
ax.set_ylabel('Coral Reef Coverage (%)', fontsize=14, style='italic')

highlight_decades = ['1990s', '2010s']
for decade in highlight_decades:
    ax.axvline(x=decade, color='navy', linestyle='-.', linewidth=1.5)

ax.annotate('Coral Bleaching Event\n(1990s)', xy=('1990s', 45), xytext=('1980s', 60),
            arrowprops=dict(facecolor='darkgreen', shrink=0.05), fontsize=11, weight='bold')

ax.grid(visible=True, linestyle='-', alpha=0.9, color='black')

ax.legend(loc='upper right', bbox_to_anchor=(0, 0.9), title='Ocean Regions', fontsize=12, shadow=False)

for y, color in zip(reef_data, ['#CD5C5C', '#4682B4', '#6A5ACD']):
    ax.plot(decades, y, marker='*', markersize=6, color=color, linestyle=':', alpha=1)

percent_change = np.diff(reef_data, axis=1) / reef_data[:, :-1] * 100
avg_percent_change = np.mean(percent_change, axis=0)

ax_change = ax.twinx()
ax_change.plot(decades[1:], avg_percent_change, color='darkred', linestyle='-', marker='h', label='Avg % Change')
ax_change.set_ylabel('Average % Change per Decade', fontsize=12, style='italic')
ax_change.set_ylim(min(avg_percent_change) - 5, max(avg_percent_change) + 5)

plt.tight_layout()
plt.show()