import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart below shows the temperature variations on Mars during different months
# of its year. The data mimics how surface temperatures change across seasons
# from January (which corresponds to the Martian month Noachis) to December (Martian month Thaumasia).

# Martian months and corresponding simulated temperature data (in degrees Celsius)
months = np.array(['Noachis', 'Hellas', 'Solis', 'Tharsis', 'Amazonis', 'Elysium', 'Planum', 'Arcadia', 'Acidalia', 'Arabia', 'Elysium II', 'Thaumasia'])
mars_day = np.linspace(1, 12, num=12)  # Mars year divided into 12 equal months for simplicity

# Surface temperature data (constructed artificially)
north_temp = np.array([-60, -50, -45, -30, -35, -40, -55, -65, -70, -75, -80, -85])
south_temp = np.array([-65, -55, -50, -35, -40, -45, -60, -70, -75, -80, -85, -90])
equator_temp = np.array([-50, -45, -40, -30, -32, -35, -42, -50, -55, -60, -65, -70])

# Define the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot line charts for each zone
ax.plot(mars_day, north_temp, marker='o', color='r', label='Northern Hemisphere', linewidth=2)  # Northern Hemisphere
ax.plot(mars_day, south_temp, marker='s', color='b', label='Southern Hemisphere', linewidth=2)  # Southern Hemisphere
ax.plot(mars_day, equator_temp, marker='^', color='g', label='Equatorial Region', linewidth=2)   # Equatorial Region

# Add titles and labels for the axes
ax.set_title("Seasonal Temperature Variations on Mars", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Martian Months", fontsize=12)
ax.set_ylabel("Surface Temperature (°C)", fontsize=12)

# Set x-tick labels to Martian months
ax.set_xticks(mars_day)
ax.set_xticklabels(months, rotation=45, ha='right')

# Customize y-ticks
ax.set_yticks(np.arange(-90, -20, 5))

# Add gridlines for better readability
ax.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend
ax.legend(loc='upper right', fontsize=12, title='Mars Zones', title_fontsize='13', frameon=True)

# Annotations for critical points
ax.annotate('Warmest point\n(Northern Hemisphere)', xy=(4, -30), xytext=(6, -25),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax.annotate('Coldest point\n(Southern Hemisphere)', xy=(12, -90), xytext=(10, -85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

# Ensuring a tight layout
plt.tight_layout()

# Display the plot
plt.show()