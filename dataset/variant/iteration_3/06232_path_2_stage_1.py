import matplotlib.pyplot as plt
import numpy as np

# Define decades and initiatives
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
initiatives = ['Air Quality', 'Water Treatment', 'Recycling', 'Renewable Energy']

# Impact of initiatives (in percentage)
impact = np.array([
    [10, 5, 5, 0],
    [15, 10, 10, 5],
    [20, 20, 15, 10],
    [25, 30, 25, 20],
    [30, 40, 35, 30]
])

# Create a figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Stacked Area Chart
ax1.stackplot(decades, impact.T, labels=initiatives, colors=['#FFA07A', '#20B2AA', '#778899', '#DEB887'], alpha=0.8)
ax1.set_title('Impact of Initiatives (1980s-2020s)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Reduction (%)', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0)
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Subplot 2: Growth in Recycling Impact (Bar Chart)
recycling_growth = np.diff(impact[:, 2])
periods = ['1990s', '2000s', '2010s', '2020s']

ax2.bar(periods, recycling_growth, color='#778899', alpha=0.8)
ax2.set_title('Recycling Impact Growth', fontsize=16, fontweight='bold')
ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Increase (%)', fontsize=12)
ax2.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()