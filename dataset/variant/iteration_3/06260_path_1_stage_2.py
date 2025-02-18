import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
coffee_consumption = np.array([1, 2, 1, 3, 2, 3, 4, 2, 5, 6, 5, 4, 3, 6,
                               5, 5, 4, 7, 6, 7, 8, 7, 9, 8, 10, 9, 7, 8, 7, 6])
lines_of_code = np.array([50, 100, 55, 150, 120, 180, 200, 130, 250, 300, 290, 220, 170, 320,
                          280, 270, 240, 350, 330, 360, 400, 380, 430, 410, 450, 420, 410, 430, 300, 250])

fig, ax1 = plt.subplots(figsize=(14, 8))

scatter = ax1.scatter(coffee_consumption, lines_of_code, color='skyblue', edgecolors='navy', s=120, label='Coding Productivity', marker='^', zorder=2)

z = np.polyfit(coffee_consumption, lines_of_code, 3)
p = np.poly1d(z)
trendline_x = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
trendline_y = p(trendline_x)
trend = ax1.plot(trendline_x, trendline_y, color='purple', linestyle='--', linewidth=2, label='Productivity Trend', zorder=1)

plt.title("Coffee & Coding Efficiency Analysis", fontsize=18, fontweight='bold', pad=25)
ax1.set_xlabel("Coffee Consumption (cups)", fontsize=12, fontweight='bold')
ax1.set_ylabel("Lines of Code", fontsize=12, fontweight='bold')

highlight_days = [10, 15, 22]
for day in highlight_days:
    ax1.annotate(f'Day {day}', 
                (coffee_consumption[day-1], lines_of_code[day-1]), 
                textcoords="offset points", 
                xytext=(-10,10), 
                ha='right', 
                fontsize=11, 
                arrowprops=dict(arrowstyle='->', color='black'))

ax1.grid(visible=True, linestyle=':', alpha=0.8)
scatter_legend = ax1.legend(loc='lower right', fontsize=11, frameon=False)

plt.tight_layout()

plt.show()