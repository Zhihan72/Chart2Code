import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

agencies = ['Holmes & Co. Investigations', 'Poirot Detective Ltd.', 'Columbo Inc.']

sherlock_data = [92, 95, 93, 90, 94, 91, 92, 92, 93, 95, 94, 91]
poirot_data = [88, 87, 89, 85, 86, 88, 90, 87, 89, 86, 85, 87]
columbo_data = [70, 72, 71, 74, 73, 72, 71, 73, 74, 70, 71, 72]

solve_rates = [sherlock_data, poirot_data, columbo_data]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(solve_rates, vert=False, patch_artist=True, labels=agencies, notch=False, showfliers=True, whis=1.0)

colors = ['#FF4500', '#32CD32', '#8A2BE2']
patterns = ['/', 'o', '\\']

for patch, color, pattern in zip(box['boxes'], colors, patterns):
    patch.set_facecolor(color)
    patch.set_hatch(pattern)

for element in ['whiskers', 'caps']:
    plt.setp(box[element], color='navy', linewidth=1.0)
plt.setp(box['medians'], color='purple', linewidth=1.5)

means = [np.mean(solve_rate) for solve_rate in solve_rates]
for i, mean in enumerate(means):
    ax.text(mean, i + 1, f'{mean:.1f}%', ha='left', va='center', fontsize=10, fontweight='bold', color='brown')

ax.xaxis.grid(True, linestyle=':', which='major', color='black', alpha=0.5)
ax.set_axisbelow(True)

plt.title('Mystery Solvers Efficiency:\nAnnual Result Rates (2022-2023)', fontsize=16, fontweight='normal')
plt.xlabel('Resolution Rate (%)', fontsize=11)
plt.ylabel('Detective Organizations', fontsize=11)

legend_handles = [mpatches.Patch(facecolor=color, edgecolor='grey', label=agency, hatch=pattern) for color, agency, pattern in zip(colors, agencies, patterns)]
plt.legend(handles=legend_handles, title="Detectives", loc='lower right')

plt.tight_layout()
plt.show()