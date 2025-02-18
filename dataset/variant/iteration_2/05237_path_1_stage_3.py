import matplotlib.pyplot as plt
import numpy as np

categories = ['Navigation', 'Combat Tactics', 'Resource Management', 'Weather Prediction', 'Team Leadership']
num_vars = len(categories)

# Randomly alter values within each captain's data while preserving structure
captain_blackbeard = [6, 9, 8, 7, 9]
captain_kidd = [8, 6, 8, 7, 7]
captain_teach = [8, 9, 9, 7, 8]
captain_morgan = [9, 7, 9, 8, 6]
captain_drake = [7, 8, 8, 9, 8]

captains = [captain_blackbeard, captain_kidd, captain_teach, captain_morgan, captain_drake]
for captain in captains:
    captain += captain[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

def plot_radar(data, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

plot_radar(captain_blackbeard, 'deepskyblue')
plot_radar(captain_kidd, 'tomato')
plot_radar(captain_teach, 'limegreen')
plot_radar(captain_morgan, 'gold')
plot_radar(captain_drake, 'mediumslateblue')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='darkblue')

plt.title('Performance Analysis of Ocean Rovers Guild Captains\nAcross Key Maritime Skills', fontsize=16, fontweight='bold', pad=20, color='navy')

plt.show()