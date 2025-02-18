import matplotlib.pyplot as plt
import numpy as np

# Data preparation
decades = np.array(['1980s', '1990s', '2000s', '2010s'])
pacific_reef = np.array([60, 55, 50, 45])
indian_ocean_reef = np.array([70, 65, 60, 55])
reef_data = np.vstack([pacific_reef, indian_ocean_reef])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(decades, reef_data, colors=['#20B2AA', '#20B2AA'], alpha=0.75)

# Remove title and labels
# ax.set_title('Oceanic Adventures:\nCoral Reef Coverage Changes Over Decades', fontsize=16, weight='bold', pad=15)
# ax.set_xlabel('Decade', fontsize=12, weight='bold')
# ax.set_ylabel('Coral Reef Coverage (%)', fontsize=12, weight='bold')

# Highlight specific decades with vertical lines
highlight_decades = ['1990s', '2010s']
for decade in highlight_decades:
    ax.axvline(x=decade, color='grey', linestyle='--', linewidth=1)

# Remove annotations
# ax.annotate('Widespread Coral Bleaching\n(1990s)', xy=('1990s', 45), xytext=('1980s', 50),
#             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Plot data points markers
for y in reef_data:
    ax.plot(decades, y, marker='o', markersize=4, color='#20B2AA', linestyle='None', alpha=0.9)

# Create an additional subplot for % change per decade
percent_change = np.diff(reef_data, axis=1) / reef_data[:, :-1] * 100
avg_percent_change = np.mean(percent_change, axis=0)
ax_change = ax.twinx()
ax_change.plot(decades[1:], avg_percent_change, color='black', linestyle='--', marker='x')

# Remove ylabel for the % change subplot
# ax_change.set_ylabel('Average % Change per Decade', fontsize=12, weight='bold')
ax_change.set_ylim(min(avg_percent_change) - 5, max(avg_percent_change) + 5)

plt.tight_layout()
plt.show()