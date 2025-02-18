import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Feb', 'Jan', 'Mar', 'Oct', 'Jul', 'Jun', 'Dec', 'May', 'Apr', 'Sep', 'Nov', 'Aug'])
new_york_temps = np.array([-1, 0, 6, 13, 18, 23, 26, 25, 21, 14, 8, 2])
los_angeles_temps = np.array([14, 15, 16, 18, 19, 21, 24, 24, 23, 20, 17, 14])
chicago_temps = np.array([-5, -2, 4, 11, 17, 22, 25, 24, 20, 13, 6, -1])

fig, ax = plt.subplots(figsize=(12, 7))

# Stylistically altered plots
ax.plot(months, new_york_temps, marker='x', linestyle='--', color='purple', label='NYC')
ax.plot(months, los_angeles_temps, marker='D', linestyle='-', color='brown', label='LA')
ax.plot(months, chicago_temps, marker='*', linestyle=':', color='red', label='Chi-Town')

ax.set_title("2023 Temperature Profiles", fontsize=16, fontweight='normal', pad=15)
ax.set_xlabel("Monthly Distribution", fontsize=12)
ax.set_ylabel("Average Temperature (°C)", fontsize=12)

# Updated legend styling
ax.legend(loc='lower left', fontsize=9, title='Cities', title_fontsize='11')

# Altered grid and background settings
ax.grid(True, linestyle=':', alpha=0.5)
ax.set_facecolor('#eaeaea')

highlight_style = dict(size=10, color='b', weight='bold')
ax.annotate('Max', xy=(4, 26), xytext=(5, 28),
            arrowprops=dict(facecolor='black', shrink=0.1), **highlight_style)
ax.annotate('Min', xy=(1, -1), xytext=(2, -7),
            arrowprops=dict(facecolor='black', shrink=0.1), **highlight_style)
ax.annotate('Max', xy=(5, 24), xytext=(6, 26),
            arrowprops=dict(facecolor='black', shrink=0.1), **highlight_style)
ax.annotate('Min', xy=(2, 14), xytext=(3, 11),
            arrowprops=dict(facecolor='black', shrink=0.1), **highlight_style)
ax.annotate('Max', xy=(4, 25), xytext=(5, 27),
            arrowprops=dict(facecolor='black', shrink=0.1), **highlight_style)
ax.annotate('Min', xy=(1, -5), xytext=(2, -11),
            arrowprops=dict(facecolor='black', shrink=0.1), **highlight_style)

plt.tight_layout()
plt.show()