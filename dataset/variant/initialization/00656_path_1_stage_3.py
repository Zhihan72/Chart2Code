import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'London', 'Tokyo', 'Sydney']
years = np.arange(2010, 2020)
ucri_scores = np.array([
    [68, 70, 72, 75, 77, 80, 83, 85, 86, 88],
    [65, 67, 69, 72, 74, 76, 78, 80, 82, 84],
    [74, 76, 77, 78, 80, 82, 83, 85, 87, 90],
    [70, 73, 75, 78, 81, 84, 86, 87, 88, 90]
])

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(ucri_scores, cmap='viridis', aspect='auto')

ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(cities)))
ax.set_xticklabels(years)
ax.set_yticklabels(cities)

plt.xticks(rotation=45)

for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(j, i, ucri_scores[i, j], va='center', ha='center', color='black', fontsize=10)

plt.tight_layout()
plt.show()