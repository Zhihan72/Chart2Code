import numpy as np
import matplotlib.pyplot as plt

# Define years and market share data for each smartphone brand
years = np.arange(2020, 2031)
brand_a = np.array([30, 35, 40, 45, 50, 52, 50, 49, 48, 47, 46])
brand_b = np.array([20, 22, 24, 25, 27, 30, 32, 33, 34, 34, 34])
brand_c = np.array([10, 11, 12, 15, 17, 19, 21, 22, 22, 23, 23])
brand_d = np.array([15, 14, 13, 12, 10, 9, 8, 8, 8, 9, 10])
brand_e = np.array([25, 18, 11, 3, 1, 1, 1, 1, 1, 1, 1])

# Create stacked data
data = np.vstack([brand_a, brand_b, brand_c, brand_d, brand_e])

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, data, labels=["Alpha Phones", "Beta Tech", "Gamma Gadgets", "Delta Devices", "Epsilon Enterprises"], 
             colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CCD1FF'], alpha=0.8)

# Titles and labels with alterations
ax.set_title('Tech City Mobile Growth (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline (Years)', fontsize=12)
ax.set_ylabel('Ownership (%)', fontsize=12)

# Set x-ticks and rotate them if necessary
ax.set_xticks(years)
ax.set_xticklabels(years)

# Add grid and legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=10, title='Market Share Leaders')

# Annotate key market shifts with altered text
ax.annotate('Alpha Dominance', xy=(2021, 35), xytext=(2023, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Epsilon Eradication', xy=(2020, 25), xytext=(2020, 45),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Ensure the layout is adjusted for better readability
plt.tight_layout()

# Show the plot
plt.show()