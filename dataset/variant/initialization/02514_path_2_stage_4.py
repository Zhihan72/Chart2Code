import matplotlib.pyplot as plt
import numpy as np

eras = ['Ancient', 'Middle', 'Renaissance', 'Modern']
years = np.arange(600, 2100, 100)

experience_points = np.array([
    [100, 300, 450, 600, 800, 1000, 1200, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700],
    [300, 500, 700, 900, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],
    [200, 400, 600, 850, 1050, 1250, 1450, 1650, 1850, 2050, 2250, 2450, 2650, 2850, 3050],
    [350, 550, 750, 950, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],
])

cumulative_points = np.cumsum(experience_points, axis=0)

plt.figure(figsize=(14, 9))
plt.stackplot(years, cumulative_points, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd'])

plt.title("Time Traveler: Experience", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Exp. Points", fontsize=12)

significant_points = [(600, 100), (1600, 1800), (2000, 3000)]
for year, value in significant_points:
    plt.annotate(f'({year}, {value})', xy=(year, value), xytext=(year+50, value+200),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='black')

plt.xticks(years, rotation=45, fontsize=10)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()