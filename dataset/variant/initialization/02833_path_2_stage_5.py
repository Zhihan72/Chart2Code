import matplotlib.pyplot as plt
import numpy as np

countries = ['JP', 'EU', 'US', 'AU', 'CN', 'Other', 'CA']
contributions = [18, 20, 25, 10, 15, 5, 7]
missions = [85, 100, 120, 55, 70, 25, 30]

# New color set
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("2023 Ocean Missions\nContributions & Execute Count", fontsize=18, fontweight='bold', color='#333')

# Horizontal bar chart for missions
ax1.barh(countries, missions, color=colors)
ax1.set_xlabel('Missions', fontsize=12, fontweight='bold')
ax1.set_title("Missions by Country", fontsize=14, fontweight='bold', color='#555')
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.set_xlim(0, max(missions) + 20)

# Changed chart type for contributions to horizontal bar chart
ax2.barh(countries, contributions, color=colors)
ax2.set_xlabel('Contributions', fontsize=12, fontweight='bold')
ax2.set_title("Contributions by Country", fontsize=14, fontweight='bold', color='#555')
ax2.grid(axis='x', linestyle='--', alpha=0.7)
ax2.set_xlim(0, max(contributions) + 5)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()