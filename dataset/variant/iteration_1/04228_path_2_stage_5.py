import matplotlib.pyplot as plt
import numpy as np

zone_acres = np.array([20, 25, 15, 30, 5, 5])
# New set of colors to replace the original ones
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33']
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    zone_acres, 
    explode=explode, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=140
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.axis('equal')

plt.show()