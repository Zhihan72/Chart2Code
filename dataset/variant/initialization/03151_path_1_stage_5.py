import matplotlib.pyplot as plt
import numpy as np

def radar_chart_angles(n):
    return np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()

def create_radar_data(values, angles):
    return values + values[:1], angles + angles[:1]

categories = ['Mem', 'Att', 'Problem', 'Creativity', 'Verbal', 'Logic', 'Speed', 'EQ']

alpha_mix = [8, 7, 6, 5, 9, 8, 6, 7]
beta_boost = [6, 8, 7, 4, 6, 9, 5, 8]
gamma_grow = [7, 6, 8, 9, 5, 7, 8, 6]
delta_develop = [5, 6, 7, 8, 9, 6, 7, 5]

angles = radar_chart_angles(len(categories))

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.suptitle("Cognitive Abilities & Blends", fontsize=14, fontweight='bold', va='bottom')

blends_data = {'A-Mix': alpha_mix, 'B-Boost': beta_boost, 'G-Grow': gamma_grow, 'D-Develop': delta_develop}

line_styles = ['-', '--', '-.', ':']

# Randomly changed stylistic elements
for i, (name, blend) in enumerate(blends_data.items()):
    values, angles_filled = create_radar_data(blend, angles)
    ax.plot(angles_filled, values, color=np.random.choice(['#FF6347', '#20B2AA', '#9370DB', '#FFD700']), 
            linewidth=2, linestyle=line_styles[i], marker='o')

ax.set_yticks(range(1, 11))
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=10, fontstyle='italic')

ax.yaxis.grid(True, linestyle=':', linewidth=0.5)
ax.xaxis.grid(True, linestyle=':', linewidth=0.5)
ax.set_ylim(0, 10)

plt.legend(loc='best', title="Blends", fontsize=10, frameon=False)
plt.tight_layout()
plt.show()