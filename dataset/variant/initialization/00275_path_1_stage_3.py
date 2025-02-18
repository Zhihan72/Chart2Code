import matplotlib.pyplot as plt
import numpy as np

languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]
orbis_popularity = [92, 72, 80, 85, 68]

# Calculating the net difference from a central value (mean or median) for demonstration purposes
central_value = np.mean([xenon_popularity, zephyr_popularity, orbis_popularity], axis=0)
xenon_deviation = np.array(xenon_popularity) - central_value
zephyr_deviation = np.array(zephyr_popularity) - central_value
orbis_deviation = np.array(orbis_popularity) - central_value

bar_width = 0.5
r = np.arange(len(languages))

fig, ax = plt.subplots(figsize=(12, 7))
ax.barh(r, xenon_deviation, color='m', height=bar_width, label='Xenon')
ax.barh(r, zephyr_deviation, left=xenon_deviation, color='b', alpha=0.7, label='Zephyr')
ax.barh(r, orbis_deviation, left=xenon_deviation + zephyr_deviation, color='c', label='Orbis')

for i in range(len(languages)):
    ax.text(xenon_deviation[i] / 2, i, str(int(xenon_popularity[i])), va='center', ha='center', fontsize=9.5)
    ax.text((xenon_deviation[i] + zephyr_deviation[i] / 2), i, str(int(zephyr_popularity[i])), va='center', ha='center', fontsize=9.5)
    ax.text((xenon_deviation[i] + zephyr_deviation[i] + orbis_deviation[i] / 2), i, str(int(orbis_popularity[i])), va='center', ha='center', fontsize=9.5)

ax.set_yticks(r)
ax.set_yticklabels(languages)
ax.set_xlabel('Deviation from Mean Popularity (%)')
ax.set_title('Diverging Popularity of Programming Languages\nAcross Alien Planets')
ax.xaxis.grid(True, linestyle='-.', which='major', color='purple', alpha=0.5)

plt.legend(title='Planets', loc='upper left')
plt.tight_layout()
plt.show()