import numpy as np
import matplotlib.pyplot as plt

categories = ['ID', 'Soil Prep', 'Pest Ctrl', 'Eff Water', 'Arrangement', 'Yield']
N = len(categories)

# Original data series
values = [8, 7, 6, 9, 5, 8] 
values += values[:1]

# Additional made-up data series
additional_values = [6, 6.5, 7.5, 8, 5.5, 6.5] 
additional_values += additional_values[:1]

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Closing the loop by repeating the first angle

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='forestgreen', size=10, rotation=45)
plt.ylim(0, 10)

# Uniform colors for different data series
uniform_color_1 = 'forestgreen'
uniform_color_2 = 'navy'

# Plot the first radar chart line and fill the area inside
ax.plot(angles, values, linewidth=2.5, linestyle='-', color=uniform_color_1, marker='o', markersize=8)
ax.fill(angles, values, uniform_color_1, alpha=0.25)

# Plot the additional data series on the radar chart
ax.plot(angles, additional_values, linewidth=2.5, linestyle='-', color=uniform_color_2, marker='o', markersize=8)
ax.fill(angles, additional_values, uniform_color_2, alpha=0.25)

plt.title('Gardening Skills Comparison', size=18, color=uniform_color_1, loc='center', y=1.1)

plt.tight_layout()
plt.show()