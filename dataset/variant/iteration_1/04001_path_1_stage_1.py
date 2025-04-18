import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define crop yield data (in tons) for each crop type (Wheat, Corn, Soybeans)
wheat_yield = np.array([2.5, 3.0, 3.1, 3.3, 3.4, 3.6, 3.7, 3.8, 4.0, 4.2, 4.3])
corn_yield = np.array([5.2, 5.0, 5.3, 5.5, 5.7, 5.8, 6.0, 6.2, 6.3, 6.5, 6.6])
soybean_yield = np.array([1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 2.0, 2.1, 2.2, 2.3, 2.5])

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with distinct markers and lines using new colors
ax.plot(years, wheat_yield, label='Wheat Yield', color='darkorange', marker='o', linewidth=2, linestyle='-')
ax.plot(years, corn_yield, label='Corn Yield', color='dodgerblue', marker='s', linewidth=2, linestyle='-.')
ax.plot(years, soybean_yield, label='Soybean Yield', color='mediumvioletred', marker='^', linewidth=2, linestyle='--')

# Enhance the plot with a title, labels, and legend
ax.set_title('A Farmer’s Journey:\nCrop Yields Over a Decade (2010-2020)',
             fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Yield (in tons)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, frameon=True)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Set x-axis ticks and rotate them for better visibility
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Highlight significant events with annotations
ax.annotate('Adoption of Sustainable Practices', xy=(2015, 3.6), xytext=(2013, 4.0),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Drought Year', xy=(2012, 5.0), xytext=(2009, 5.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('New Soybean Variety', xy=(2017, 2.1), xytext=(2015, 2.2),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()