import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2050, 2051, 2052, 2053, 2054])
martian_potatoes = np.array([1.2, 1.5, 1.7, 2.0, 2.3])
space_carrots = np.array([1.0, 1.2, 1.5, 1.7, 2.1])

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each crop type with varied markers and line styles
plt.plot(years, martian_potatoes, marker='s', linestyle='-.', linewidth=2, color='tab:orange', label='Martian Potatoes')
plt.plot(years, space_carrots, marker='d', linestyle=':', linewidth=2, color='tab:blue', label='Space Carrots')

# Title and labels
plt.title('Extraterrestrial Agriculture: \nCrop Yields on Mars (2050-2054)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Yield (tons per Martian acre)', fontsize=12)

# Ticks and grid
plt.xticks(years)
plt.grid(True, linestyle='-', linewidth=0.75, alpha=0.9)

# Legend with changed position and font size
plt.legend(loc='lower right', fontsize=12)

# Annotations without change in this instruction
plt.annotate('Experimentation begins', xy=(2050, 1.2), xytext=(2050, 1.5),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

plt.annotate('Optimal conditions achieved', xy=(2053, 2.0), xytext=(2052.7, 2.4),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

# Modify the borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()