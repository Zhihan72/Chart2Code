import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Randomized population data for three cities while maintaining structure
city1_population = [1.2, 1.22, 1.28, 1.37, 1.44, 1.48, 1.54, 1.58, 1.66, 1.74, 1.82]
city2_population = [0.81, 0.86, 0.9, 0.93, 1.01, 1.03, 1.06, 1.11, 1.13, 1.22, 1.24]
city3_population = [0.52, 0.56, 0.6, 0.64, 0.7, 0.77, 0.8, 0.87, 0.88, 0.94, 0.99]

def calculate_annual_growth_rate(data):
    return [100 * (data[k+1] - data[k]) / data[k] for k in range(len(data)-1)]

city1_growth = calculate_annual_growth_rate(city1_population)
city2_growth = calculate_annual_growth_rate(city2_population)
city3_growth = calculate_annual_growth_rate(city3_population)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(years, city1_population, marker='o', linestyle='-', color='blue', linewidth=2, label='City Alpha')
ax1.plot(years, city2_population, marker='s', linestyle='--', color='green', linewidth=2, label='City Beta')
ax1.plot(years, city3_population, marker='^', linestyle='-.', color='red', linewidth=2, label='City Gamma')
ax1.set_title("Urban Growth Analysis:\nTracking Population Changes (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Population (Millions)', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.axvspan(2014, 2016, color='yellow', alpha=0.3, label='Urban Planning Initiative')
ax1.annotate('Planning Initiative', xy=(2015, 1.58), xytext=(2013, 1.78),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
             fontsize=10, color='black')

ind = np.arange(len(city1_growth))
width = 0.25

ax2.bar(ind - width, city1_growth, width=width, color='blue', alpha=0.7, label='City Alpha')
ax2.bar(ind, city2_growth, width=width, color='green', alpha=0.7, label='City Beta')
ax2.bar(ind + width, city3_growth, width=width, color='red', alpha=0.7, label='City Gamma')
ax2.set_title('Annual Population Growth Rate', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')
ax2.set_xticks(ind)
ax2.set_xticklabels(years[1:])
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()