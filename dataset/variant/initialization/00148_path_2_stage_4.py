import matplotlib.pyplot as plt
import numpy as np

sectors = ['Res', 'Agri', 'Ind', 'Rec', 'Com']
water_usage = np.array([120, 80, 50, 30, 70])
single_color = '#66c2a5'

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    colors=[single_color] * len(water_usage),
    startangle=90
)

plt.setp(texts, size=12, weight='bold', va='center')
plt.setp(autotexts, size=12, color='white', weight='bold')

ax.axis('equal')

plt.show()