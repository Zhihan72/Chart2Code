import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_levels = np.array([30, 35, 40, 50, 55, 60, 68, 75, 82, 88, 90])
relaxation_levels = np.array([20, 22, 28, 35, 45, 55, 60, 65, 70, 75, 78])

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

cubic_params_happiness, _ = curve_fit(cubic_fit, creative_hours, happiness_levels)
cubic_params_relaxation, _ = curve_fit(cubic_fit, creative_hours, relaxation_levels)

hours_range = np.linspace(min(creative_hours), max(creative_hours), 300)
happiness_fitting_curve = cubic_fit(hours_range, *cubic_params_happiness)
relaxation_fitting_curve = cubic_fit(hours_range, *cubic_params_relaxation)

plt.figure(figsize=(10, 6))
plt.scatter(creative_hours, happiness_levels, color='green', marker='^', label='Happiness Data', alpha=0.8, edgecolors='k', s=120)
plt.scatter(creative_hours, relaxation_levels, color='blue', marker='o', label='Relaxation Data', alpha=0.8, edgecolors='k', s=100)
plt.plot(hours_range, happiness_fitting_curve, color='purple', linestyle='-.', linewidth=1.5, label='Happiness Fit')
plt.plot(hours_range, relaxation_fitting_curve, color='orange', linestyle='--', linewidth=1.5, label='Relaxation Fit')

plt.title("Creative Activities vs. Happiness & Relaxation", fontsize=16, pad=20)
plt.xlabel("Hours/Week", fontsize=12)
plt.ylabel("Levels", fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, linestyle='-', alpha=0.3)
plt.xlim(min(creative_hours) - 1, max(creative_hours) + 1)
plt.ylim(15, 100)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(20, 101, 10))
plt.tight_layout()
plt.show()