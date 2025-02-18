import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2029)
math_engagement = np.array([70, 72, 75, 78, 80, 82])
science_engagement = np.array([65, 67, 70, 73, 75, 78])
literature_engagement = np.array([55, 58, 60, 62, 65, 67])

fig, ax = plt.subplots(figsize=(12, 6))

# Applying a single color consistently across all data groups
consistent_color = '#1f77b4'

ax.plot(years, math_engagement, marker='v', linestyle='--', color=consistent_color)
ax.plot(years, science_engagement, marker='x', linestyle='-', color=consistent_color)
ax.plot(years, literature_engagement, marker='D', linestyle=':', color=consistent_color)

ax.grid(True, linestyle='-', alpha=0.3)

ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()