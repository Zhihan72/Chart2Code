import matplotlib.pyplot as plt
import numpy as np

# Number of community libraries in various districts
libraries_original = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
literacy_rates_original = np.array([60, 65, 70, 75, 78, 80, 82, 84, 86, 88])

# Additional dataset
libraries_additional = np.array([6, 12, 18, 24, 30, 36, 42, 48, 54, 60])
literacy_rates_additional = np.array([62, 67, 72, 76, 79, 81, 83, 85, 87, 89])

# Setting up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot for the original dataset
scatter_original = ax.scatter(libraries_original, literacy_rates_original, color='royalblue', edgecolor='black', s=150, alpha=0.6, label='Districts Original')

# Scatter plot for the additional dataset
scatter_additional = ax.scatter(libraries_additional, literacy_rates_additional, color='seagreen', edgecolor='black', s=150, alpha=0.6, label='Districts Additional')

# Adding quadratic trend line for original dataset
def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

params_original = np.polyfit(libraries_original, literacy_rates_original, 2, full=False, cov=False)
x_smooth_original = np.linspace(min(libraries_original), max(libraries_original), 300)
y_smooth_original = quadratic(x_smooth_original, *params_original)

ax.plot(x_smooth_original, y_smooth_original, linestyle='--', color='orange', linewidth=2, label='Quadratic Fit Original')

# Adding quadratic trend line for additional dataset
params_additional = np.polyfit(libraries_additional, literacy_rates_additional, 2, full=False, cov=False)
x_smooth_additional = np.linspace(min(libraries_additional), max(libraries_additional), 300)
y_smooth_additional = quadratic(x_smooth_additional, *params_additional)

ax.plot(x_smooth_additional, y_smooth_additional, linestyle='--', color='red', linewidth=2, label='Quadratic Fit Additional')

# Titles and labels
plt.title('Impact of Community Libraries on Literacy Rates\nIncluding Additional District Data', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Number of Community Libraries', fontsize=14)
plt.ylabel('Literacy Rates (%)', fontsize=14)

# Adding grid
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Adding annotations for clarity
highlight_libraries = [10, 30, 50]
highlight_labels = ['Small Town A', 'Metro B', 'Urban Center C']
for lib, label in zip(highlight_libraries, highlight_labels):
    index = np.where(libraries_original == lib)[0][0]
    ax.annotate(label, (libraries_original[index], literacy_rates_original[index]), 
                textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, 
                arrowprops=dict(arrowstyle='->', color='gray'))

# Set legend
plt.legend(loc='lower right', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()