import matplotlib.pyplot as plt
import numpy as np

exercise_hours_A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores_A = np.array([55, 60, 65, 68, 72, 75, 78, 82, 85, 88])

exercise_hours_B = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
happiness_scores_B = np.array([50, 55, 59, 63, 67, 70, 74, 77, 80, 83])

plt.figure(figsize=(12, 8))

# Style elements altered: colors, markers, and edge colors.
plt.scatter(exercise_hours_A, happiness_scores_A, color='purple', s=80, alpha=0.85, edgecolor='orange', marker='x', label='Group A')
plt.scatter(exercise_hours_B, happiness_scores_B, color='cyan', s=80, alpha=0.85, edgecolor='red', marker='*', label='Group B')

coefficients_A = np.polyfit(exercise_hours_A, happiness_scores_A, 1)
poly_A = np.poly1d(coefficients_A)
x_fit_A = np.linspace(min(exercise_hours_A), max(exercise_hours_A), 100)
y_fit_A = poly_A(x_fit_A)
# Changed line style and color
plt.plot(x_fit_A, y_fit_A, color='green', linestyle='-', linewidth=3, label='Trend A')

coefficients_B = np.polyfit(exercise_hours_B, happiness_scores_B, 1)
poly_B = np.poly1d(coefficients_B)
x_fit_B = np.linspace(min(exercise_hours_B), max(exercise_hours_B), 100)
y_fit_B = poly_B(x_fit_B)
# Changed line style and color
plt.plot(x_fit_B, y_fit_B, color='blue', linestyle='-.', linewidth=3, label='Trend B')

# Altered grid style and transparency
plt.grid(True, linestyle=':', linewidth=1.5, alpha=0.8)
plt.xlim(0, 11)
plt.ylim(45, 90)

# Added legends with altered position
plt.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)

plt.tight_layout()
plt.show()