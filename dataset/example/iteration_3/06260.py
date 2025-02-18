import matplotlib.pyplot as plt
import numpy as np

# Backstory: Studying the Correlation Between Coffee Consumption and Coding Productivity Over a Month
# Data for Coffee Consumption (cups) vs. Lines of Code Written

# Creating artificial but meaningful data 
days = np.arange(1, 31)  # Days of the month

# Coffee consumption in cups per day for a month
coffee_consumption = np.array([1, 2, 1, 3, 2, 3, 4, 2, 5, 6, 5, 4, 3, 6,
                               5, 5, 4, 7, 6, 7, 8, 7, 9, 8, 10, 9, 7, 8, 7, 6])

# Lines of code written each day
lines_of_code = np.array([50, 100, 55, 150, 120, 180, 200, 130, 250, 300, 290, 220, 170, 320,
                          280, 270, 240, 350, 330, 360, 400, 380, 430, 410, 450, 420, 410, 430, 300, 250])

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot for Lines of Code Written
scatter = ax1.scatter(coffee_consumption, lines_of_code, color='coral', edgecolors='black', s=100, label='Lines of Code', zorder=2)

# Add a polynomial trend line (3rd degree)
z = np.polyfit(coffee_consumption, lines_of_code, 3)
p = np.poly1d(z)
trendline_x = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
trendline_y = p(trendline_x)
trend = ax1.plot(trendline_x, trendline_y, color='darkgreen', linestyle='-', linewidth=2, label='Trend Line', zorder=1)

# Titles and labels
plt.title("Impact of Daily Coffee Consumption on Coding Productivity:\nA Detailed Study Over One Month", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Coffee Consumption (cups/day)", fontsize=12)
ax1.set_ylabel("Lines of Code Written", fontsize=12)

# Highlight specific observations
highlight_days = [10, 15, 22]  # Sample days for annotation
for day in highlight_days:
    ax1.annotate(f'Day {day}', 
                (coffee_consumption[day-1], lines_of_code[day-1]), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center', 
                fontsize=10, 
                arrowprops=dict(arrowstyle='->', color='gray'))

# Grid and legends
ax1.grid(visible=True, linestyle='--', alpha=0.6)
scatter_legend = ax1.legend(loc='upper left', fontsize=10)

# Tight layout for better spacing
plt.tight_layout()

# Show plot
plt.show()