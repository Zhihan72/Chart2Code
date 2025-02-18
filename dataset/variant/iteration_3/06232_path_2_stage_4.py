import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
initiatives = ['Air Quality', 'Water Treatment', 'Recycling', 'Renewable Energy', 'Waste Management']

# Adding made-up data for a new initiative: 'Waste Management'
impact = np.array([
    [10, 5, 5, 0, 3],
    [15, 10, 10, 5, 6],
    [20, 20, 15, 10, 9],
    [25, 30, 25, 20, 15],
    [30, 40, 35, 30, 20]
])

# Adding color for the new initiative
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 16))

ax1.stackplot(decades, impact.T, colors=['#FFA07A', '#20B2AA', '#778899', '#DEB887', '#8FBC8F'], alpha=0.8)
ax1.set_title('Impact of Initiatives Including Waste Management (1980s-2020s)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Reduction (%)', fontsize=12)

recycling_growth = np.diff(impact[:, 2])
periods = ['1990s', '2000s', '2010s', '2020s']

ax2.bar(periods, recycling_growth, color='#778899', alpha=0.8)
ax2.set_title('Recycling Impact Growth', fontsize=16, fontweight='bold')
ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Increase (%)', fontsize=12)

plt.tight_layout()
plt.show()