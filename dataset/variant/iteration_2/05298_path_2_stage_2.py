import numpy as np
import matplotlib.pyplot as plt
from math import pi

attributes = ['Fire Power', 'Healing', 'Flight Speed', 'Mystical Aura', 'Wisdom', 'Strength']
dragonscore = [9, 6, 10, 7, 8, 9]
phoenixscore = [8, 9, 9, 5, 8, 7]

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

dragonscore += dragonscore[:1]
phoenixscore += phoenixscore[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Apply a single color for both Dragon and Phoenix
color = 'blue'

ax.plot(angles, dragonscore, linewidth=2, linestyle='-', marker='o', color=color, label='Dragon')
ax.fill(angles, dragonscore, color, alpha=0.25)

ax.plot(angles, phoenixscore, linewidth=2, linestyle='-', marker='o', color=color, label='Phoenix')
ax.fill(angles, phoenixscore, color, alpha=0.25)

plt.xticks(angles[:-1], attributes, color='darkslategray', size=12)
plt.title("Mythical Creatures: Comparative Magical Attributes", size=16, weight='bold', pad=20)
ax.yaxis.set_tick_params(labelsize=10, colors='darkslategray')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.yticks(range(1, 11), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], color='grey', size=10)
plt.ylim(0, 10)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
plt.tight_layout()
plt.show()