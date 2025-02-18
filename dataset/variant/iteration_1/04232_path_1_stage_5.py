import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

agencies = ['Holmes', 'Poirot', 'Marple']

sherlock_data = [92, 95, 93, 90, 94, 91, 92, 92, 93, 95, 94, 91]
poirot_data = [88, 87, 89, 85, 86, 88, 90, 87, 89, 86, 85, 87]
marple_data = [78, 80, 82, 79, 81, 80, 79, 78, 80, 81, 82, 81]

solve_rates = [sherlock_data, poirot_data, marple_data]

fig, ax = plt.subplots(figsize=(12, 8))

box = ax.boxplot(solve_rates, vert=False, patch_artist=True, labels=agencies, notch=False, showfliers=False, whis=2.0)

# Shuffled colors and patterns
colors = ['#7FFF00', '#FF69B4', '#8A2BE2']
patterns = ['*', '.', 'o']

for patch, color, pattern in zip(box['boxes'], colors, patterns):
    patch.set_facecolor(color)
    patch.set_hatch(pattern)

plt.setp(box['whiskers'], color='black', linewidth=2, linestyle='-')
plt.setp(box['caps'], color='brown', linewidth=2)
plt.setp(box['medians'], color='blue', linewidth=2, linestyle='-.')

ax.xaxis.grid(False)

plt.title('Agency Solve Rates (2022-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Rate (%)', fontsize=12)
plt.ylabel('Agency', fontsize=12)

legend_handles = [
    mpatches.Patch(facecolor=color, edgecolor='black', label=agency, hatch=pattern) 
    for color, agency, pattern in zip(colors, agencies, patterns)
]
plt.legend(handles=legend_handles, title="Agencies", loc='lower right', bbox_to_anchor=(1, 0))

plt.tight_layout()

plt.show()