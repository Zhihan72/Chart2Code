import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data for the historical performance of detective agencies in solving cases
agencies = ['Sherlock Holmes & Co.', 'Poirot Detective Services', 'Marple Investigations']

# Manually crafted solve rate data (in percentages)
sherlock_data = [92, 95, 93, 90, 94, 91, 92, 92, 93, 95, 94, 91]
poirot_data = [88, 87, 89, 85, 86, 88, 90, 87, 89, 86, 85, 87]
marple_data = [78, 80, 82, 79, 81, 80, 79, 78, 80, 81, 82, 81]

# Organize data for the box plot
solve_rates = [sherlock_data, poirot_data, marple_data]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal box plot
box = ax.boxplot(solve_rates, vert=False, patch_artist=True, labels=agencies, notch=True, showfliers=True, whis=1.5)

# Define colors and patterns
colors = ['#FF6347', '#FFD700', '#98FB98']
patterns = ['/', '\\', '-']

# Customize box plot colors
for patch, color, pattern in zip(box['boxes'], colors, patterns):
    patch.set_facecolor(color)
    patch.set_hatch(pattern)

# Whisker, cap, median settings
for element in ['whiskers', 'caps']:
    plt.setp(box[element], color='darkred', linewidth=1.5)
plt.setp(box['medians'], color='darkgreen', linewidth=2)

# Add data labels for mean
means = [np.mean(solve_rate) for solve_rate in solve_rates]
for i, mean in enumerate(means):
    ax.text(mean, i + 1, f'{mean:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Add grid and enhance readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.set_axisbelow(True)

# Title and labels with improved readability
plt.title('Detective Agency Performance Analysis:\nAnnual Case Solution Rates (2022-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Solve Rate (%)', fontsize=12)
plt.ylabel('Agencies', fontsize=12)

# Add legend for box colors
legend_handles = [mpatches.Patch(facecolor=color, edgecolor='black', label=agency, hatch=pattern) for color, agency, pattern in zip(colors, agencies, patterns)]
plt.legend(handles=legend_handles, title="Agencies", loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()