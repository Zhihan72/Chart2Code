import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

apples_yield = [15, 22, 50, 10, 40, 25, 65, 12, 55, 15, 18, 30]
oranges_yield = [55, 35, 28, 45, 30, 25, 60, 45, 30, 50, 35, 30]
grapes_yield = [30, 80, 5, 12, 18, 70, 75, 60, 8, 50, 30, 18]

fig, ax = plt.subplots(figsize=(12, 7))

uniform_color = '#4682B4'

ax.plot(months, apples_yield, marker='o', linestyle='-', color=uniform_color, linewidth=2, label='Apples')
ax.plot(months, oranges_yield, marker='o', linestyle='-', color=uniform_color, linewidth=2, label='Oranges')
ax.plot(months, grapes_yield, marker='o', linestyle='-', color=uniform_color, linewidth=2, label='Grapes')

ax.set_title("Fruit Yields", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Mnth', fontsize=14)
ax.set_ylabel('Yield (t)', fontsize=14)
ax.set_xticks(months)
ax.set_xticklabels(month_names, rotation=45, ha='right')

ax.annotate('Peak', xy=(7, 65), xytext=(5, 75),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color=uniform_color)
ax.annotate('Peak', xy=(1, 55), xytext=(3, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color=uniform_color)
ax.annotate('Peak', xy=(2, 80), xytext=(4, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color=uniform_color)

ax.axvspan(6, 9, color='yellow', alpha=0.1)
ax.text(7.5, 90, 'Summer', fontsize=12, color='darkorange', ha='center')

plt.tight_layout()
plt.legend()
plt.show()