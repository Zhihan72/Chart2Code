import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Updated bicycle commuter data (thousands) with Berlin data added
copenhagen_commuters = np.array([18, 22, 25, 35, 40, 45, 50, 48, 42, 37, 30, 25])
amsterdam_commuters = np.array([20, 24, 28, 36, 42, 48, 52, 50, 45, 38, 32, 28])
portland_commuters = np.array([15, 18, 21, 25, 30, 35, 37, 36, 33, 28, 22, 18])
barcelona_commuters = np.array([10, 12, 15, 18, 22, 26, 30, 28, 25, 20, 16, 12])
berlin_commuters = np.array([12, 14, 19, 22, 26, 32, 35, 33, 29, 24, 20, 15])

fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data for each city with different styles, including Berlin
ax.scatter(months, copenhagen_commuters, label='Copenhagen', color='skyblue', marker='o', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, amsterdam_commuters, label='Amsterdam', color='lightgreen', marker='s', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, portland_commuters, label='Portland', color='salmon', marker='^', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, barcelona_commuters, label='Barcelona', color='orchid', marker='D', s=100, alpha=0.7, edgecolors='k')
ax.scatter(months, berlin_commuters, label='Berlin', color='gold', marker='v', s=100, alpha=0.7, edgecolors='k')

ax.set_title('Urban Buzz: Bicycle Commute Trends Across\nFive Major Cities in 2023', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Bicycle Commuters (in thousands)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title='Cities', fontsize=12, loc='upper left', title_fontsize='13', frameon=False)

plt.tight_layout()
plt.show()