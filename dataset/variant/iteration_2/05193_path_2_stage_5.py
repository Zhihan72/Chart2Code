import matplotlib.pyplot as plt
import numpy as np

# Data initialization
residential_day = np.array([50, 48, 55, 47, 52, 45, 53, 50, 49, 51])
residential_night = np.array([38, 37, 35, 36, 39, 34, 38, 37, 36, 40])
commercial_day = np.array([68, 66, 71, 65, 70, 67, 70, 68, 69, 66])
commercial_night = np.array([58, 60, 54, 55, 59, 56, 60, 58, 59, 57])
industrial_day = np.array([80, 75, 78, 81, 77, 82, 85, 80, 78, 79])
industrial_night = np.array([68, 65, 69, 66, 67, 70, 66, 67, 68, 68])

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

ax.set_xlabel("Sound Intensities (dB)", fontsize=14)
ax.set_ylabel("Urban Context", fontsize=14)
ax.set_yticks(np.arange(1, len(scenarios) + 1))
ax.set_yticklabels(scenarios, fontsize=12)

plt.show()