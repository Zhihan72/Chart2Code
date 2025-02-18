import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
coffee_consumption = np.array([1, 2, 1, 3, 2, 3, 4, 2, 5, 6, 5, 4, 3, 6,
                               5, 5, 4, 7, 6, 7, 8, 7, 9, 8, 10, 9, 7, 8, 7, 6])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(days, coffee_consumption, label='Coffee Consumption', color='navy', linewidth=2)

plt.title("Coffee Consumption Over Days", fontsize=18, fontweight='bold', pad=25)
ax1.set_xlabel("Days", fontsize=12, fontweight='bold')
ax1.set_ylabel("Coffee Consumption (cups)", fontsize=12, fontweight='bold')

highlight_days = [10, 15, 22]
for day in highlight_days:
    ax1.annotate(f'Day {day}', 
                (day, coffee_consumption[day-1]), 
                textcoords="offset points", 
                xytext=(-10,10), 
                ha='right', 
                fontsize=11, 
                arrowprops=dict(arrowstyle='->', color='black'))

ax1.grid(visible=True, linestyle=':', alpha=0.8)
scatter_legend = ax1.legend(loc='upper left', fontsize=11, frameon=False)

plt.tight_layout()

plt.show()