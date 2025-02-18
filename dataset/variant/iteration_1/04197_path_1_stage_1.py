import matplotlib.pyplot as plt
import numpy as np

# Data: Monthly average temperatures (in °C) for the year
months = np.array(['Feb', 'Jan', 'Mar', 'Oct', 'Jul', 'Jun', 'Dec', 'May', 'Apr', 'Sep', 'Nov', 'Aug'])
new_york_temps = np.array([-1, 0, 6, 13, 18, 23, 26, 25, 21, 14, 8, 2])
los_angeles_temps = np.array([14, 15, 16, 18, 19, 21, 24, 24, 23, 20, 17, 14])
chicago_temps = np.array([-5, -2, 4, 11, 17, 22, 25, 24, 20, 13, 6, -1])

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting data for each city
ax.plot(months, new_york_temps, marker='o', linestyle='-', color='tab:blue', label='NYC')
ax.plot(months, los_angeles_temps, marker='^', linestyle='--', color='tab:orange', label='LA')
ax.plot(months, chicago_temps, marker='s', linestyle='-.', color='tab:green', label='Chi-Town')

# Adding titles and labels with alterations
ax.set_title("Climatic Temperature Variations\nfor 2023", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Months of the Year", fontsize=12)
ax.set_ylabel("Avg Temp (°C)", fontsize=12)

# Customizing the legend
ax.legend(loc='upper right', fontsize=10, title='Metropolis', title_fontsize='12')

# Enhancing grid and background
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f9f9f9')

# Adding annotations for extremes
highlight_style = dict(size=10, color='b', weight='bold')
ax.annotate('Peak', xy=(4, 26), xytext=(5, 27),
            arrowprops=dict(facecolor='blue', shrink=0.1), **highlight_style)
ax.annotate('Low', xy=(1, -1), xytext=(2, -6),
            arrowprops=dict(facecolor='blue', shrink=0.1), **highlight_style)
ax.annotate('Peak', xy=(5, 24), xytext=(6, 25),
            arrowprops=dict(facecolor='orange', shrink=0.1), **highlight_style)
ax.annotate('Low', xy=(2, 14), xytext=(3, 10),
            arrowprops=dict(facecolor='orange', shrink=0.1), **highlight_style)
ax.annotate('Peak', xy=(4, 25), xytext=(5, 26),
            arrowprops=dict(facecolor='green', shrink=0.1), **highlight_style)
ax.annotate('Low', xy=(1, -5), xytext=(2, -10),
            arrowprops=dict(facecolor='green', shrink=0.1), **highlight_style)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()