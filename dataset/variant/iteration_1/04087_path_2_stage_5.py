import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Younglings (0-12)', 'Adolescents (13-19)', 'Mature (20-59)', 'Elders (60+)']

children_sleep = [9.5, 9, 9, 10, 10, 9.5, 9]
teenagers_sleep = [7.5, 7.2, 8, 8.2, 7.5, 7.8, 8]
adults_sleep = [6.8, 7, 7, 6.5, 6.9, 6.5, 7]
seniors_sleep = [6.5, 6, 6.3, 6.5, 6.7, 6.2, 6.5]

data = [children_sleep, teenagers_sleep, adults_sleep, seniors_sleep]

fig, axs = plt.subplots(1, 1, figsize=(12, 8))
violin = axs.violinplot(data, vert=False, showmeans=True, showextrema=True, showmedians=True)

colors = ['#99ff99', '#ffcc99', '#ff9999', '#66b3ff']
for i, pc in enumerate(violin['bodies']):
    pc.set_facecolor(colors[i % len(colors)])
    pc.set_edgecolor('purple')
    pc.set_alpha(0.5)

violin['cmeans'].set_color('orange')
violin['cmedians'].set_color('red')
violin['cbars'].set_edgecolor('blue')
violin['cbars'].set_linestyle('--')
violin['cbars'].set_linewidth(1.5)

axs.set_title("Snooze Habits Across Age Ranges\n(Nightly Sleep Duration Over a Week)", fontsize=16, fontweight='bold')
axs.set_xlabel("Sleep Duration (Hours)", fontsize=12)
axs.set_yticks(np.arange(1, len(age_groups) + 1))
axs.set_yticklabels(age_groups, fontsize=12)
axs.grid(axis='x', linestyle=':', alpha=0.5)
axs.spines['top'].set_visible(False)
axs.spines['right'].set_color('gray')
axs.spines['right'].set_linewidth(1.5)
axs.spines['left'].set_color('black')
axs.spines['bottom'].set_color('black')
plt.tight_layout()
plt.show()