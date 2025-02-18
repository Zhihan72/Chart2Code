import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)

coffee_consumption = np.array([1, 2, 1, 3, 2, 3, 4, 2, 5, 6, 5, 4, 3, 6,
                               5, 5, 4, 7, 6, 7, 8, 7, 9, 8, 10, 9, 7, 8, 7, 6])

lines_of_code = np.array([50, 100, 55, 150, 120, 180, 200, 130, 250, 300, 290, 220, 170, 320,
                          280, 270, 240, 350, 330, 360, 400, 380, 430, 410, 450, 420, 410, 430, 300, 250])

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