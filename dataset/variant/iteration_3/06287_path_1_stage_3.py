import matplotlib.pyplot as plt
import numpy as np

exercise_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([55, 60, 65, 68, 72, 75, 78, 82, 85, 88])

exercise_hours_group2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores_group2 = np.array([50, 52, 58, 63, 70, 73, 77, 80, 83, 86])

plt.figure(figsize=(12, 8))

plt.scatter(exercise_hours, happiness_scores, color='orange', s=100, alpha=0.75, edgecolor='black')
plt.scatter(exercise_hours_group2, happiness_scores_group2, color='blue', s=100, alpha=0.75, edgecolor='black')

coefficients_group1 = np.polyfit(exercise_hours, happiness_scores, 1)
poly_group1 = np.poly1d(coefficients_group1)
coefficients_group2 = np.polyfit(exercise_hours_group2, happiness_scores_group2, 1)
poly_group2 = np.poly1d(coefficients_group2)

x_fit = np.linspace(1, 10, 100)
y_fit_group1 = poly_group1(x_fit)
y_fit_group2 = poly_group2(x_fit)

plt.plot(x_fit, y_fit_group1, color='green', linestyle='--', linewidth=2)
plt.plot(x_fit, y_fit_group2, color='red', linestyle='--', linewidth=2)

plt.xlim(0, 11)
plt.ylim(50, 90)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()