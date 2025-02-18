import matplotlib.pyplot as plt
import numpy as np

# Title and backstory:
# The chart depicts the relationship between the number of community libraries in various districts and the literacy rates in those districts. The chart aims to highlight the importance of community libraries in enhancing literacy and education.

# Data:
# Number of community libraries in various districts
libraries = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Corresponding literacy rates in percentage
literacy_rates = np.array([60, 65, 70, 75, 78, 80, 82, 84, 86, 88])

# Setting up the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Creating the scatter plot
scatter = ax.scatter(libraries, literacy_rates, color='royalblue', edgecolor='black', s=150, alpha=0.6, label='Districts')

# Adding quadratic trend line for a smoother fit
def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the curve
params = np.polyfit(libraries, literacy_rates, 2, full=False, cov=False)
x_smooth = np.linspace(min(libraries), max(libraries), 300)
y_smooth = quadratic(x_smooth, *params)

# Plotting the trend line
ax.plot(x_smooth, y_smooth, linestyle='--', color='orange', linewidth=2, label='Quadratic Fit')

# Titles and labels
plt.title('Impact of Community Libraries on Literacy Rates\nAn Insightful Look at District-wise Data', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Number of Community Libraries', fontsize=14)
plt.ylabel('Literacy Rates (%)', fontsize=14)

# Adding grid for readability
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Adding annotations for clarity
highlight_libraries = [10, 30, 50]
highlight_labels = ['Small Town A', 'Metro B', 'Urban Center C']
for lib, label in zip(highlight_libraries, highlight_labels):
    index = np.where(libraries == lib)[0][0]
    ax.annotate(label, (libraries[index], literacy_rates[index]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, arrowprops=dict(arrowstyle='->', color='gray'))

# Set legend
plt.legend(loc='lower right', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()