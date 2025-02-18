import matplotlib.pyplot as plt
import numpy as np

sectors = ['Artificial Intelligence', 'Cybersecurity', 'Fintech', 'EdTech', 'HealthTech']

ai_growth = [22, 27, 19, 25, 30]
cyber_growth = [12, 18, 15, 22, 17]
fintech_growth = [35, 28, 40, 33, 45]
edtech_growth = [8, 15, 10, 14, 9]
healthtech_growth = [25, 23, 20, 26, 27]

growth_data = [ai_growth, cyber_growth, fintech_growth, edtech_growth, healthtech_growth]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(growth_data, vert=True, notch=True, patch_artist=True,
                labels=sectors, 
                boxprops=dict(facecolor='lightblue', color='darkblue'),
                whiskerprops=dict(color='darkblue'),
                capprops=dict(color='darkblue'),
                medianprops=dict(color='darkblue', linewidth=2),
                flierprops=dict(marker='o', color='darkblue', markersize=8, alpha=0.5))

ax.set_title('Growth Analysis of Tech Startups by Sector\nAnnual Revenue Growth (5-Year Data)', fontsize=14, fontweight='bold')
ax.set_ylabel('Annual Revenue Growth (%)', fontsize=12)
ax.set_xlabel('Technology Sectors', fontsize=12)

ax.yaxis.grid(True, linestyle='--', which='major', color='lightgrey', alpha=0.7)

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()