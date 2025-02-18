import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define abilities and performance data
abilities = ['Strength', 'Speed', 'Intelligence', 'Agility', 'Stamina', 'Stealth']
num_abilities = len(abilities)

superheroes = {
    'Superman': [9, 9, 8, 8, 10, 6],
    'Wonder Woman': [8, 8, 7, 9, 9, 7],
    'Batman': [6, 7, 10, 8, 7, 9],
    'Flash': [6, 10, 6, 9, 7, 8],
    'Aquaman': [9, 7, 6, 7, 8, 7]
}

mean_scores = {hero: np.mean(scores) for hero, scores in superheroes.items()}

# Closing the loop for radar chart plotting
for hero, scores in superheroes.items():
    superheroes[hero] += scores[:1]

angles = np.linspace(0, 2 * pi, num_abilities, endpoint=False).tolist()
angles += angles[:1]

# Setup Figure with Two Subplots (Radar and Bar Charts)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), subplot_kw={'polar': True}, gridspec_kw={'width_ratios': [2.5, 1]})

# Radar Chart for Superheroes
colors = plt.cm.viridis(np.linspace(0, 1, len(superheroes)))
for (hero, color) in zip(superheroes.keys(), colors):
    ax1.plot(angles, superheroes[hero], color=color, linewidth=2, linestyle='solid')
    ax1.fill(angles, superheroes[hero], color=color, alpha=0.25)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels([''] * num_abilities)  # Removed labels
ax1.set_ylim(0, 10)

# Bar Chart for Mean Scores
ax2 = plt.subplot(122)
ax2.bar(mean_scores.keys(), mean_scores.values(), color=colors, alpha=0.7)
ax2.set_ylim(0, 10)

plt.tight_layout()
plt.show()