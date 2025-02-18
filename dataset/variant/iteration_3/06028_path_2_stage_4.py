import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
city1_population = [1.2, 1.25, 1.32, 1.40, 1.45, 1.50, 1.55, 1.60, 1.70, 1.75, 1.80]
city2_population = [0.8, 0.85, 0.88, 0.92, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25]

def calculate_annual_growth_rate(data):
    return [100 * (data[k+1] - data[k]) / data[k] for k in range(len(data)-1)]

city1_growth = calculate_annual_growth_rate(city1_population)
city2_growth = calculate_annual_growth_rate(city2_population)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(years, city1_population, marker='o', linestyle='-', color='blue', linewidth=2)
ax1.plot(years, city2_population, marker='s', linestyle='--', color='green', linewidth=2)
ax1.set_title("Population Dynamics:\nAn Overview from 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Timeline', fontsize=12, fontweight='bold')
ax1.set_ylabel('Residents (Millions)', fontsize=12, fontweight='bold')
ax1.axvspan(2014, 2016, color='yellow', alpha=0.3)

ind = np.arange(len(city1_growth))
width = 0.3

ax2.barh(ind - width/2, city1_growth, height=width, color='blue', alpha=0.7)
ax2.barh(ind + width/2, city2_growth, height=width, color='green', alpha=0.7)
ax2.set_title('Yearly Growth Trends', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Growth Percentage', fontsize=12, fontweight='bold')
ax2.set_ylabel('Timeline', fontsize=12, fontweight='bold')
ax2.set_yticks(ind)
ax2.set_yticklabels(years[1:])

plt.tight_layout()
plt.show()