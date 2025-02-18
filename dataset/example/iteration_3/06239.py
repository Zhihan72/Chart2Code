import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We're tracking the global sales data of different types of electric vehicles from 2015 to 2025. 
# This is a period of rapid technological advancement, with Electric Sedans, SUVs, Hatchbacks, and Trucks 
# occupying significant market shares over these years. We aim to visualize this evolution in a comprehensive manner.

# Define the years from 2015 to 2025
years = np.arange(2015, 2026)

# Sales data (in millions) for each type of electric vehicle
sedans_sales = np.array([0.2, 0.4, 0.6, 0.85, 1.2, 1.5, 2.0, 2.4, 2.8, 3.3, 3.8])
suvs_sales = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 1.3, 1.7, 2.1, 2.5, 3.0, 3.5])
hatchbacks_sales = np.array([0.05, 0.1, 0.25, 0.35, 0.45, 0.65, 0.8, 0.9, 1.1, 1.3, 1.4])
trucks_sales = np.array([0.01, 0.05, 0.1, 0.25, 0.45, 0.7, 1.0, 1.4, 1.8, 2.2, 2.6])

# Stack the data for the area chart
sales_data = np.vstack([sedans_sales, suvs_sales, hatchbacks_sales, trucks_sales])

# Define colors for each type of electric vehicle
colors = ['#ffadad', '#ffdae4', '#ffd6a5', '#fdffb6']

# Create the area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, sales_data, labels=['Sedans', 'SUVs', 'Hatchbacks', 'Trucks'], colors=colors, alpha=0.85)

# Customize the chart
ax.set_title('Global Electric Vehicle Sales Growth (2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales (in millions)', fontsize=12)

# Add grid and legend
ax.grid(linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=12, title='Vehicle Types')

# Ticks and axis limits
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 4.1, 0.5))
ax.set_xlim(2015, 2025)
ax.set_ylim(0, 4)

# Rotate x-tick labels to avoid overlap
plt.xticks(rotation=45)

# Annotate significant increase points
ax.annotate('Massive Adoption of Electric SUVs', xy=(2022, suvs_sales[7]), xytext=(2018, 2), 
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='blue')

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()