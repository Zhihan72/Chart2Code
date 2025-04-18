import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2025)
machine_learning = np.array([2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212, 233, 255, 278, 301])
natural_language_processing = np.array([1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256, 279])
computer_vision = np.array([1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212, 233, 255, 278])
robotics = np.array([1, 2, 3, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256])
reinforcement_learning = np.array([1, 2, 3, 4, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157, 175, 194, 214, 235])

cumulative_ai = machine_learning + natural_language_processing + computer_vision + robotics + reinforcement_learning

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(
    years,
    machine_learning,
    natural_language_processing,
    computer_vision,
    robotics,
    reinforcement_learning,
    colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
    alpha=0.8
)

ax2 = ax.twinx()
ax2.plot(years, cumulative_ai, 'k--', linewidth=2)

ax.set_title(
    "AI Domain Growth (2000-2025)",
    fontsize=18,
    fontweight='bold',
    pad=20
)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Effort (Unit)', fontsize=14)
ax2.set_ylabel('Total', fontsize=14, color='k')

# Removed grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

fig.tight_layout()
plt.show()