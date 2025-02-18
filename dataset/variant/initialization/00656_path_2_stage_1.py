import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Tokyo', 'London', 'São Paulo', 'New York']  # Shuffled city labels
years = np.arange(2025, 2015, -1)  # Reversed year labels

ucri_scores = np.array([
    [86, 88, 85, 83, 80, 77, 75, 72, 70, 68],  # Sydney scores matching the row position
    [87, 90, 85, 83, 82, 80, 78, 77, 76, 74],  # Tokyo scores matching the row position
    [82, 84, 80, 78, 76, 74, 72, 69, 67, 65],  # London scores matching the row position
    [75, 77, 73, 72, 70, 68, 66, 64, 62, 60],  # São Paulo scores matching the row position
    [86, 88, 85, 83, 80, 77, 75, 72, 70, 68]   # New York scores matching the row position
])

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(ucri_scores, cmap='YlGn', aspect='auto')

ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(cities)))
ax.set_xticklabels(years)
ax.set_yticklabels(cities)
ax.set_xlabel('Timeline', fontsize=12)  # Randomly changed label
ax.set_ylabel('Metropolis', fontsize=12)  # Randomly changed label
ax.set_title('Climate Readiness City Score:', fontsize=14, fontweight='bold')  # Randomly changed title

plt.xticks(rotation=45)

cbar = fig.colorbar(cax)
cbar.set_label('Score Index', fontsize=12)  # Randomly changed label

# Annotate cells with scores
for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(j, i, ucri_scores[i, j], va='center', ha='center', color='black', fontsize=10)

plt.tight_layout()
plt.show()