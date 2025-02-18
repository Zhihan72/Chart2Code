import matplotlib.pyplot as plt
import numpy as np

years = np.array([2019, 2020, 2021, 2022, 2023])
gardens_created = np.array([5, 15, 25, 40, 60])
volunteers_joined = np.array([50, 120, 180, 250, 320])
average_area = np.array([200, 250, 300, 350, 400])

fig, ax1 = plt.subplots(figsize=(10, 6))

bar_width = 0.35
bar1 = ax1.barh(years - bar_width/2, gardens_created, bar_width, label='Vegetation Spaces Initiated', color='green', edgecolor='black', hatch='/')

ax2 = ax1.twiny()
bar2 = ax2.barh(years + bar_width/2, volunteers_joined, bar_width, label='Helpers Enrolled', color='yellow', edgecolor='black', hatch='\\')

line = ax2.plot(average_area, years, color='#ff9999', marker='s', linestyle='--', label='Mean Garden Dimension', lw=2, markerfacecolor='#66b3ff')

ax1.set_title("Expansion of Urban Nature in Greentown: Milestones (2019-2023)", fontsize=14, fontweight='bold')
ax1.set_ylabel("Chronological Year", fontsize=12)
ax1.set_xlabel("Spaces Initiated for Vegetation", fontsize=12)
ax2.set_xlabel("Participants & Mean Dimension Area (sq m)", fontsize=12)

ax1.set_yticks(years)
ax1.set_yticklabels(years)

bars = bar1 + bar2
labels = [b.get_label() for b in bars] + ['Mean Garden Dimension']
ax2.legend(bars, labels, loc='lower right')

ax1.grid(True, linestyle=':', linewidth=1, color='gray')
ax2.grid(False)

plt.tight_layout()
plt.show()