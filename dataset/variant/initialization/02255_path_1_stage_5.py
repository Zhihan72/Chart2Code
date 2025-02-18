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

# Set vert=False to change to a horizontal box plot
ax.boxplot(growth_data, vert=False, notch=True, patch_artist=True, labels=sectors)

ax.set_title('Tech Sector Growth\n(5-Yr Data)', fontsize=14, fontweight='bold')
ax.set_xlabel('Growth (%)', fontsize=12)  # Swapping labels for horizontal orientation
ax.set_ylabel('Sectors', fontsize=12)     # Swapping labels for horizontal orientation

plt.yticks(rotation=15)  # Rotate sector labels
plt.tight_layout()
plt.show()