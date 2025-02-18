import matplotlib.pyplot as plt
import numpy as np

retreats = ['Mars V.', 'Jup. H.', 'Ven. O.', 'Sat. R.', 'Nep. S.']
intellectual_diversity = np.array([85, 55, 70, 60, 80])  # Manually altered to preserve dimensional structure

sorted_indices = np.argsort(intellectual_diversity)
retreats_sorted = [retreats[i] for i in sorted_indices]
intellectual_diversity_sorted = intellectual_diversity[sorted_indices]

plt.figure(figsize=(10, 6))
plt.barh(retreats_sorted, intellectual_diversity_sorted, color='skyblue', edgecolor='gray', linestyle='-', linewidth=1.5)

plt.title("Intellectual Diversity at Writers' Retreats", fontsize=16, fontweight='bold', style='italic')
plt.xlabel('Intellectual Diversity', fontsize=12, color='darkred')
plt.ylabel('Retreat Locations', fontsize=12, color='darkred')

plt.grid(True, linestyle='-.', linewidth=0.8, alpha=0.4)

plt.legend(['Diversity Score'], loc='lower right', fontsize=10, frameon=True, shadow=True, edgecolor='black')

plt.tight_layout()

plt.show()