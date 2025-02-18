import matplotlib.pyplot as plt
import numpy as np

sectors = ['AI', 'Cyber', 'FinTech', 'EdTech', 'Health', 'Agri', 'Reg']

ai_growth = [22, 27, 19, 25, 30]
cyber_growth = [12, 18, 15, 22, 17]
fintech_growth = [35, 28, 40, 33, 45]
edtech_growth = [8, 15, 10, 14, 9]
healthtech_growth = [25, 23, 20, 26, 27]
agritech_growth = [10, 14, 12, 11, 16]
regtech_growth = [9, 13, 8, 12, 10]

growth_data = [ai_growth, cyber_growth, fintech_growth, edtech_growth, healthtech_growth, agritech_growth, regtech_growth]

fig, ax = plt.subplots(figsize=(14, 8))

ax.boxplot(growth_data, vert=True, notch=True, patch_artist=True, labels=sectors)

ax.set_title('Tech Sector Growth\n(5-Yr Data)', fontsize=14, fontweight='bold')
ax.set_ylabel('Growth (%)', fontsize=12)
ax.set_xlabel('Sectors', fontsize=12)

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()