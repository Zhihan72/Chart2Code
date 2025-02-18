import matplotlib.pyplot as plt
import numpy as np

attributes = ['Charisma', 'Agility', 'Wisdom', 'Intelligence', 'Strength']
n_attributes = len(attributes)

dragon_stats = [5, 6, 8, 9, 7]
unicorn_stats = [5, 7, 9, 8, 6]
griffin_stats = [9, 7, 6, 5, 8]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

def plot_creature(ax, stats, color):
    stats += stats[:1]
    ax.fill(angles, stats, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plot_creature(ax, dragon_stats, 'darkorange')
plot_creature(ax, unicorn_stats, 'mediumseagreen')
plot_creature(ax, griffin_stats, 'mediumslateblue')

plt.xticks(angles[:-1], attributes, color='gray', size=10)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="gray", size=8)
plt.ylim(0, 10)

plt.title("Eldoria's Mythical Beast Attributes", size=14, color='navy', pad=20)

plt.tight_layout()
plt.show()