import matplotlib.pyplot as plt
import numpy as np

culinary_techniques = [
    "Grilling",  # Randomly rearranged
    "Fermentation", 
    "Smoking", 
    "Pickling",  
    "Sautéing",  
    "Sous Vide",  
    "Braising",  
    "Frying",   
    "Steaming", 
    "Poaching",  
    "Roasting",  
    "Blanching"  
]

popularity_scores = [50, 25, 20, 18, 40, 15, 17, 22, 35, 30, 45, 10]

colors = ['#1d91c0', '#fdbb84', '#253494', '#c7e9b4', '#fee8c8', 
          '#7fcdbb', '#e34a33', '#fc8d59', '#41b6c4', '#225ea8',
          '#b30000', '#081d58']

data = list(zip(popularity_scores, culinary_techniques, colors))
data_sorted = sorted(data, key=lambda x: x[0])

popularity_scores_sorted, culinary_techniques_sorted, colors_sorted = zip(*data_sorted)

fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques_sorted))

ax.barh(y_pos, popularity_scores_sorted, color=colors_sorted, edgecolor='black', alpha=0.8)

ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques_sorted, fontsize=10, fontweight='medium')
ax.invert_yaxis()

ax.set_title('Favored Cooking Methods Globally\nSurveyed by World Chefs', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Score of Popularity (%)', fontsize=12)
ax.set_ylabel('Cooking Techniques', fontsize=12)

for i in range(len(popularity_scores_sorted)):
    ax.text(popularity_scores_sorted[i] + 1, i, f'{popularity_scores_sorted[i]}%', 
            va='center', color='black', fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()