import matplotlib.pyplot as plt
import numpy as np

# Titles and labels are manually altered
cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern"]
popularity_scores = np.array([70, 85, 60, 55, 75, 40, 45, 35, 65, 50])

colors = ['#581845', '#B833FF', '#FF5733', '#C70039', '#DAF7A6', '#FFC300', '#92A8D1', '#900C3F', '#FF6F61', '#FFC0CB']

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(cuisines, popularity_scores, color=colors, edgecolor='grey', linestyle=':', hatch='//')

# Randomly alter textual elements
ax.set_title('Cuisine Curiosity: Exploring Global Dishes in the Metro Area', fontsize=16, fontweight='light', ha='left')
ax.set_ylabel('Preference Index', fontsize=14, color='maroon')
ax.set_xlabel('World Cuisines', fontsize=14, color='maroon')

# Randomly altered text properties for bar labels
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{bar.get_height()}',
            ha='center', va='top', color='steelblue', fontsize=10, fontweight='bold')

ax.yaxis.grid(True, linestyle='-', alpha=0.3)

ax.spines['top'].set_color('none')
ax.spines['right'].set_linewidth(2)

ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()