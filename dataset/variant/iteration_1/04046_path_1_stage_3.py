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

ax1.set_title('Battle of Legends: Superhero Abilities Comparison', fontsize=16, fontweight='light', pad=25)
colors = plt.cm.plasma(np.linspace(0, 1, len(superheroes)))
markers = ['o', 's', '^', 'd', 'v', '<', '>', '*']  # Different marker types
line_styles = ['-', '--', '-.', ':']

for i, (hero, color) in enumerate(zip(superheroes.keys(), colors)):
    ax1.plot(angles, superheroes[hero], color=color, linewidth=2, label=hero, 
             linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)])
    ax1.fill(angles, superheroes[hero], color=color, alpha=0.2)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(abilities, fontsize=13, fontweight='normal', color='black')
ax1.set_ylim(0, 10)
ax1.yaxis.set_tick_params(labelsize=11, width=1.5)

ax1.legend(loc='lower left', bbox_to_anchor=(1.05, 0.05), fontsize=10, title="Superheroes", title_fontsize=13)
ax1.grid(False)
ax1.spines['polar'].set_color('grey')
ax1.spines['polar'].set_linewidth(1.5)

ax2 = plt.subplot(122)
mean_scores = {key: sum(superheroes[key])/len(superheroes[key]) for key in superheroes}
ax2.bar(mean_scores.keys(), mean_scores.values(), color=colors, alpha=0.8, edgecolor='black', linewidth=1)
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Score', fontsize=13, fontweight='normal', color='black')
ax2.set_title('Overall Ability Scores', fontsize=16, fontweight='light', pad=25)
for hero, score in mean_scores.items():
    ax2.text(hero, score + 0.3, f'{score:.2f}', ha='center', va='bottom', fontsize=11, fontweight='normal', color='blue')

plt.tight_layout()
plt.show()