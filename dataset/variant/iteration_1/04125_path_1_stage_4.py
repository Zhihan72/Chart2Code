import matplotlib.pyplot as plt
import numpy as np

decades = np.array(['80s', '90s', '00s', '10s'])
caribbean_reef = np.array([35, 40, 25, 30])
pacific_reef = np.array([55, 60, 45, 50])
indian_ocean_reef = np.array([60, 70, 55, 65])
reef_data = np.vstack([caribbean_reef, pacific_reef, indian_ocean_reef])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(decades, reef_data, labels=['Carib', 'Pac', 'Ind'],
             colors=['#4682B4', '#6A5ACD', '#CD5C5C'], alpha=0.85)

ax.set_title('Coral Reef Coverage', fontsize=18, weight='heavy', pad=20)
ax.set_xlabel('Decade', fontsize=14, style='italic')
ax.set_ylabel('Coverage (%)', fontsize=14, style='italic')

highlight_decades = ['90s', '10s']
for decade in highlight_decades:
    ax.axvline(x=decade, color='navy', linestyle='-.', linewidth=1.5)

ax.annotate('Bleaching\nEvent (90s)', xy=('90s', 45), xytext=('80s', 60),
            arrowprops=dict(facecolor='darkgreen', shrink=0.05), fontsize=11, weight='bold')

ax.grid(visible=True, linestyle='-', alpha=0.9, color='black')

ax.legend(loc='upper right', bbox_to_anchor=(0, 0.9), title='Regions', fontsize=12, shadow=False)

for y, color in zip(reef_data, ['#4682B4', '#6A5ACD', '#CD5C5C']):
    ax.plot(decades, y, marker='*', markersize=6, color=color, linestyle=':', alpha=1)

percent_change = np.diff(reef_data, axis=1) / reef_data[:, :-1] * 100
avg_percent_change = np.mean(percent_change, axis=0)

ax_change = ax.twinx()
ax_change.plot(decades[1:], avg_percent_change, color='darkred', linestyle='-', marker='h', label='% Change')
ax_change.set_ylabel('% Change/Decade', fontsize=12, style='italic')
ax_change.set_ylim(min(avg_percent_change) - 5, max(avg_percent_change) + 5)

plt.tight_layout()
plt.show()