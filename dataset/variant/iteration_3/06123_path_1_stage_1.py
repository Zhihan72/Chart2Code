import matplotlib.pyplot as plt
import numpy as np

focus_areas = ['Artificial Intelligence', 'Fintech', 'HealthTech', 'EdTech', 'Blockchain', 'IoT', 'Cybersecurity']
percentages = [25, 20, 18, 15, 12, 7, 3]

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C71585', '#7B68EE']

fig, ax = plt.subplots(figsize=(10, 8))
explode = (0.05, 0.05, 0, 0, 0, 0, 0)

ax.pie(percentages, startangle=140, colors=colors, pctdistance=0.85,
       wedgeprops=dict(width=0.3, edgecolor='w'), explode=explode, shadow=True)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()

plt.show()