import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2020, 2035)

# Define the number of successful landings
moon_landings = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
mars_landings = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
venus_landings = np.array([1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Create the figure and subplots using a 2x1 grid
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 16))

# New set of colors
new_colors = ['#4B0082', '#008B8B', '#FF1493']

# Subplot 1: Stacked Area Chart for Landings
ax1.stackplot(years, moon_landings, mars_landings, venus_landings,
              labels=['Luna', 'Ares', 'Aphrodite'],
              colors=new_colors, alpha=0.8)
ax1.set_title("Galactic Quest Expeditions\nTriumphant Touchdowns (2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Chronology", fontsize=14)
ax1.set_ylabel("Tally of Descents", fontsize=14)
ax1.set_xticks(years[::1])
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left', title="Heavenly Entities", fontsize=12, bbox_to_anchor=(1, 1))
ax1.grid(True, linestyle='--', alpha=0.6)

# Subplot 2: Line Plot for Yearly Growth Rate
moon_growth_rate = np.gradient(moon_landings) / moon_landings * 100
mars_growth_rate = np.gradient(mars_landings) / mars_landings * 100
venus_growth_rate = np.gradient(venus_landings) / venus_landings * 100

ax2.plot(years, moon_growth_rate, label='Luna', color=new_colors[0], marker='o')
ax2.plot(years, mars_growth_rate, label='Ares', color=new_colors[1], marker='o')
ax2.plot(years, venus_growth_rate, label='Aphrodite', color=new_colors[2], marker='o')
ax2.set_title("Annual Leap of Victorious Landings\n(2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Chronology", fontsize=14)
ax2.set_ylabel("Increment Rate (%)", fontsize=14)
ax2.set_xticks(years[::1])
ax2.tick_params(axis='x', rotation=45)
ax2.legend(loc='upper left', title="Heavenly Entities", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()