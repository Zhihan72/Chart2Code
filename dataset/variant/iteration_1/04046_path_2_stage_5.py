import numpy as np
import matplotlib.pyplot as plt
from math import pi

abilities = ['Strength', 'Speed', 'Intelligence', 'Agility', 'Stamina', 'Stealth']
num_abilities = len(abilities)

superheroes = {
    'Superman': [9, 9, 8, 8, 10, 6],
    'Wonder Woman': [8, 8, 7, 9, 9, 7],
    'Batman': [6, 7, 10, 8, 7, 9],
    'Flash': [6, 10, 6, 9, 7, 8],
    'Aquaman': [9, 7, 6, 7, 8, 7]
}

for hero, scores in superheroes.items():
    superheroes[hero] += scores[:1]

angles = np.linspace(0, 2 * pi, num_abilities, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(2, 1, figsize=(9, 18), subplot_kw={'polar': True})

colors = ['b', 'g', 'r', 'c', 'm']

# Radar Chart for Superheroes
for i, (hero, scores) in enumerate(superheroes.items()):
    ax[0].plot(angles, scores, color=colors[i], linewidth=2, linestyle='solid')
    ax[0].fill(angles, scores, color=colors[i], alpha=0.25, label=hero)

ax[0].set_xticks(angles[:-1])
ax[0].set_xticklabels(abilities)
ax[0].set_ylim(0, 10)
ax[0].legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Bar Chart for Mean Scores
mean_scores = {hero: np.mean(scores[:-1]) for hero, scores in superheroes.items()}  # Re-calculate mean without repeated first element
ax2 = plt.subplot(212)
ax2.bar(mean_scores.keys(), mean_scores.values(), color=colors, alpha=0.7)
ax2.set_ylim(0, 10)

plt.tight_layout()
plt.show()