import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_levels = np.array([30, 33, 36, 48, 52, 60, 70, 80, 85, 89, 95])

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

cubic_params, _ = curve_fit(cubic_fit, creative_hours, happiness_levels)
quadratic_params, _ = curve_fit(quadratic_fit, creative_hours, happiness_levels)

hours_range = np.linspace(min(creative_hours), max(creative_hours), 300)
cubic_curve = cubic_fit(hours_range, *cubic_params)
quadratic_curve = quadratic_fit(hours_range, *quadratic_params)

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(creative_hours, happiness_levels, color='teal', alpha=0.8, edgecolors='k', s=100)

ax.plot(hours_range, cubic_curve, color='orange', linestyle='-', linewidth=2)
ax.plot(hours_range, quadratic_curve, color='purple', linestyle='--', linewidth=2)

happiness_std = np.array([3, 4, 5, 5, 6, 5, 4, 3, 4, 3, 3])
ax.errorbar(creative_hours, happiness_levels, yerr=happiness_std, fmt='o', color='gray', alpha=0.5)

ax.set_xlim(min(creative_hours) - 1, max(creative_hours) + 1)
ax.set_ylim(20, 100)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(20, 101, 10))

ax2 = ax.twinx()
social_hours = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])
ax2.plot(creative_hours, social_hours, color='blue', linestyle=':', linewidth=2, marker='s')

fig.tight_layout()

plt.show()