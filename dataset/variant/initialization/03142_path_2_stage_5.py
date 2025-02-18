import matplotlib.pyplot as plt
import numpy as np

culinary_techniques = [
    "Blanching",  # Randomly rearranged
    "Smoking",
    "Frying",
    "Sous Vide",
    "Grilling",
    "Pickling",
    "Braising",
    "Sautéing",
    "Fermentation",
    "Roasting",
    "Poaching",
    "Steaming"
]

popularity_scores = [10, 20, 22, 15, 50, 18, 17, 40, 25, 45, 30, 35]

colors = ['#b30000', '#c7e9b4', '#fc8d59', '#7fcdbb', '#1d91c0',
          '#fdbb84', '#e34a33', '#fee8c8', '#253494', '#b30000', 
          '#41b6c4', '#081d58']

data = list(zip(popularity_scores, culinary_techniques, colors))
data_sorted = sorted(data, key=lambda x: x[0])

popularity_scores_sorted, culinary_techniques_sorted, colors_sorted = zip(*data_sorted)

fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques_sorted))

ax.barh(y_pos, popularity_scores_sorted, color=colors_sorted, edgecolor='grey', alpha=0.9)

ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques_sorted, fontsize=10, fontweight='medium')
ax.invert_yaxis()

ax.set_title('Favored Cooking Methods Globally\nSurveyed by World Chefs', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Score of Popularity (%)', fontsize=12, color='darkred')
ax.set_ylabel('Cooking Techniques', fontsize=12, color='darkblue')

for i in range(len(popularity_scores_sorted)):
    ax.text(popularity_scores_sorted[i] + 1, i, f'{popularity_scores_sorted[i]}%', 
            va='center', color='purple', fontsize=10)

ax.grid(axis='x', linestyle='-.', alpha=0.7)

plt.tight_layout()

plt.show()