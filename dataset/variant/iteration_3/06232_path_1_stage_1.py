import matplotlib.pyplot as plt
import numpy as np

# Define decades and various pollution control initiatives
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
initiatives = ['Air Quality Controls', 'Water Treatment Plants', 'Waste Recycling Programs', 'Renewable Energy Adoption']

# Impact of initiatives on pollution reduction over decades (in percentage)
impact = np.array([
    [10, 5, 5, 0],    # 1980s: Initiation phase
    [15, 10, 10, 5],  # 1990s: Slight improvements
    [20, 20, 15, 10], # 2000s: Incremental progress
    [25, 30, 25, 20], # 2010s: Major endeavors
    [30, 40, 35, 30]  # 2020s: High emphasis
])

# Create a figure with 2 subplots and switch their orders
fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Yearly Growth in Impact of Recycling (Bar Chart)
# Calculating increments for waste recycling programs
recycling_growth = np.diff(impact[:, 2])

# Bar chart data
periods = ['1990s', '2000s', '2010s', '2020s']

ax2.bar(periods, recycling_growth, color='#778899', alpha=0.8)
ax2.set_title('Growth in Impact of\nWaste Recycling Programs', fontsize=16, fontweight='bold')
ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Increase in Impact (%)', fontsize=12)
ax2.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Subplot 2: Stacked Area Chart
ax1.stackplot(decades, impact.T, labels=initiatives, colors=['#FFA07A', '#20B2AA', '#778899', '#DEB887'], alpha=0.8)
ax1.set_title('Pollution Control Initiatives Impact\n(1980s - 2020s)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Pollution Reduction (%)', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0)
ax1.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()