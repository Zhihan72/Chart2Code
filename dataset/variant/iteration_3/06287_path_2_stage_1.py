import matplotlib.pyplot as plt
import numpy as np

# Original Data for Community A
exercise_hours_A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores_A = np.array([55, 60, 65, 68, 72, 75, 78, 82, 85, 88])

# New Data for Community B
exercise_hours_B = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
happiness_scores_B = np.array([50, 55, 59, 63, 67, 70, 74, 77, 80, 83])

plt.figure(figsize=(12, 8))

# Scatter plot for Community A
plt.scatter(exercise_hours_A, happiness_scores_A, color='green', s=100, alpha=0.75, edgecolor='black', label='Community A')

# Scatter plot for Community B
plt.scatter(exercise_hours_B, happiness_scores_B, color='blue', s=100, alpha=0.75, edgecolor='black', label='Community B')

# Trend line for Community A
coefficients_A = np.polyfit(exercise_hours_A, happiness_scores_A, 1)
poly_A = np.poly1d(coefficients_A)
x_fit_A = np.linspace(min(exercise_hours_A), max(exercise_hours_A), 100)
y_fit_A = poly_A(x_fit_A)
plt.plot(x_fit_A, y_fit_A, color='orange', linestyle='--', linewidth=2, label='Trend Line A')

# Trend line for Community B
coefficients_B = np.polyfit(exercise_hours_B, happiness_scores_B, 1)
poly_B = np.poly1d(coefficients_B)
x_fit_B = np.linspace(min(exercise_hours_B), max(exercise_hours_B), 100)
y_fit_B = poly_B(x_fit_B)
plt.plot(x_fit_B, y_fit_B, color='red', linestyle='--', linewidth=2, label='Trend Line B')

plt.title("Comparison of Exercise Time and Happiness Level in Smithville", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Hours of Exercise per Week", fontsize=12)
plt.ylabel("Happiness Score (out of 100)", fontsize=12)

plt.legend(loc='lower right', fontsize=10)
plt.xlim(0, 11)
plt.ylim(45, 90)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()