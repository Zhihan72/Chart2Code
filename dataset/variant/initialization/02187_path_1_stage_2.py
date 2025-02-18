import matplotlib.pyplot as plt
import numpy as np

years = np.array([2050, 2051, 2052, 2053, 2054])
martian_potatoes = np.array([1.2, 1.5, 1.7, 2.0, 2.3])
space_carrots = np.array([1.0, 1.2, 1.5, 1.7, 2.1])

plt.figure(figsize=(10, 6))

# Use a single consistent color for both crop types
plt.plot(years, martian_potatoes, marker='o', linestyle='-', linewidth=2, color='tab:green', label='Martian Potatoes')
plt.plot(years, space_carrots, marker='^', linestyle='-', linewidth=2, color='tab:green', label='Space Carrots')

plt.title('Extraterrestrial Agriculture: \nCrop Yields on Mars (2050-2054)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Yield (tons per Martian acre)', fontsize=12)

plt.xticks(years)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.legend(loc='upper left', fontsize=10)

plt.annotate('Experimentation begins', xy=(2050, 1.2), xytext=(2050, 1.5),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

plt.annotate('Optimal conditions achieved', xy=(2053, 2.0), xytext=(2052.7, 2.4),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

plt.tight_layout()
plt.show()