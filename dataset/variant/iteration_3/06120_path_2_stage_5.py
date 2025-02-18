import numpy as np
import matplotlib.pyplot as plt

categories = ['Int', 'Phys', 'Emo', 'Spir', 'Soc']

aries = [7, 5, 8, 7, 6] 
taurus = [7, 6, 8, 7, 6]
gemini = [6, 8, 5, 9, 6]
cancer = [8, 5, 6, 9, 5]
leo = [5, 7, 8, 6, 8]

zodiac_data = np.array([aries, taurus, gemini, cancer, leo])

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar(ax, data, colors):
    for idx, d in enumerate(data):
        values = d.tolist()
        values += values[:1]
        ax.plot(angles, values, color=colors[idx], linewidth=2)
        ax.fill(angles, values, color=colors[idx], alpha=0.4)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']
plot_radar(ax, zodiac_data, colors)

plt.xticks(angles[:-1], categories, color='dimgray', size=10)

ax.set_yticklabels([])
ax.set_ylim(0, 10)
plt.grid(False)

plt.tight_layout()
plt.show()