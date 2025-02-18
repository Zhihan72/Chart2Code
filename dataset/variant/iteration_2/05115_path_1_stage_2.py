import matplotlib.pyplot as plt
import numpy as np

interest = [20, 10, 25, 15, 30]

colors = ['#99ff99', '#ff6666', '#66b3ff', '#ffcc99', '#ff9999']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, autotexts = ax.pie(
    interest, 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    explode=(0, 0, 0, 0, 0.1),
    shadow=True
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

plt.tight_layout()
plt.show()