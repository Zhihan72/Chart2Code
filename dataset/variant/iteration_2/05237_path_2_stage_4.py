import matplotlib.pyplot as plt
import numpy as np

categories = ['Navigation', 'Combat Tactics', 'Resource Management', 'Weather Prediction', 'Team Leadership']
num_vars = len(categories)

captain_blackbeard = [9, 6, 8, 7, 9]
captain_kidd = [6, 8, 7, 9, 8]
captain_teach = [8, 9, 9, 8, 7]
captain_morgan = [8, 9, 7, 6, 9]
captain_drake = [7, 9, 8, 8, 7]

captains = [captain_blackbeard, captain_kidd, captain_teach, captain_morgan, captain_drake]
for captain in captains:
    captain += captain[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

def plot_radar(data, label):
    color = 'steelblue'
    linestyle = '-' if label == 'Captain Blackbeard' else '--'
    marker = 'o' if label == 'Captain Kidd' else 's'
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, label=label, color=color, linestyle=linestyle, linewidth=2, marker=marker)

plot_radar(captain_blackbeard, 'Captain Blackbeard')
plot_radar(captain_kidd, 'Captain Kidd')
plot_radar(captain_teach, 'Captain Teach')
plot_radar(captain_morgan, 'Captain Morgan')
plot_radar(captain_drake, 'Captain Drake')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkred')
plt.title('Performance Analysis of Ocean Rovers Guild Captains\nAcross Key Maritime Skills', fontsize=16, fontweight='bold', pad=20, color='darkgreen')

ax.legend(loc='upper left', bbox_to_anchor=(1.1, 1.2), fontsize=11, title='Sea Captains', title_fontsize='13', frameon=False)
plt.tight_layout()
plt.grid(color='black', linestyle=':', linewidth=0.7)

plt.show()