import matplotlib.pyplot as plt
import numpy as np

years = ['2022', '2023', '2024', '2025', '2026']
hull_progress = np.array([60, 70, 80, 90, 100]) - 60
engine_progress = np.array([50, 65, 75, 85, 95]) - 60
control_systems_progress = np.array([40, 55, 70, 85, 95]) - 60
living_quarters_progress = np.array([30, 50, 65, 80, 90]) - 60

fig, ax = plt.subplots(figsize=(10, 7))

# Changed colors for stylistic variation
colors = ['#FF7F50', '#8A2BE2', '#7FFF00', '#DC143C']

# Randomly altered bar elements with different line styles and fill patterns
ax.barh(years, hull_progress, label='Hulls', color=colors[0], left=0, edgecolor='green', hatch='/')
ax.barh(years, engine_progress, label='Engines', color=colors[1], left=hull_progress, edgecolor='blue', hatch='\\')
ax.barh(years, control_systems_progress, label='Control Systems', color=colors[2], left=hull_progress + engine_progress, edgecolor='orange', hatch='|')
ax.barh(years, living_quarters_progress, label='Living Quarters', color=colors[3], left=hull_progress + engine_progress + control_systems_progress, edgecolor='purple', hatch='-')

# Altered title and label styles
ax.set_title('Construction Progress Overview (2022-2026)', fontsize=14, fontweight='light', pad=15)
ax.set_xlabel('Progress (%) from Avg.', fontsize=11)
ax.set_ylabel('Year', fontsize=11)

# Modified legend position and style for variety
ax.legend(title='Components', loc='upper left', fontsize=9, fancybox=True)

# Adjusted grid styles
ax.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.5)

ax.set_xlim(-60, 40)
plt.tight_layout()
plt.show()