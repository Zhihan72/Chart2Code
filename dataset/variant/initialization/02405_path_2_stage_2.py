import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
solar = [5, 8, 15, 22, 30, 40, 52, 60, 68, 74, 80]
wind = [3, 5, 10, 16, 23, 35, 45, 55, 63, 70, 75]
geothermal = [1, 2, 3, 5, 7, 10, 15, 20, 25, 30, 35]

plt.figure(figsize=(12, 8))

# Slight shuffling of line styles and marker colors
plt.plot(years, solar, marker='^', color='forestgreen', linestyle='-', linewidth=2, label='Solar Power')
plt.plot(years, wind, marker='o', color='forestgreen', linestyle='-', linewidth=2, label='Wind Sources')
plt.plot(years, geothermal, marker='s', color='forestgreen', linestyle='-', linewidth=2, label='Geo Energy')

# Altering annotations with the same context
plt.annotate('Solar panel incentives', xy=(2014, solar[4]), xytext=(2014, solar[4] + 12),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='right')
plt.annotate('Innovations in wind turbines', xy=(2016, wind[6]), xytext=(2016, wind[6] + 12),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='right')
plt.annotate('Advancements in geothermal', xy=(2018, geothermal[8]), xytext=(2018, geothermal[8] + 12),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='right')

# Altered title and label texts
plt.title('Renewable Energy Growth: 2010-2020', fontsize=18, fontweight='bold')
plt.xlabel('Calendar Year', fontsize=14)
plt.ylabel('Growth Rate (%)', fontsize=14)
plt.xticks(years)
plt.yticks(range(0, 101, 10))
plt.legend(loc='upper left', title='Energy Forms')

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()