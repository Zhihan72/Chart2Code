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

ax.scatter(months, copenhagen_commuters, color='skyblue', marker='o', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, amsterdam_commuters, color='lightgreen', marker='s', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, portland_commuters, color='salmon', marker='^', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, barcelona_commuters, color='orchid', marker='D', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, berlin_commuters, color='gold', marker='v', s=100, alpha=0.7, edgecolors='k')

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()