import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
new_york_temps = np.array([14, 0, 8, 2, 18, 23, -1, 21, 26, 13, 6, 25])
los_angeles_temps = np.array([17, 24, 15, 19, 14, 16, 20, 23, 24, 14, 21, 18])
chicago_temps = np.array([20, -2, 6, 24, 4, 25, 13, 17, -5, 11, 22, -1])

fig, ax = plt.subplots(figsize=(12, 7))

# Unified color across all data groups
uniform_color = 'tab:blue'

ax.plot(months, new_york_temps, marker='o', linestyle='-', color=uniform_color, label='New York')
ax.plot(months, los_angeles_temps, marker='^', linestyle='--', color=uniform_color, label='Los Angeles')
ax.plot(months, chicago_temps, marker='s', linestyle='-.', color=uniform_color, label='Chicago')

ax.set_title("Monthly Average Temperature Variations\nAcross Three Major Cities in 2023", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Average Temperature (°C)", fontsize=12)

ax.legend(loc='upper right', fontsize=10, title='Cities', title_fontsize='12')
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f9f9f9')

highlight_style = dict(size=10, color='b', weight='bold')
# Updated arrow colors to match uniform color
ax.annotate('Highest', xy=(8, 26), xytext=(9, 27), arrowprops=dict(facecolor=uniform_color, shrink=0.1), **highlight_style)
ax.annotate('Lowest', xy=(6, -1), xytext=(7, -6), arrowprops=dict(facecolor=uniform_color, shrink=0.1), **highlight_style)
ax.annotate('Highest', xy=(8, 24), xytext=(9, 25), arrowprops=dict(facecolor=uniform_color, shrink=0.1), **highlight_style)
ax.annotate('Lowest', xy=(0, 14), xytext=(1, 10), arrowprops=dict(facecolor=uniform_color, shrink=0.1), **highlight_style)
ax.annotate('Highest', xy=(5, 25), xytext=(6, 26), arrowprops=dict(facecolor=uniform_color, shrink=0.1), **highlight_style)
ax.annotate('Lowest', xy=(8, -5), xytext=(9, -10), arrowprops=dict(facecolor=uniform_color, shrink=0.1), **highlight_style)

plt.tight_layout()
plt.show()