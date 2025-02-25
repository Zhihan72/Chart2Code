import matplotlib.pyplot as plt
import numpy as np

categories = ['Tactics Navigation', 'Resource Forecasting', 'Leadership Skills', 'Environmental Planning', 'Combat Management']
num_vars = len(categories)

captain_jack = [6, 9, 8, 7, 9]
captain_flint = [8, 6, 8, 7, 7]
captain_hook = [8, 9, 9, 7, 8]
captain_sparrow = [9, 7, 9, 8, 6]
captain_neem = [7, 8, 8, 9, 8]

captains = [captain_jack, captain_flint, captain_hook, captain_sparrow, captain_neem]
for captain in captains:
    captain += captain[:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

def plot_radar(data, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

plot_radar(captain_jack, 'deepskyblue')
plot_radar(captain_flint, 'tomato')
plot_radar(captain_hook, 'limegreen')
plot_radar(captain_sparrow, 'gold')
plot_radar(captain_neem, 'mediumslateblue')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='darkblue')

plt.title('Key Skills Comparison among Sea Captain Circle\nPerformance Metrics', fontsize=16, fontweight='bold', pad=20, color='navy')

plt.show()