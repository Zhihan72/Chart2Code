import matplotlib.pyplot as plt
import numpy as np

exercise_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([55, 60, 65, 68, 72, 75, 78, 82, 85, 88])

plt.figure(figsize=(12, 8))

# Changed color for scatter plot from 'green' to 'orange'
plt.scatter(exercise_hours, happiness_scores, color='orange', s=100, alpha=0.75, edgecolor='black', label='Individuals')

coefficients = np.polyfit(exercise_hours, happiness_scores, 1)
poly = np.poly1d(coefficients)

x_fit = np.linspace(min(exercise_hours), max(exercise_hours), 100)
y_fit = poly(x_fit)

# Changed color for trend line from 'orange' to 'green'
plt.plot(x_fit, y_fit, color='green', linestyle='--', linewidth=2, label='Trend Line (Linear Fit)')

plt.title("Correlation between Exercise Time and Happiness Level in Smithville", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Hours of Exercise per Week", fontsize=12)
plt.ylabel("Happiness Score (out of 100)", fontsize=12)

plt.annotate('Optimal Happiness Level', xy=(8, 82), xytext=(4, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, backgroundcolor='w')

plt.legend(loc='lower right', fontsize=10)

plt.xlim(0, 11)
plt.ylim(50, 90)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()