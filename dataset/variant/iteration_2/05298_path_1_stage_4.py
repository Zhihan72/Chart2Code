import numpy as np
import matplotlib.pyplot as plt
from math import pi

dragonscore = [9, 6, 10, 7, 8, 9]
phoenixscore = [8, 9, 9, 5, 8, 7]

angles = np.linspace(0, 2 * pi, len(dragonscore), endpoint=False).tolist()
angles += angles[:1]

dragonscore += dragonscore[:1]
phoenixscore += phoenixscore[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.plot(angles, dragonscore, linewidth=2, linestyle='-', marker='o', color='orange')
ax.fill(angles, dragonscore, 'orange', alpha=0.25)

ax.plot(angles, phoenixscore, linewidth=2, linestyle='-', marker='o', color='red')
ax.fill(angles, phoenixscore, 'red', alpha=0.25)

plt.xticks([])
plt.yticks([])
plt.ylim(0, 10)

plt.show()