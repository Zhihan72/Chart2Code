import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
month_names = ['Apr', 'Feb', 'Nov', 'Jun', 'Sep', 'Jan', 
               'Aug', 'Mar', 'Oct', 'Jul', 'May', 'Dec']

# Randomly altered yields
apples_yield = [22, 65, 30, 40, 55, 12, 25, 50, 15, 18, 15, 10]
oranges_yield = [50, 35, 30, 45, 30, 28, 60, 25, 45, 30, 55, 35]
grapes_yield = [18, 5, 30, 70, 75, 60, 50, 8, 12, 30, 80, 50]

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(months, apples_yield, marker='s', linestyle='--', color='#8B0000', label='Apples', linewidth=2)
ax.plot(months, oranges_yield, marker='^', linestyle='-.', color='#FF4500', label='Oranges', linewidth=2)
ax.plot(months, grapes_yield, marker='d', linestyle=':', color='#8A2BE2', label='Grapes', linewidth=2)

ax.set_title("Harvesting Seasonal Trends in Fruits", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time of Year', fontsize=14)
ax.set_ylabel('Tons of Yield', fontsize=14)
ax.set_xticks(months)
ax.set_xticklabels(month_names, rotation=45, ha='right')

ax.legend(loc='lower left', title="Harvest of Fruits", fontsize=12)

ax.grid(linestyle='-', linewidth=0.6, alpha=0.7)

ax.annotate('Intensive Picking', xy=(8, 50), xytext=(5, 62),
            arrowprops=dict(facecolor='grey', arrowstyle='->'),
            fontsize=11, color='#8B0000')
ax.annotate('High Picking', xy=(2, 60), xytext=(3, 70),
            arrowprops=dict(facecolor='grey', arrowstyle='->'),
            fontsize=11, color='#FF4500')
ax.annotate('Peak Collection', xy=(9, 80), xytext=(10, 88),
            arrowprops=dict(facecolor='grey', arrowstyle='->'),
            fontsize=11, color='#8A2BE2')

ax.axvspan(6, 9, color='green', alpha=0.1)
ax.text(7.5, 85, 'Season of Summer Harvest', fontsize=12, color='#FF4500', ha='center')

plt.tight_layout()
plt.show()