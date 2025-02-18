import matplotlib.pyplot as plt
import numpy as np

# Data preparation with manually shuffled values
decades = np.array(['1980s', '1990s', '2000s', '2010s'])
caribbean_reef = np.array([35, 40, 25, 30])  # Values shuffled
pacific_reef = np.array([55, 60, 45, 50])    # Values shuffled
indian_ocean_reef = np.array([60, 70, 55, 65]) # Values shuffled

# Stack the data for plotting
reef_data = np.vstack([caribbean_reef, pacific_reef, indian_ocean_reef])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(decades, reef_data, labels=['Caribbean', 'Pacific', 'Indian Ocean'], 
             colors=['#FFA07A', '#20B2AA', '#9370DB'], alpha=0.75)

# Customize the chart with title and labels
ax.set_title('Oceanic Adventures:\nCoral Reef Coverage Changes Over Decades', fontsize=16, weight='bold', pad=15)
ax.set_xlabel('Decade', fontsize=12, weight='bold')
ax.set_ylabel('Coral Reef Coverage (%)', fontsize=12, weight='bold')

# Highlight specific decades with vertical lines
highlight_decades = ['1990s', '2010s']
for decade in highlight_decades:
    ax.axvline(x=decade, color='grey', linestyle='--', linewidth=1)

# Annotate a significant point
ax.annotate('Widespread Coral Bleaching\n(1990s)', xy=('1990s', 45), xytext=('1980s', 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Add grid
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Position the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Regions', fontsize=11, shadow=True)

# Add data points markers with corresponding lines
for y, color in zip(reef_data, ['#FFA07A', '#20B2AA', '#9370DB']):
    ax.plot(decades, y, marker='o', markersize=4, color=color, linestyle='None', alpha=0.9)

# Create an additional subplot for % change per decade
percent_change = np.diff(reef_data, axis=1) / reef_data[:, :-1] * 100
avg_percent_change = np.mean(percent_change, axis=0)

ax_change = ax.twinx()
ax_change.plot(decades[1:], avg_percent_change, color='black', linestyle='--', marker='x', label='Avg % Change')
ax_change.set_ylabel('Average % Change per Decade', fontsize=12, weight='bold')
ax_change.set_ylim(min(avg_percent_change) - 5, max(avg_percent_change) + 5)

# Tight layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()