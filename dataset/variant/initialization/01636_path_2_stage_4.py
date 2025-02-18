import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

# Adjusted the adoption values randomly within the groups.
ai_adoption = np.array([10, 5, 30, 20, 50, 40, 55, 75, 60, 70])
blockchain_adoption = np.array([8, 2, 22, 15, 28, 30, 24, 26, 20, 22])
iot_adoption = np.array([15, 10, 35, 25, 55, 45, 51, 50, 48, 53])
ar_adoption = np.array([7, 3, 15, 10, 20, 18, 20, 22, 17, 18])

total_adoption = ai_adoption + blockchain_adoption + iot_adoption + ar_adoption

ai_adoption_percentage = (ai_adoption / total_adoption) * 100
blockchain_adoption_percentage = (blockchain_adoption / total_adoption) * 100
iot_adoption_percentage = (iot_adoption / total_adoption) * 100
ar_adoption_percentage = (ar_adoption / total_adoption) * 100

adoption_data = np.vstack([ai_adoption_percentage, blockchain_adoption_percentage, iot_adoption_percentage, ar_adoption_percentage])

fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

ax.stackplot(years, adoption_data, colors=colors, alpha=0.85)

for i, percentage in enumerate(adoption_data):
    ax.plot(years, np.cumsum(adoption_data, axis=0)[i], marker='o', markersize=5, linestyle='None', color=colors[i])

ax.set_title('Tech Landscape Over Ten Years:\nAdoption Rates (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Adoption Rate (%) Distribution', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.annotate('AI Overcomes Peers', xy=(2017, 50), xytext=(2015, 70), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='navy')

plt.tight_layout()
plt.show()