import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

stress_levels = np.array([2, 3, 5, 7, 8, 6, 4, 9])
artworks_produced = np.array([12, 15, 20, 24, 22, 19, 17, 26])

corr_coefficient, _ = pearsonr(stress_levels, artworks_produced)
corr_text = f"Pearson Correlation: {corr_coefficient:.2f}"

plt.figure(figsize=(12, 8))
# Changed colors of the scatter plot
plt.scatter(stress_levels, artworks_produced, color='teal', s=150, alpha=0.6, edgecolor='black')

plt.title("Creative Output vs. Stress Parameters\nExploration with Hypothetical Creators", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Stress Index (1-10)", fontsize=14)
plt.ylabel("Monthly Art Creations", fontsize=14)

for i, txt in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
    plt.annotate(f"Creator {txt}", (stress_levels[i], artworks_produced[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

plt.text(6, 15, corr_text, fontsize=12, color='darkred', bbox=dict(facecolor='white', edgecolor='darkred', pad=5.0))

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()