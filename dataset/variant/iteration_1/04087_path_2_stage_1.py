import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Children (0-12)', 'Teenagers (13-19)', 'Adults (20-59)', 'Seniors (60+)']

# Randomly altered content within each age group while preserving structure
# children_sleep was [9, 9.5, 10, 9, 9.5, 9, 10]
children_sleep = [9.5, 9, 9, 10, 10, 9.5, 9]

# teenagers_sleep was [7.2, 8, 7.5, 8, 7.8, 7.5, 8.2]
teenagers_sleep = [7.5, 7.2, 8, 8.2, 7.5, 7.8, 8]

# adults_sleep was [6.5, 7, 6.8, 7, 6.9, 7, 6.5]
adults_sleep = [6.8, 7, 7, 6.5, 6.9, 6.5, 7]

# seniors_sleep was [6, 6.5, 6.2, 6.5, 6.7, 6.5, 6.3]
seniors_sleep = [6.5, 6, 6.3, 6.5, 6.7, 6.2, 6.5]

data = [children_sleep, teenagers_sleep, adults_sleep, seniors_sleep]

fig, axs = plt.subplots(1, 1, figsize=(12, 8))
violin = axs.violinplot(data, vert=True, showmeans=True, showextrema=True, showmedians=True)

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for i, pc in enumerate(violin['bodies']):
    pc.set_facecolor(colors[i % len(colors)])
    pc.set_edgecolor('black')
    pc.set_alpha(0.6)

violin['cmeans'].set_color('blue')
violin['cmedians'].set_color('green')
for partname in ('cbars', 'cmins', 'cmaxes'):
    vp = violin[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

axs.set_title("Sleep Patterns Across Different Age Groups\n(Distribution of Sleep Hours per Night Over a Week)", fontsize=16, fontweight='bold')
axs.set_ylabel("Hours of Sleep", fontsize=12)
axs.set_xticks(np.arange(1, len(age_groups) + 1))
axs.set_xticklabels(age_groups, fontsize=12)
axs.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()