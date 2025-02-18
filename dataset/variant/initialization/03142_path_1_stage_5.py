import matplotlib.pyplot as plt
import numpy as np

culinary_techniques = [
    "Smoking",
    "Fermentation",
    "Sous Vide",
    "Pickling",
    "Braising",
    "Sautéing",
    "Grilling",
    "Poaching",
    "Roasting",
    "Steaming",
    "Deep Frying",
    "Broiling",
]

popularity_scores = [20, 25, 15, 18, 45, 40, 50, 30, 17, 35, 28, 42]

colors = ['#7fcdbb', '#b30000', '#225ea8', '#e34a33', '#1d91c0', 
          '#c7e9b4', '#253494', '#fc8d59', '#081d58', '#41b6c4', 
          '#fdae61', '#fee08b']

fig, ax = plt.subplots(figsize=(12, 8))
x_pos = np.arange(len(culinary_techniques))

ax.bar(x_pos, popularity_scores, color=colors, edgecolor='black', alpha=0.8)
ax.set_xticks(x_pos)
ax.set_xticklabels(culinary_techniques, rotation=45, fontsize=10, fontweight='medium')

ax.set_title('Varied Taste Trends in Gastronomy\nChef Preferences Globally', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Methodologies', fontsize=12)
ax.set_ylabel('Score of Popularity (%)', fontsize=12)

for i in range(len(popularity_scores)):
    ax.text(i, popularity_scores[i] + 1, f'{popularity_scores[i]}%', ha='center', color='black', fontsize=10)

plt.tight_layout()
plt.show()