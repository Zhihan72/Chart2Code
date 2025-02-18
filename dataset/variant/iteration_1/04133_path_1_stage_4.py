import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026])

new_york_green_spaces = np.array([30, 33, 37, 40, 44, 47, 50, 56, 61])
tokyo_green_spaces = np.array([25, 28, 30, 31, 36, 38, 42, 48, 51])
berlin_green_spaces = np.array([22, 24, 27, 29, 33, 39, 43, 46, 51])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, new_york_green_spaces, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(years, tokyo_green_spaces, marker='s', linestyle='--', color='orange', linewidth=2)
ax.plot(years, berlin_green_spaces, marker='^', linestyle='-.', color='cyan', linewidth=2)

ax.set_title('Comparative Growth of City Green Spaces from 2010 to 2026', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year Range', fontsize=12)
ax.set_ylabel('Area of Green Spaces (sq km)', fontsize=12)

milestones = {
    2016: 'Eco Boost Initiated',
    2020: 'Implementation of Green Policies',
    2024: 'Major Greening Projects Launch'
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