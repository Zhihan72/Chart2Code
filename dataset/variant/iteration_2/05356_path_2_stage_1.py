import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = ['1990s', '2000s', '2010s', '2020s', '2030s', '2040s']

# Types of solar energy contributors
contributors = ['Residential PV', 'Commercial PV', 'Utility PV', 'CSP']

# Percentage of solar energy contribution by each type over the decades
solar_adoption = np.array([
    [20, 30, 40, 10],
    [25, 35, 30, 10],
    [30, 30, 30, 10],
    [35, 25, 30, 10],
    [40, 20, 25, 15],
    [50, 15, 20, 15]
])

# Create a stacked area chart with new colors
plt.figure(figsize=(14, 8))
new_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
plt.stackplot(decades, solar_adoption.T, labels=contributors, colors=new_colors, alpha=0.85)

# Chart details
plt.title("Adoption of Solar Power Technologies\nFrom the 1990s to 2040s", fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Contribution to Solar Power Adoption (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left', title='Solar Energy Contributors', bbox_to_anchor=(1.05, 1), borderaxespad=0)
plt.grid(True, linestyle='--', alpha=0.7)

# Annotate key developments
plt.annotate('Rise of Residential PV', xy=('2030s', 40), xytext=('2020s', 60),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='darkgreen')
plt.annotate('Significant CSP Influence', xy=('2040s', 80), xytext=('2030s', 75),
             arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=10, color='darkorange')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display plot
plt.show()