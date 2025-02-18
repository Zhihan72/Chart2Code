import matplotlib.pyplot as plt
import numpy as np

years = np.array([2019, 2020, 2021, 2022, 2023])
gardens_created = np.array([5, 15, 25, 40, 60])
volunteers_joined = np.array([50, 120, 180, 250, 320])
average_area = np.array([200, 250, 300, 350, 400])
workshops_conducted = np.array([3, 6, 12, 18, 25])
community_funds_raised = np.array([1000, 4500, 7000, 12000, 20000])
volunteers_returned = np.array([10, 30, 50, 70, 100])

fig, ax1 = plt.subplots(figsize=(12, 7))

bar_width = 0.2
bar1 = ax1.barh(years - bar_width, gardens_created, bar_width, label='Vegetation Spaces Initiated', color='green', edgecolor='black', hatch='/')
bar2 = ax1.barh(years, workshops_conducted, bar_width, label='Workshops Conducted', color='blue', edgecolor='black', hatch='.')
bar3 = ax1.barh(years + bar_width, community_funds_raised / 1000, bar_width, label='Community Funds Raised (thousands $)', color='orange', edgecolor='black', hatch='*')

ax2 = ax1.twiny()
bar4 = ax2.barh(years, volunteers_joined, bar_width, label='Helpers Enrolled', color='yellow', edgecolor='black', hatch='\\')
bar5 = ax2.barh(years + bar_width, volunteers_returned, bar_width, label='Returning Volunteers', color='purple', edgecolor='black', hatch='x')

line = ax2.plot(average_area, years, color='#ff9999', marker='s', linestyle='--', label='Mean Garden Dimension', lw=2, markerfacecolor='#66b3ff')

ax1.set_title("Expansion of Urban Nature in Greentown: Milestones (2019-2023)", fontsize=14, fontweight='bold')
ax1.set_ylabel("Chronological Year", fontsize=12)
ax1.set_xlabel("Spaces Initiated & Workshops Conducted", fontsize=12)
ax2.set_xlabel("Volunteers & Mean Dimension Area (sq m)", fontsize=12)

ax1.set_yticks(years)
ax1.set_yticklabels(years)

# Combine both bar plots for the legend
bars = bar1 + bar2 + bar3 + bar4 + bar5
labels = [b.get_label() for b in bars] + ['Mean Garden Dimension']
ax2.legend(bars, labels, loc='lower right', bbox_to_anchor=(1.1, 0))

ax1.grid(True, linestyle=':', linewidth=1, color='gray')
ax2.grid(False)

plt.tight_layout()
plt.show()