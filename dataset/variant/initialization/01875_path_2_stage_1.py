import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_levels = np.array([30, 35, 40, 50, 55, 60, 68, 75, 82, 88, 90])

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

cubic_params, _ = curve_fit(cubic_fit, creative_hours, happiness_levels)

hours_range = np.linspace(min(creative_hours), max(creative_hours), 300)
fitting_curve = cubic_fit(hours_range, *cubic_params)

plt.figure(figsize=(10, 6))
plt.scatter(creative_hours, happiness_levels, color='teal', label='Data', alpha=0.8, edgecolors='k', s=100)
plt.plot(hours_range, fitting_curve, color='orange', linestyle='-', linewidth=2, label='Fit')

plt.title("Creative Activities vs. Happiness", fontsize=16, pad=20)
plt.xlabel("Hours/Week", fontsize=12)
plt.ylabel("Happiness", fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(min(creative_hours) - 1, max(creative_hours) + 1)
plt.ylim(20, 100)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(20, 101, 10))
plt.tight_layout()
plt.show()