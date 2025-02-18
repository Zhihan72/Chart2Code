import matplotlib.pyplot as plt
import numpy as np

# Altered distribution by switching some elements' positions
distribution = np.array([25, 10, 30, 15, 20])
colors = ['#FFC300', '#900C3F', '#DAF7A6', '#33FFEC', '#FF5733']
explode = (0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(distribution, startangle=90,
       colors=colors, explode=explode, 
       wedgeprops=dict(width=0.4, edgecolor='black'))

ax.grid(True)
ax.legend(['A', 'B', 'C', 'D', 'E'], loc='upper left')

plt.show()