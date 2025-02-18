import matplotlib.pyplot as plt
import numpy as np

sectors = ['Res', 'Agri', 'Ind', 'Rec', 'Com']
water_usage = np.array([120, 80, 50, 30, 70])
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

fig, ax = plt.subplots(figsize=(9, 9))

# Change: Removed wedgeprops to convert donut into a standard pie chart
wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    colors=colors,
    startangle=90
)

plt.setp(texts, size=12, weight='bold', va='center')
plt.setp(autotexts, size=12, color='white', weight='bold')

# Change: Removed center_circle as it's not needed for a standard pie chart

ax.axis('equal')

plt.show()