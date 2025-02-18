import matplotlib.pyplot as plt
import numpy as np

residential_day = np.array([45, 50, 55, 47, 52, 53, 48, 50, 51, 49])
residential_night = np.array([35, 38, 40, 36, 39, 37, 34, 36, 38, 37])
commercial_day = np.array([65, 68, 70, 66, 69, 67, 70, 71, 68, 66])
commercial_night = np.array([55, 58, 60, 56, 59, 57, 54, 59, 60, 58])
industrial_day = np.array([75, 80, 85, 78, 82, 81, 79, 77, 80, 78])
industrial_night = np.array([65, 68, 70, 66, 69, 68, 67, 66, 68, 67])

data_violin = [residential_day, residential_night, commercial_day, commercial_night, industrial_day, industrial_night]
scenarios = ['Res. Day', 'Res. Nite', 'Commrc Day', 'Commrc Nite', 'Industri Day', 'Industri Night']

fig, ax = plt.subplots(figsize=(14, 8))
vparts = ax.violinplot(data_violin, vert=False, showmedians=True, showmeans=True, showextrema=True, widths=0.7)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.6)
    
for partname in ('cbars', 'cmeans', 'cmedians'):
    vparts[partname].set_edgecolor('black')
    vparts[partname].set_linewidth(1.5)

ax.set_title("Urban Sound Levels in Varying Conditions\nby Daylight and Night", fontsize=18, fontweight='bold')
ax.set_xlabel("Sound Intensities (dB)", fontsize=14)
ax.set_ylabel("Urban Context", fontsize=14)
ax.set_yticks(np.arange(1, len(scenarios) + 1))
ax.set_yticklabels(scenarios, fontsize=12)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(handles, scenarios, title="Scene Types", loc='upper right', fontsize=12, title_fontsize='13')

plt.tight_layout()
plt.show()