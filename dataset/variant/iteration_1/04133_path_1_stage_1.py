import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026])

# Randomly altered green spaces data while maintaining the structure
new_york_green_spaces = np.array([30, 33, 37, 40, 44, 47, 50, 56, 61])
tokyo_green_spaces = np.array([25, 28, 30, 31, 36, 38, 42, 48, 51])
berlin_green_spaces = np.array([22, 24, 27, 29, 33, 39, 43, 46, 51])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, new_york_green_spaces, marker='o', linestyle='-', color='green', linewidth=2, label='New York')
ax.plot(years, tokyo_green_spaces, marker='s', linestyle='--', color='blue', linewidth=2, label='Tokyo')
ax.plot(years, berlin_green_spaces, marker='^', linestyle='-.', color='red', linewidth=2, label='Berlin')

ax.set_title('Growth in Urban Green Spaces (2010-2026)\nA Comparative Study Across New York, Tokyo, and Berlin', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Urban Green Spaces (sq km)', fontsize=12)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

milestones = {
    2016: 'Sustainability Initiatives Boost',
    2020: 'Green Policy Implementation',
    2024: 'Urban Greening Projects'
}
for year, city_data in zip([2016, 2020, 2024], [new_york_green_spaces, tokyo_green_spaces, berlin_green_spaces]):
    ax.annotate(milestones[year], 
                xy=(year, city_data[np.where(years == year)[0][0]]), 
                xytext=(10, -30), 
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                fontsize=10,
                color='darkred')

plt.tight_layout()
plt.show()