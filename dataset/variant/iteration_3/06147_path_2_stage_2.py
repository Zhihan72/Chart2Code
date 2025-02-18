import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
beverages = ['Coffee', 'Tea', 'Juice']

coffee_preference = np.array([40, 35, 30, 25, 15])
tea_preference = np.array([20, 25, 30, 35, 40])
juice_preference = np.array([40, 40, 40, 40, 45])

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.6
bar_positions = np.arange(len(age_groups))

coffee_start = -coffee_preference / 2
tea_start = np.zeros_like(tea_preference)
juice_start = coffee_preference / 2

ax.bar(bar_positions, -coffee_preference, bar_width, bottom=coffee_start, color='#8B4513')
ax.bar(bar_positions, tea_preference, bar_width, bottom=tea_start, color='#CD853F')
ax.bar(bar_positions, juice_preference, bar_width, bottom=juice_start, color='#FBC02D')

for bars in ax.containers:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{abs(height)}%',
                    xy=(bar.get_x() + bar.get_width() / 2, (bar.get_y() + bar.get_y() + height) / 2),
                    xytext=(0, 0), 
                    textcoords='offset points',
                    ha='center', va='center', fontsize=10, color='black')

ax.set_xticks(bar_positions)
ax.set_xticklabels(age_groups)

plt.axhline(y=0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()