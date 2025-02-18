import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

# Define adoption data for each technology
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

# New set of custom colors for each technology
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

# Altered labels for the chart
ax.stackplot(years, adoption_data, labels=['Artificial Intelligence', 'Distributed Ledger Tech', 'Internet-Things', 'Augmented Reality'], colors=colors, alpha=0.85)

for i, percentage in enumerate(adoption_data):
    ax.plot(years, np.cumsum(adoption_data, axis=0)[i], marker='o', markersize=5, linestyle='None', label='_nolegend_', color=colors[i])

ax.set_title('Tech Landscape Over Ten Years:\nAdoption Rates (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Adoption Rate (%) Distribution', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.annotate('AI Overcomes Peers', xy=(2017, 50), xytext=(2015, 70), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='navy')

ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), frameon=False)

ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()