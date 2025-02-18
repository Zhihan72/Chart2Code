import matplotlib.pyplot as plt
import numpy as np

zone_acres = np.array([20, 25, 15, 30, 5, 5])
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']
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