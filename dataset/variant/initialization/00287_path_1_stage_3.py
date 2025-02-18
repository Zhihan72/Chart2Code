import matplotlib.pyplot as plt
import numpy as np

attributes = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Charisma']
n_attributes = len(attributes)

# Randomly altering the stats maintaining the original structure
dragon_stats = [6, 7, 9, 8, 5]
unicorn_stats = [7, 6, 8, 9, 5]
griffin_stats = [8, 7, 5, 6, 9]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

def plot_creature(ax, stats, label, color):
    stats += stats[:1]
    ax.fill(angles, stats, color=color, alpha=0.25, label=label)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plot_creature(ax, dragon_stats, 'Dragon', 'darkorange')
plot_creature(ax, unicorn_stats, 'Unicorn', 'mediumseagreen')
plot_creature(ax, griffin_stats, 'Griffin', 'mediumslateblue')

plt.xticks(angles[:-1], attributes, color='gray', size=10)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="gray", size=8)
plt.ylim(0, 10)

plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.title("Attributes of Mythical Creatures\nin the World of Eldoria", size=14, color='navy', pad=20)

plt.tight_layout()

plt.show()