import matplotlib.pyplot as plt
import numpy as np

countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
tea_consumption = [2.5, 4.2, 1.8, 3.6, 2.9]
coffee_consumption = [3.0, 5.0, 2.2, 4.5, 3.4]

bar_width = 0.35
y_pos = np.arange(len(countries))

fig, ax = plt.subplots(figsize=(10, 6))

tea_bars = ax.barh(y_pos, tea_consumption, color='#FF6347', alpha=0.9, height=bar_width, label='Tea', edgecolor='black', linestyle='-.')
coffee_bars = ax.barh(y_pos + bar_width, coffee_consumption, color='#4682B4', alpha=0.9, height=bar_width, label='Coffee', edgecolor='black', linestyle='--')

for bar in tea_bars:
    width = bar.get_width()
    ax.text(width + 0.05, bar.get_y() + bar.get_height() / 2.0,
            f'{width:.1f}', va='center', ha='left', fontsize=11, fontweight='bold')

for bar in coffee_bars:
    width = bar.get_width()
    ax.text(width + 0.05, bar.get_y() + bar.get_height() / 2.0,
            f'{width:.1f}', va='center', ha='left', fontsize=11, fontstyle='italic')

ax.set_title('Average Annual Beverage Consumption\nPer Person by Country', fontsize=18, fontweight='bold', pad=15)
ax.set_ylabel('Country', fontsize=13, fontweight='light')
ax.set_xlabel('Consumption (kg/person/year)', fontsize=13, fontweight='light')

ax.set_yticks(y_pos + bar_width / 2)
ax.set_yticklabels(countries, fontsize=11)

ax.xaxis.grid(True, linestyle=':', linewidth=0.7, alpha=0.6)
ax.yaxis.grid(True, linestyle=':', linewidth=0.7, alpha=0.5)

ax.legend(loc='lower right', fontsize=11, shadow=True)

plt.tight_layout()
plt.show()