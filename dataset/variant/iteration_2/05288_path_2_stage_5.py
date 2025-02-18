import matplotlib.pyplot as plt
import numpy as np

allocations = [25, 22, 17, 12, 14, 10]
colors = ['#66b3ff','#ff9999','#ffcc99','#99ff99','#ffb3e6','#c2c2f0']

plt.figure(figsize=(12, 7))

ax1 = plt.subplot(121)
ax1.pie(
    allocations, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(width=0.3)
)

quarter_allocations = [
    [6, 6, 3, 4, 3, 3],
    [9, 4, 5, 1, 4, 3],
    [8, 6, 3, 3, 4, 2],
    [7, 5, 4, 3, 4, 1]
]
quarter_allocations = np.array(quarter_allocations).T

ax2 = plt.subplot(122)
bar_width = 0.35
ind = np.arange(len(quarter_allocations[0]))
bottom = np.zeros(len(quarter_allocations[0]))

for i, allocation in enumerate(quarter_allocations):
    ax2.bar(
        ind, 
        allocation, 
        bar_width, 
        bottom=bottom, 
        color=colors[i]
    )
    bottom += allocation

plt.show()