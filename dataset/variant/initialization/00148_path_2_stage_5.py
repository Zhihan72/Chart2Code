import matplotlib.pyplot as plt
import numpy as np

# Original sectors and water usage data
sectors = ['Res', 'Agri', 'Ind', 'Rec', 'Com']
water_usage = np.array([120, 80, 50, 30, 70])

# Adding new made-up data series
# New sectors added: 'Edu', 'Tech', 'Trans'
new_sectors = ['Edu', 'Tech', 'Trans']
new_water_usage = np.array([40, 60, 20])

# Combine the original and new data
all_sectors = sectors + new_sectors
all_water_usage = np.concatenate((water_usage, new_water_usage))

colors = ['#66c2a5'] * len(all_water_usage)  # Keeping the same color for all

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    all_water_usage,
    labels=all_sectors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    colors=colors,
    startangle=90
)

plt.setp(texts, size=12, weight='bold', va='center')
plt.setp(autotexts, size=12, color='white', weight='bold')

ax.axis('equal')

plt.show()