import matplotlib.pyplot as plt
import numpy as np

# Showing random adjustments to text elements like titles, axis, and labels

days = np.arange(1, 31)
coffee_consumption = np.array([1, 2, 1, 3, 2, 3, 4, 2, 5, 6, 5, 4, 3, 6,
                               5, 5, 4, 7, 6, 7, 8, 7, 9, 8, 10, 9, 7, 8, 7, 6])
lines_of_code = np.array([50, 100, 55, 150, 120, 180, 200, 130, 250, 300, 290, 220, 170, 320,
                          280, 270, 240, 350, 330, 360, 400, 380, 430, 410, 450, 420, 410, 430, 300, 250])

fig, ax1 = plt.subplots(figsize=(14, 8))

scatter = ax1.scatter(coffee_consumption, lines_of_code, color='coral', edgecolors='black', s=100, label='Code Output Units', zorder=2)

z = np.polyfit(coffee_consumption, lines_of_code, 3)
p = np.poly1d(z)
trendline_x = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
trendline_y = p(trendline_x)
trend = ax1.plot(trendline_x, trendline_y, color='darkgreen', linestyle='-', linewidth=2, label='Smooth Flow', zorder=1)

plt.title("Caffeine Infusion Correlation Analysis\nOne Month Exploration", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Caffeine Units (cups)", fontsize=12)
ax1.set_ylabel("Coding Volume (lines)", fontsize=12)

highlight_days = [10, 15, 22]
for day in highlight_days:
    ax1.annotate(f'Day {day}', 
                (coffee_consumption[day-1], lines_of_code[day-1]), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center', 
                fontsize=10, 
                arrowprops=dict(arrowstyle='->', color='gray'))

ax1.grid(visible=True, linestyle='--', alpha=0.6)
scatter_legend = ax1.legend(loc='upper left', fontsize=10)

plt.tight_layout()

plt.show()