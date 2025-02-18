import matplotlib.pyplot as plt
import numpy as np

# Define the years for the trend analysis
years = np.arange(2040, 2071)

# Define the production volumes for each crop in tons per year, excluding Leafy Greens
tubers = np.array([10, 12, 14, 18, 22, 28, 34, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155])
legumes = np.array([5, 7, 9, 12, 16, 20, 25, 30, 36, 42, 48, 55, 62, 70, 78, 87, 96, 106, 116, 127, 138, 150, 162, 175, 188, 202, 216, 231, 246, 262, 278])
fruits = np.array([2, 3, 5, 7, 10, 15, 20, 26, 32, 39, 46, 54, 63, 72, 82, 92, 103, 114, 126, 139, 152, 166, 181, 196, 212, 229, 247, 266, 285, 305, 325])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot production volumes, excluding Leafy Greens
ax.stackplot(years, tubers, legumes, fruits,
             labels=['Tubers', 'Legumes', 'Fruits'],
             colors=['#FFD700', '#98FB98', '#FF6347'], alpha=0.7)

# Set the title and labels
ax.set_title("Mars Colony Annual Food Production (2040-2070)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Production Volume (Tons)", fontsize=14)

# Customize the ticks on the x-axis
ax.set_xticks(years[::2])
ax.tick_params(axis='x', rotation=45)

# Add a legend with custom styling
ax.legend(loc='upper left', title="Crop Varieties", fontsize=12, title_fontsize='13', frameon=False)

# Enhance grid
ax.grid(linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)

# Create an annotation for a significant milestone
ax.annotate('Introduction of Advanced Agriculture Technology', xy=(2055, 240), xytext=(2045, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkred')

# Add a description box detailing the trend
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.2)
textstr = ('This chart showcases the increasing\n'
           'food production volumes in the Mars colony,\n'
           'highlighting the impact of advanced\n'
           'agricultural technologies on crop yields.')
ax.text(0.03, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()