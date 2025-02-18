import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Altered attributes and scores
attributes = ['Healing', 'Wisdom', 'Fire Power', 'Strength', 'Mystical Aura', 'Flight Speed']
dragonscore = [6, 8, 9, 9, 7, 10]
phoenixscore = [9, 8, 8, 7, 5, 9]

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

dragonscore += dragonscore[:1]
phoenixscore += phoenixscore[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

dragon_color = 'blue'
phoenix_color = 'red'

ax.plot(angles, dragonscore, linewidth=2, linestyle='-', marker='o', color=dragon_color)
ax.fill(angles, dragonscore, dragon_color, alpha=0.25)

ax.plot(angles, phoenixscore, linewidth=2, linestyle='-', marker='o', color=phoenix_color)
ax.fill(angles, phoenixscore, phoenix_color, alpha=0.25)

# Altered title and labels
plt.xticks(angles[:-1], attributes, color='black', size=12)
plt.title("Battle of Creatures: Magical Element Comparison", size=16, weight='bold', pad=20)
ax.yaxis.set_tick_params(labelsize=10, colors='black')
plt.yticks(range(1, 11), ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], color='black', size=10)
plt.ylim(0, 10)
plt.tight_layout()
plt.show()