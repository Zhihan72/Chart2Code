import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
precipitation_sunnyville = np.array([52, 32, 85, 34, 61, 42, 43, 22, 74, 78, 15, 20])
precipitation_rainytown = np.array([160, 150, 190, 140, 160, 150, 160, 130, 180, 180, 120, 130])
temperature_sunnyville = np.array([12, 20, 28, 16, 24, 18, 15, 28, 10, 22, 12, 25])
temperature_rainytown = np.array([6, 12, 6, 16, 13, 18, 9, 21, 5, 22, 9, 20])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Shuffled color assignments
scatter1 = ax1.scatter(months, precipitation_sunnyville, color='lightcoral', marker='x', s=120, edgecolors='brown')
scatter2 = ax1.scatter(months, precipitation_rainytown, color='darkcyan', marker='D', s=120, edgecolors='black')

ax2 = ax1.twinx()
scatter3 = ax2.scatter(months, temperature_sunnyville, color='orchid', marker='*', s=120, edgecolors='navy')
scatter4 = ax2.scatter(months, temperature_rainytown, color='darkorange', marker='o', s=120, edgecolors='black')

ax1.grid(True, linestyle='-', color='gray', alpha=0.6)
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months)
ax1.tick_params(axis='x', colors='black', rotation=30)
ax1.tick_params(axis='y', colors='lightcoral')
ax2.tick_params(axis='y', colors='orchid')

scatter1.set_alpha(0.75)
scatter2.set_alpha(0.75)
scatter3.set_alpha(0.75)
scatter4.set_alpha(0.75)

plt.tight_layout()
plt.show()