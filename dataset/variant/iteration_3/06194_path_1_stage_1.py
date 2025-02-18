import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 25)
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Cape Town']

new_york = [0, 1, 4, 10, 15, 20, 24, 23, 19, 14, 8, 3,
            1, 2, 5, 11, 16, 21, 25, 24, 20, 15, 9, 4]
london = [5, 6, 8, 11, 14, 17, 20, 19, 17, 13, 9, 6,
          6, 7, 9, 12, 15, 18, 21, 20, 18, 14, 10, 7]
tokyo = [5, 6, 10, 15, 20, 24, 28, 29, 25, 19, 14, 8,
         6, 7, 11, 16, 21, 25, 29, 30, 26, 20, 15, 9]
sydney = [23, 23, 21, 18, 15, 12, 10, 12, 15, 18, 20, 22,
          24, 24, 22, 19, 16, 13, 11, 13, 16, 19, 21, 23]
cape_town = [24, 24, 21, 18, 15, 12, 10, 11, 14, 17, 20, 23,
             25, 25, 22, 19, 16, 13, 11, 12, 15, 18, 21, 24]

data = [new_york, london, tokyo, sydney, cape_town]

# Plot configuration
fig, ax = plt.subplots(figsize=(14, 8))

# Randomly chosen markers and styles
markers = ['s', 'D', '^', 'v', '*']
line_styles = ['-', '--', '-.', ':', '-']

# Plotting data with style changes
for temperatures, city, marker, line_style in zip(data, cities, markers, line_styles):
    ax.plot(months, temperatures, marker=marker, linestyle=line_style, label=city)

# Customizing the appearance
ax.set_title('Monthly Average Temperatures Over Two Years\n(5 Major Cities)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Avg Temp (°C)', fontsize=12)

# Setting x-ticks
ax.set_xticks(months)
ax.set_xticklabels([f'Month {i}' for i in months], rotation=45, ha='right')

# Alter grid and legend
ax.grid(False)  # Disable grid
ax.legend(loc='lower left', fontsize=10)  # Changed legend position

# Adjusting border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()