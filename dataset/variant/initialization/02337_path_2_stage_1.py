import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

apples_yield = [10, 12, 15, 18, 22, 30, 50, 65, 55, 40, 25, 15]
oranges_yield = [30, 45, 60, 55, 50, 45, 35, 30, 28, 25, 30, 35]
grapes_yield = [5, 8, 12, 18, 30, 50, 60, 75, 80, 70, 50, 30]

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(months, apples_yield, marker='o', linestyle='-', color='#8B0000', label='Apples', linewidth=2)
ax.plot(months, oranges_yield, marker='o', linestyle='-', color='#FF4500', label='Oranges', linewidth=2)
ax.plot(months, grapes_yield, marker='o', linestyle='-', color='#8A2BE2', label='Grapes', linewidth=2)

ax.set_title("Seasonal Trends in Fruit Harvesting", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Yield (tons)', fontsize=14)
ax.set_xticks(months)
ax.set_xticklabels(month_names, rotation=45, ha='right')

ax.legend(loc='upper right', title="Fruit Type", fontsize=12)
ax.grid(linestyle='--', alpha=0.5)

ax.annotate('Peak Harvest', xy=(8, 65), xytext=(5, 75),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color='#8B0000')
ax.annotate('Peak Harvest', xy=(2, 45), xytext=(3, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color='#FF4500')
ax.annotate('Peak Harvest', xy=(9, 80), xytext=(10, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color='#8A2BE2')

ax.axvspan(6, 9, color='yellow', alpha=0.1)
ax.text(7.5, 90, 'Summer Harvest Season', fontsize=12, color='#FF4500', ha='center')

plt.tight_layout()
plt.show()