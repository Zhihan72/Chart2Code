import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

copenhagen_commuters = np.array([18, 22, 25, 35, 40, 45, 50, 48, 42, 37, 30, 25])
amsterdam_commuters = np.array([20, 24, 28, 36, 42, 48, 52, 50, 45, 38, 32, 28])
portland_commuters = np.array([15, 18, 21, 25, 30, 35, 37, 36, 33, 28, 22, 18])
barcelona_commuters = np.array([10, 12, 15, 18, 22, 26, 30, 28, 25, 20, 16, 12])
berlin_commuters = np.array([12, 14, 19, 22, 26, 32, 35, 33, 29, 24, 20, 15])

fig, ax = plt.subplots(figsize=(12, 8))

ax.scatter(months, copenhagen_commuters, color='green', marker='s', s=70, alpha=0.5, edgecolors='r', label='Copenhagen')
ax.scatter(months, amsterdam_commuters, color='orange', marker='^', s=80, alpha=0.6, edgecolors='g', label='Amsterdam')
ax.scatter(months, portland_commuters, color='purple', marker='D', s=90, alpha=0.7, edgecolors='b', label='Portland')
ax.scatter(months, barcelona_commuters, color='red', marker='o', s=60, alpha=0.4, edgecolors='c', label='Barcelona')
ax.scatter(months, berlin_commuters, color='brown', marker='v', s=95, alpha=0.8, edgecolors='m', label='Berlin')

ax.grid(False)

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()