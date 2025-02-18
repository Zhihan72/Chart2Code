import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)

coffee_consumption = np.array([3, 1, 4, 2, 5, 3, 2, 6, 4, 5, 7, 6, 5, 6,
                               7, 5, 4, 8, 7, 9, 6, 10, 8, 7, 10, 9, 8, 9, 7, 6])

lines_of_code = np.array([180, 50, 200, 100, 220, 180, 160, 250, 200, 230, 290, 310, 300, 320,
                          270, 260, 250, 390, 350, 380, 340, 410, 430, 405, 420, 415, 405, 430, 320, 280])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Changed marker styling and line styling
scatter = ax1.scatter(coffee_consumption, lines_of_code, color='mediumseagreen', marker='x', s=80, zorder=2)

z = np.polyfit(coffee_consumption, lines_of_code, 3)
p = np.poly1d(z)
trendline_x = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
trendline_y = p(trendline_x)
trend = ax1.plot(trendline_x, trendline_y, color='purple', linestyle=':', linewidth=1.5, zorder=1)

# Altered grid style and visibility
ax1.grid(visible=True, linestyle='-', alpha=0.9)

# Added a legend with new styling
ax1.legend(['Trend Line', 'Data Points'], loc='upper left', fontsize=10, frameon=True, facecolor='lightgray', edgecolor='gray')

plt.tight_layout()

plt.show()