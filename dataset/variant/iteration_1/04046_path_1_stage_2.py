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
    'Aquaman': [9, 7, 6, 7, 8, 7],
    'Green Lantern': [7, 8, 7, 8, 8, 6],
    'Cyborg': [8, 6, 8, 7, 9, 7],
    'Martian Manhunter': [9, 8, 9, 8, 8, 8]
}

# Closing the loop for radar chart plotting
for hero, scores in superheroes.items():
    superheroes[hero] += scores[:1]

angles = np.linspace(0, 2 * pi, num_abilities, endpoint=False).tolist()
angles += angles[:1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), subplot_kw={'polar': True}, gridspec_kw={'width_ratios': [2.5, 1]})

ax1.set_title('Battle of Legends: Superhero Abilities Comparison', fontsize=14, fontweight='bold', pad=20)
colors = plt.cm.viridis(np.linspace(0, 1, len(superheroes)))
for (hero, color) in zip(superheroes.keys(), colors):
    ax1.fill(angles, superheroes[hero], color=color, alpha=0.25, label=hero)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(abilities, fontsize=12, fontweight='bold', color='darkblue')
ax1.set_ylim(0, 10)
ax1.yaxis.set_tick_params(labelsize=10)

ax1.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1), fontsize=11, title="Superheroes", title_fontsize=12)
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)
ax1.spines['polar'].set_visible(False)

ax2 = plt.subplot(122)
mean_scores = {key: sum(superheroes[key])/len(superheroes[key]) for key in superheroes}
ax2.bar(mean_scores.keys(), mean_scores.values(), color=colors, alpha=0.7)
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Score', fontsize=12, fontweight='bold', color='darkblue')
ax2.set_title('Overall Ability Scores', fontsize=14, fontweight='bold', pad=20)
for hero, score in mean_scores.items():
    ax2.text(hero, score + 0.2, f'{score:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkgreen')

plt.tight_layout()
plt.show()