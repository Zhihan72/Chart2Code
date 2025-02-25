import matplotlib.pyplot as plt
import numpy as np

public_transport_hubs_day = np.array([70, 72, 74, 71, 73, 75, 76, 72, 73, 74])
public_transport_hubs_night = np.array([60, 62, 64, 61, 63, 62, 60, 61, 63, 62])

data_violin = [
    np.array([45, 50, 55, 47, 52, 53, 48, 50, 51, 49]),
    np.array([35, 38, 40, 36, 39, 37, 34, 36, 38, 37]),
    np.array([65, 68, 70, 66, 69, 67, 70, 71, 68, 66]),
    np.array([55, 58, 60, 56, 59, 57, 54, 59, 60, 58]),
    np.array([75, 80, 85, 78, 82, 81, 79, 77, 80, 78]),
    np.array([65, 68, 70, 66, 69, 68, 67, 66, 68, 67]),
    public_transport_hubs_day,
    public_transport_hubs_night
]
scenarios = ['Residential Day', 'Residential Night', 'Commercial Day', 'Commercial Night', 
             'Industrial Day', 'Industrial Night', 'Transport Hubs Day', 'Transport Hubs Night']

fig, ax = plt.subplots(figsize=(16, 8))

vparts = ax.violinplot(data_violin, showmedians=True, showmeans=True, showextrema=True, widths=0.7)

# Manually shuffled color palette
colors = ['#CD5C5C', '#5F9EA0', '#FF8C00', '#7FFFD4', '#8B0000', '#8A2BE2', '#6A5ACD', '#FFA500']

for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.6)

for partname, style in zip(('cbars', 'cmeans', 'cmedians'), ('-', '--', ':')):
    vparts[partname].set_edgecolor('black')
    vparts[partname].set_linestyle(style)
    vparts[partname].set_linewidth(2.0 if partname == 'cmeans' else 1.0)

ax.set_title("Noise Pollution Levels in Different Urban Scenarios\nDuring Day and Night", fontsize=18, fontweight='bold')
ax.set_ylabel("Noise Levels (dB)", fontsize=14)
ax.set_xlabel("Urban Scenario", fontsize=14)
ax.set_xticks(np.arange(1, len(scenarios) + 1))
ax.set_xticklabels(scenarios, rotation=45, fontsize=12)

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(handles, scenarios, title="Scenarios", loc='upper left', fontsize=12, title_fontsize='13')

plt.tight_layout()
plt.show()