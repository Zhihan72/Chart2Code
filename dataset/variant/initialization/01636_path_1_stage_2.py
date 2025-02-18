import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

years = np.arange(2013, 2023)
ai_adoption = np.array([5, 10, 20, 30, 40, 50, 55, 60, 70, 75])
blockchain_adoption = np.array([2, 8, 15, 22, 30, 28, 26, 24, 22, 20])
iot_adoption = np.array([10, 15, 25, 35, 45, 55, 53, 51, 50, 48])
ar_adoption = np.array([3, 7, 10, 15, 18, 20, 22, 20, 18, 17])

total_adoption = ai_adoption + blockchain_adoption + iot_adoption + ar_adoption
ai_adoption_percentage = (ai_adoption / total_adoption) * 100
blockchain_adoption_percentage = (blockchain_adoption / total_adoption) * 100
iot_adoption_percentage = (iot_adoption / total_adoption) * 100
ar_adoption_percentage = (ar_adoption / total_adoption) * 100

adoption_data = np.vstack([ai_adoption_percentage, blockchain_adoption_percentage, iot_adoption_percentage, ar_adoption_percentage])

fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

colors = cm.viridis(np.linspace(0, 1, 4))
shuffled_colors = [colors[2], colors[0], colors[3], colors[1]]

ax.stackplot(years, adoption_data, colors=shuffled_colors, alpha=0.85)

for i, percentage in enumerate(adoption_data):
    ax.plot(years, np.cumsum(adoption_data, axis=0)[i], marker='o', markersize=5, linestyle='None', label='_nolegend_', color=shuffled_colors[i])

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()