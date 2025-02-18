import matplotlib.pyplot as plt
import numpy as np

eras = ['Ancient World', 'Middle Ages', 'Renaissance', 'Industrial Age', 'Modern Era']
years = np.arange(600, 2100, 100)

experience_points = np.array([
    [100, 300, 450, 600, 800, 1000, 1200, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700],
    [300, 500, 700, 900, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],
    [200, 400, 600, 850, 1050, 1250, 1450, 1650, 1850, 2050, 2250, 2450, 2650, 2850, 3050],
    [250, 450, 650, 850, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100],
    [350, 550, 750, 950, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],
])

cumulative_points = np.cumsum(experience_points, axis=0)

plt.figure(figsize=(14, 9))
plt.stackplot(years, cumulative_points, labels=eras, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

plt.title("Journey Through Time: A Time Traveler's\nExperience Accumulation", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Cumulative Experience Points", fontsize=12)
plt.legend(loc='upper left', title="Historical Eras", fontsize=10)
plt.grid(linestyle='--', alpha=0.7)

significant_points = [(600, 100), (1600, 1800), (2000, 3000)]
for year, value in significant_points:
    plt.annotate(f'({year}, {value})', xy=(year, value), xytext=(year+50, value+200),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='black')

plt.xticks(years, rotation=45, fontsize=10)
plt.tight_layout()
plt.show()