import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Randomly altered crop yield data while maintaining the original structure
wheat_yield = np.array([2.8, 3.3, 2.9, 3.1, 3.5, 3.7, 3.6, 4.0, 3.8, 4.1, 4.4])
corn_yield = np.array([5.3, 5.1, 6.0, 5.4, 5.6, 5.9, 6.1, 6.4, 5.8, 6.2, 6.7])
soybean_yield = np.array([1.1, 1.5, 1.6, 1.4, 1.8, 1.7, 2.1, 2.3, 2.0, 2.4, 2.6])

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot with distinct markers and lines
ax.plot(years, wheat_yield, label='Wheat Harvest', color='saddlebrown', marker='o', linewidth=2, linestyle='-')
ax.plot(years, corn_yield, label='Corn Production', color='gold', marker='s', linewidth=2, linestyle='-.')
ax.plot(years, soybean_yield, label='Soybean Output', color='green', marker='^', linewidth=2, linestyle='--')

# Title, labels, and legend
ax.set_title('Crop Growth Trends: 2010s', fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Production Volume (tons)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, frameon=True)

# Grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# X-axis ticks and rotation
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Significant events annotations
ax.annotate('Eco-Friendly Approaches Adopted', xy=(2015, 3.5), xytext=(2013, 4.0),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Year of Scarcity', xy=(2012, 6.0), xytext=(2009, 5.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Debut of New Soybean Type', xy=(2017, 2.3), xytext=(2015, 2.2),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')

# Layout adjustment
plt.tight_layout()

# Show the plot
plt.show()