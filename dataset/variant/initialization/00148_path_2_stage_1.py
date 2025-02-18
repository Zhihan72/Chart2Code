import matplotlib.pyplot as plt
import numpy as np

sectors = ['Residential', 'Agricultural', 'Industrial', 'Recreational', 'Commercial']
water_usage = np.array([120, 80, 50, 30, 70])
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

plt.setp(texts, size=12, weight='bold', va='center')
plt.setp(autotexts, size=12, color='white', weight='bold')

center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

ax.axis('equal')

plt.show()