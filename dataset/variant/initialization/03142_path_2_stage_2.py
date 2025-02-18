import matplotlib.pyplot as plt
import numpy as np

culinary_techniques = [
    "Sous Vide",
    "Fermentation",
    "Smoking",
    "Pickling",
    "Braising",
    "Sautéing",
    "Grilling",
    "Poaching",
    "Steaming",
    "Roasting",
    "Frying",
    "Blanching"
]

popularity_scores = [15, 25, 20, 18, 17, 40, 50, 30, 35, 45, 22, 10]

colors = ['#7fcdbb', '#fdbb84', '#253494', '#c7e9b4', '#fee8c8', 
          '#e34a33', '#1d91c0', '#41b6c4', '#081d58', '#b30000',
          '#fc8d59', '#225ea8']  # Shuffled manually

fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques))

ax.barh(y_pos, popularity_scores, color=colors, edgecolor='black', alpha=0.8)

ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques, fontsize=10, fontweight='medium')
ax.invert_yaxis()

ax.set_title('Top Culinary Techniques in World Cuisines\nBased on Global Chef Survey', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Popularity Score (%)', fontsize=12)
ax.set_ylabel('Culinary Techniques', fontsize=12)

for i in range(len(popularity_scores)):
    ax.text(popularity_scores[i] + 1, i, f'{popularity_scores[i]}%', 
            va='center', color='black', fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()