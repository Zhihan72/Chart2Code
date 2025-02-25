import matplotlib.pyplot as plt
import numpy as np

categories = ['Navigation', 'Combat Tactics', 'Resource Management', 'Weather Prediction', 'Team Leadership']
num_vars = len(categories)

captain_blackbeard = [8, 9, 6, 7, 9]
captain_kidd = [7, 8, 8, 6, 7]
captain_teach = [9, 7, 9, 8, 8]
captain_morgan = [6, 8, 7, 9, 9]
captain_drake = [8, 9, 7, 8, 8]

captains = [captain_blackbeard, captain_kidd, captain_teach, captain_morgan, captain_drake]
for captain in captains:
    captain += captain[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

def plot_radar(data, label, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, label=label, color=color, linewidth=2)

# New colors for each captain
plot_radar(captain_blackbeard, 'Captain Blackbeard', 'deepskyblue')
plot_radar(captain_kidd, 'Captain Kidd', 'tomato')
plot_radar(captain_teach, 'Captain Teach', 'limegreen')
plot_radar(captain_morgan, 'Captain Morgan', 'gold')
plot_radar(captain_drake, 'Captain Drake', 'mediumslateblue')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='darkblue')

plt.title('Performance Analysis of Ocean Rovers Guild Captains\nAcross Key Maritime Skills', fontsize=16, fontweight='bold', pad=20, color='navy')

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Sea Captains', title_fontsize='13', frameon=True, borderpad=1)
plt.tight_layout()
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()