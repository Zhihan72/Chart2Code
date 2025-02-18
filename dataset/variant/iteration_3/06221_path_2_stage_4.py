import matplotlib.pyplot as plt
import numpy as np

genres = ["Hidden Treasures", "Unveiled Truths", "Star Lore", "Chimerical Realms", "Conundrum Whodunits"]
total_sales = np.array([1735, 1670, 1320, 1200, 995])

sorted_indices = np.argsort(total_sales)[::-1]

sorted_genres = np.array(genres)[sorted_indices]
sorted_sales = total_sales[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(sorted_genres, sorted_sales, color=['dodgerblue', 'orangered', 'green', 'purple', 'gold'], alpha=0.85)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel('Literary Category', fontsize=12)
ax.set_ylabel('Volume Sold (x1000)', fontsize=12)
ax.set_title('Compendium of Book Exchanges (2010-2020)', fontsize=16, fontweight='bold')

for i, val in enumerate(sorted_sales):
    ax.text(i, val + 5, str(val), ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()