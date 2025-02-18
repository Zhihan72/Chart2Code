import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart examines the relationship between people's investment in exercise and their level of happiness. The data simulates measurements for a group of individuals in a small community, aiming to visualize how investment in exercise time each week (in hours) correlates with a happiness score (out of 100).

# Data: Hours of exercise per week and corresponding happiness scores
exercise_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([55, 60, 65, 68, 72, 75, 78, 82, 85, 88])

# Scatter plot setup
plt.figure(figsize=(12, 8))

# Scatter plot for exercise vs happiness
plt.scatter(exercise_hours, happiness_scores, color='green', s=100, alpha=0.75, edgecolor='black', label='Individuals')

# Add trend line by fitting a linear model
coefficients = np.polyfit(exercise_hours, happiness_scores, 1)
poly = np.poly1d(coefficients)

# Generate values for the trend line
x_fit = np.linspace(min(exercise_hours), max(exercise_hours), 100)
y_fit = poly(x_fit)

# Plot the trend line
plt.plot(x_fit, y_fit, color='orange', linestyle='--', linewidth=2, label='Trend Line (Linear Fit)')

# Titles and labels
plt.title("Correlation between Exercise Time and Happiness Level in Smithville", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Hours of Exercise per Week", fontsize=12)
plt.ylabel("Happiness Score (out of 100)", fontsize=12)

# Annotation for key observation
plt.annotate('Optimal Happiness Level', xy=(8, 82), xytext=(4, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, backgroundcolor='w')

# Legend placement
plt.legend(loc='lower right', fontsize=10)

# Axis limits
plt.xlim(0, 11)
plt.ylim(50, 90)

# Grid styling and layout adjustment
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show plot
plt.show()