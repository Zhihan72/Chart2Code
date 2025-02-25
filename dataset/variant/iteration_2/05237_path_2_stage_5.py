import matplotlib.pyplot as plt
import numpy as np

num_vars = 5

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

def plot_radar(data):
    color = 'steelblue'
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linestyle='--', linewidth=2)

plot_radar(captain_blackbeard)
plot_radar(captain_kidd)
plot_radar(captain_teach)
plot_radar(captain_morgan)
plot_radar(captain_drake)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels([''] * num_vars)  # Remove category labels

plt.grid(color='black', linestyle=':', linewidth=0.7)

plt.show()