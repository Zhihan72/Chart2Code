import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Tokyo', 'London', 'São Paulo', 'New York']
years = np.arange(2025, 2015, -1)

ucri_scores = np.array([
    [86, 88, 85, 83, 80, 77, 75, 72, 70, 68],
    [87, 90, 85, 83, 82, 80, 78, 77, 76, 74],
    [82, 84, 80, 78, 76, 74, 72, 69, 67, 65],
    [75, 77, 73, 72, 70, 68, 66, 64, 62, 60],
    [86, 88, 85, 83, 80, 77, 75, 72, 70, 68]
])

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(ucri_scores, cmap='YlGn', aspect='auto')

ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(cities)))
ax.set_xticklabels(years)
ax.set_yticklabels(cities)

# Annotate cells with scores
for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(j, i, ucri_scores[i, j], va='center', ha='center', color='black', fontsize=10)

plt.xticks(rotation=45)
plt.show()