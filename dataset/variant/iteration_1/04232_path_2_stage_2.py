import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

agencies = ['Holmes & Co. Investigations', 'Poirot Detective Ltd.', 'Columbo Inc.']

sherlock_data = [92, 95, 93, 90, 94, 91, 92, 92, 93, 95, 94, 91]
poirot_data = [88, 87, 89, 85, 86, 88, 90, 87, 89, 86, 85, 87]
columbo_data = [70, 72, 71, 74, 73, 72, 71, 73, 74, 70, 71, 72]

solve_rates = [sherlock_data, poirot_data, columbo_data]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(solve_rates, vert=True, patch_artist=True, labels=agencies, notch=True, showfliers=True, whis=1.5)

colors = ['#FF6347', '#FFD700', '#1E90FF']
patterns = ['/', '\\', '|']

for patch, color, pattern in zip(box['boxes'], colors, patterns):
    patch.set_facecolor(color)
    patch.set_hatch(pattern)

for element in ['whiskers', 'caps']:
    plt.setp(box[element], color='darkred', linewidth=1.5)
plt.setp(box['medians'], color='darkgreen', linewidth=2)

means = [np.mean(solve_rate) for solve_rate in solve_rates]
for i, mean in enumerate(means):
    ax.text(i + 1, mean, f'{mean:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.set_axisbelow(True)

plt.title('Mystery Solvers Efficiency:\nAnnual Result Rates (2022-2023)', fontsize=14, fontweight='bold')
plt.ylabel('Resolution Rate (%)', fontsize=12)
plt.xlabel('Detective Organizations', fontsize=12)

legend_handles = [mpatches.Patch(facecolor=color, edgecolor='black', label=agency, hatch=pattern) for color, agency, pattern in zip(colors, agencies, patterns)]
plt.legend(handles=legend_handles, title="Detectives", loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()