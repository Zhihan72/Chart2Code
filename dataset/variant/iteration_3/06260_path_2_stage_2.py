import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)

# Original coffee_consumption array had the pattern [1, 2, 1, 3,...];
# Altering some values to match a similar random pattern [3, 1, 4, 2,...]
coffee_consumption = np.array([3, 1, 4, 2, 5, 3, 2, 6, 4, 5, 7, 6, 5, 6,
                               7, 5, 4, 8, 7, 9, 6, 10, 8, 7, 10, 9, 8, 9, 7, 6])

# Original lines_of_code array had the pattern [50, 100, 55, 150,...];
# Altering some values to reflect a similar random pattern [180, 50, 200, 100,...]
lines_of_code = np.array([180, 50, 200, 100, 220, 180, 160, 250, 200, 230, 290, 310, 300, 320,
                          270, 260, 250, 390, 350, 380, 340, 410, 430, 405, 420, 415, 405, 430, 320, 280])

fig, ax1 = plt.subplots(figsize=(14, 8))

scatter = ax1.scatter(coffee_consumption, lines_of_code, color='coral', edgecolors='black', s=100, zorder=2)

z = np.polyfit(coffee_consumption, lines_of_code, 3)
p = np.poly1d(z)
trendline_x = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
trendline_y = p(trendline_x)
trend = ax1.plot(trendline_x, trendline_y, color='darkgreen', linestyle='-', linewidth=2, zorder=1)

ax1.grid(visible=True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()