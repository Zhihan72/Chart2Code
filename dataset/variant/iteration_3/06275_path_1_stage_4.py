import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
avg_daily_hours_online = np.array([1.5, 2.3, 3.2, 4.0, 4.8, 5.5, 6.1])

fig, ax = plt.subplots(figsize=(10, 6))

# Updating plot style: changing color, marker type, and line style
color = 'tab:green'
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Hours', fontsize=14, color=color)
ax.plot(years, avg_daily_hours_online, color=color, marker='o', markersize=10, 
        linestyle='-', linewidth=2.5, label='Daily Hours Usage')
ax.tick_params(axis='y', labelcolor=color)

# Title with different style
plt.title('Online Activity Over Years', fontsize=16, style='italic')

# Grid style changed
ax.grid(True, linestyle='-', color='gray', alpha=0.3)

# Legend location and style updated
ax.legend(loc='lower right', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()