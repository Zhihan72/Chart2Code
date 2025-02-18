import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

creative_hours = np.array([0, 1, 6, 3, 4, 5, 2, 7, 8, 10, 9])
happiness_levels = np.array([30, 40, 60, 50, 35, 55, 68, 75, 82, 90, 88])

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

cubic_params, _ = curve_fit(cubic_fit, creative_hours, happiness_levels)

hours_range = np.linspace(min(creative_hours), max(creative_hours), 300)
fitting_curve = cubic_fit(hours_range, *cubic_params)

plt.figure(figsize=(10, 6))
plt.scatter(
    creative_hours, happiness_levels,
    color='orange', label='Observed Data',
    alpha=0.7, edgecolors='blue', s=120, marker='v'
)
plt.plot(
    hours_range, fitting_curve,
    color='green', linestyle='--', linewidth=3, label='Cubic Fit Curve'
)
plt.title("Impact of Creative Activities on Happiness", fontsize=16, pad=20)
plt.xlabel("Creative Hours per Week", fontsize=12)
plt.ylabel("Happiness Level", fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, linestyle='-.', alpha=0.5)
plt.xlim(min(creative_hours) - 1, max(creative_hours) + 1)
plt.ylim(20, 100)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(20, 101, 10))
plt.tight_layout()
plt.show()