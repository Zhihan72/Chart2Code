import matplotlib.pyplot as plt
import numpy as np

# Define decades and initiatives
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
initiatives = ['Air', 'Water', 'Recycling', 'Renewable']

# Pollution reduction impact (percentage)
impact = np.array([
    [10, 5, 5, 0],    
    [15, 10, 10, 5],  
    [20, 20, 15, 10], 
    [25, 30, 25, 20], 
    [30, 40, 35, 30]  
])

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Recycling Growth
recycling_growth = np.diff(impact[:, 2])
periods = ['1990s', '2000s', '2010s', '2020s']
ax2.bar(periods, recycling_growth, color='#778899', alpha=0.8)
ax2.set_title('Recycling Growth', fontsize=16, fontweight='bold')
ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Impact Change (%)', fontsize=12)

# Subplot 2: Stacked Area Chart
ax1.stackplot(decades, impact.T, colors=['#FFA07A', '#20B2AA', '#778899', '#DEB887'], alpha=0.8)
ax1.set_title('Initiatives Impact', fontsize=16, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Reduction (%)', fontsize=12)

plt.tight_layout()
plt.show()