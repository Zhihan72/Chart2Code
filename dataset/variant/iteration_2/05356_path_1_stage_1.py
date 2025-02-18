import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = ['1990s', '2000s', '2010s', '2020s', '2030s', '2040s']

# Types of solar energy contributors
contributors = ['Residential PV', 'Commercial PV', 'Utility PV', 'CSP']

# Randomly altered percentage of solar energy contribution by each type
solar_adoption = np.array([
    [20, 40, 30, 10],  # 1990s
    [30, 25, 35, 10],  # 2000s
    [30, 30, 10, 30],  # 2010s
    [10, 35, 25, 30],  # 2020s
    [40, 25, 20, 15],  # 2030s
    [15, 50, 20, 15]   # 2040s
])

# Create a stacked area chart
plt.figure(figsize=(14, 8))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.stackplot(decades, solar_adoption.T, labels=contributors, colors=colors, alpha=0.85)

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