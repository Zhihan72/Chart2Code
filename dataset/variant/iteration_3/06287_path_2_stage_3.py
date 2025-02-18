import matplotlib.pyplot as plt
import numpy as np

exercise_hours_A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores_A = np.array([55, 60, 65, 68, 72, 75, 78, 82, 85, 88])

exercise_hours_B = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
happiness_scores_B = np.array([50, 55, 59, 63, 67, 70, 74, 77, 80, 83])

plt.figure(figsize=(12, 8))

# Colors shuffled: Swapped colors of scatter plots
plt.scatter(exercise_hours_A, happiness_scores_A, color='blue', s=100, alpha=0.75, edgecolor='black')
plt.scatter(exercise_hours_B, happiness_scores_B, color='green', s=100, alpha=0.75, edgecolor='black')

coefficients_A = np.polyfit(exercise_hours_A, happiness_scores_A, 1)
poly_A = np.poly1d(coefficients_A)
x_fit_A = np.linspace(min(exercise_hours_A), max(exercise_hours_A), 100)
y_fit_A = poly_A(x_fit_A)
# Swapped colors for regression lines
plt.plot(x_fit_A, y_fit_A, color='red', linestyle='--', linewidth=2)

coefficients_B = np.polyfit(exercise_hours_B, happiness_scores_B, 1)
poly_B = np.poly1d(coefficients_B)
x_fit_B = np.linspace(min(exercise_hours_B), max(exercise_hours_B), 100)
y_fit_B = poly_B(x_fit_B)
# Swapped colors for regression lines
plt.plot(x_fit_B, y_fit_B, color='orange', linestyle='--', linewidth=2)

plt.xlim(0, 11)
plt.ylim(45, 90)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()