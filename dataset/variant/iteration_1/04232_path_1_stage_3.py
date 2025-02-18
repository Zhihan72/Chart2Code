import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data for the historical performance of detective agencies in solving cases
agencies = ['Holmes', 'Poirot', 'Marple']

# Solve rate data (in percentages)
sherlock_data = [92, 95, 93, 90, 94, 91, 92, 92, 93, 95, 94, 91]
poirot_data = [88, 87, 89, 85, 86, 88, 90, 87, 89, 86, 85, 87]
marple_data = [78, 80, 82, 79, 81, 80, 79, 78, 80, 81, 82, 81]

solve_rates = [sherlock_data, poirot_data, marple_data]

fig, ax = plt.subplots(figsize=(12, 8))

# Horizontal box plot
box = ax.boxplot(solve_rates, vert=False, patch_artist=True, labels=agencies, notch=True, showfliers=True, whis=1.5)

colors = ['#FF6347', '#FFD700', '#98FB98']
patterns = ['/', '\\', '-']

for patch, color, pattern in zip(box['boxes'], colors, patterns):
    patch.set_facecolor(color)
    patch.set_hatch(pattern)

for element in ['whiskers', 'caps']:
    plt.setp(box[element], color='darkred', linewidth=1.5)
plt.setp(box['medians'], color='darkgreen', linewidth=2)

# Add data labels for mean
means = [np.mean(solve_rate) for solve_rate in solve_rates]
for i, mean in enumerate(means):
    ax.text(mean, i + 1, f'{mean:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.set_axisbelow(True)

plt.title('Agency Solve Rates (2022-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Rate (%)', fontsize=12)
plt.ylabel('Agency', fontsize=12)

legend_handles = [mpatches.Patch(facecolor=color, edgecolor='black', label=agency, hatch=pattern) for color, agency, pattern in zip(colors, agencies, patterns)]
plt.legend(handles=legend_handles, title="Agencies", loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()

plt.show()