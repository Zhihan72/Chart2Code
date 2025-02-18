import matplotlib.pyplot as plt
import numpy as np

# Including original and additional culinary techniques
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
    "Deep Frying",  # New technique
    "Broiling",     # New technique
]

# Updated popularity scores for the original and new techniques
popularity_scores = [20, 25, 15, 18, 45, 40, 50, 30, 17, 35, 28, 42]

# Updated set of colors for the original and new techniques
colors = ['#7fcdbb', '#b30000', '#225ea8', '#e34a33', '#1d91c0', 
          '#c7e9b4', '#253494', '#fc8d59', '#081d58', '#41b6c4', 
          '#fdae61', '#fee08b']  # New colors for newly added techniques

fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques))

ax.barh(y_pos, popularity_scores, color=colors, edgecolor='black', alpha=0.8)
ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques, fontsize=10, fontweight='medium')
ax.invert_yaxis()

ax.set_title('Varied Taste Trends in Gastronomy\nChef Preferences Globally', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Score of Popularity (%)', fontsize=12)
ax.set_ylabel('Methodologies', fontsize=12)

for i in range(len(popularity_scores)):
    ax.text(popularity_scores[i] + 1, i, f'{popularity_scores[i]}%', va='center', color='black', fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()