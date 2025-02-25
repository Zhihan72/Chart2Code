import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
self_driving_cars = np.array([0.5, 1, 2, 3, 5, 9, 15, 25, 38, 54, 75])
road_accidents = np.array([35, 36, 37, 35, 34, 32, 30, 26, 23, 20, 17])

base_accidents = 37
accidents_reduction_percentage = ((base_accidents - road_accidents) / base_accidents) * 100

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, self_driving_cars, marker='o', color='green', linewidth=2)
for (x, y) in zip(years, self_driving_cars):
    ax1.text(x, y + 2, f'{y}', ha='center', va='bottom', fontsize=10, color='green')

milestones = {2012: "Large Trials", 2016: "Regulations", 
              2018: "Highway", 2020: "Urban"}
for year, text in milestones.items():
    ax1.annotate(text, 
                 xy=(year, self_driving_cars[years.tolist().index(year)]),
                 xytext=(year, self_driving_cars[years.tolist().index(year)] + 20),
                 arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                 fontsize=10, color='black')

ax1.set_title('Self-Driving Cars & Road Safety (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Cars (thousands)', fontsize=12, color='green')
ax1.set_xticks(years)

ax2 = ax1.twinx()

ax2.plot(years, accidents_reduction_percentage, 'purple', linewidth=2)
for (x, y) in zip(years, accidents_reduction_percentage):
    ax2.text(x, y - 2, f'{y:.1f}%', ha='center', va='top', fontsize=10, color='purple')

ax2.set_ylabel('Accidents Reduction (%)', fontsize=12, color='purple')
ax2.tick_params(axis='y', colors='purple')

plt.tight_layout()
plt.show()