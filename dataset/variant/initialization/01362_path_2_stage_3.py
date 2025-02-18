import matplotlib.pyplot as plt
import numpy as np

cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern"]
popularity_scores = np.array([70, 85, 60, 55, 75, 40, 45, 35, 65, 50])

colors = ['#FF5733', '#C70039', '#581845', '#DAF7A6', '#92A8D1', '#900C3F', '#B833FF', '#FFC0CB', '#FFC300', '#FF6F61']

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(cuisines, popularity_scores, color=colors, edgecolor='grey', linestyle=':', hatch='//')

ax.set_title('Culinary Adventures: Popularity of International Cuisines Among City Residents', fontsize=16, fontweight='light', ha='left')
ax.set_ylabel('Popularity Score', fontsize=14, color='navy')
ax.set_xlabel('Cuisines', fontsize=14, color='navy')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{bar.get_height()}', 
            ha='center', va='top', color='navy', fontsize=10, fontweight='light')

ax.yaxis.grid(True, linestyle='-', alpha=0.3)

ax.spines['top'].set_color('none')
ax.spines['right'].set_linewidth(2)

ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()