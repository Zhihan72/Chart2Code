import matplotlib.pyplot as plt
import numpy as np

elements_discovered = np.array([35, 20, 15, 18, 12, 25, 10])
colors = ['#32CD32', '#8A2BE2', '#FF4500', '#FF69B4', '#1E90FF', '#FFD700', '#6A5ACD']

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(
    elements_discovered,
    colors=colors,
    startangle=140,
    wedgeprops=dict(edgecolor='w')
)

plt.show()