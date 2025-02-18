import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Sea ice extent (in million square kilometers) for different months
march_extent = [15.64, 15.61, 15.48, 15.36, 15.25, 14.94, 14.80, 14.71, 14.65, 14.55, 14.35, 14.26, 14.16, 14.10, 14.04, 13.91, 13.83, 13.80, 13.66, 13.54, 13.41]
june_extent = [11.34, 11.29, 11.23, 11.08, 10.94, 10.74, 10.51, 10.33, 10.14, 10.05, 9.91, 9.75, 9.59, 9.41, 9.28, 9.13, 9.00, 8.89, 8.75, 8.65, 8.53]
september_extent = [6.41, 6.37, 6.30, 6.14, 5.97, 5.75, 5.55, 5.36, 5.20, 5.10, 4.92, 4.76, 4.63, 4.50, 4.38, 4.24, 4.12, 4.00, 3.88, 3.76, 3.67]
december_extent = [13.54, 13.52, 13.49, 13.42, 13.30, 13.11, 12.93, 12.82, 12.63, 12.48, 12.30, 12.13, 11.96, 11.81, 11.67, 11.52, 11.38, 11.27, 11.15, 11.03, 10.91]

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors and markers for different months
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
months = ['March', 'June', 'September', 'December']
extents = [march_extent, june_extent, september_extent, december_extent]
markers = ['x', '*', 'o', 's'] # Changed markers
linestyles = ['-', '--', '-.', ':'] # Introduced line styles

# Plot the sea ice extent data
for extent, month, color, marker, linestyle in zip(extents, months, colors, markers, linestyles):
    ax.plot(years, extent, label=month, color=color, marker=marker, linestyle=linestyle, linewidth=1.5)

    # Annotate data points with the extent values in million square kilometers
    for (x, y) in zip(years, extent):
        ax.annotate(f'{y:.2f}M', xy=(x, y), xytext=(-2, 5),
                     textcoords='offset points', ha='center', fontsize=8, color=color)

# Set title and labels
ax.set_title('Arctic Sea Ice Extent (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Extent (Million km²)', fontsize=12)

# Add gridlines with different style
ax.grid(True, linestyle=':', which='major', color='grey', alpha=0.7)

# Remove the horizontal line and the text annotation

# Changed legend to have a frame
ax.legend(title='Months', title_fontsize='13', loc='lower left', frameon=True, framealpha=0.9, edgecolor='black')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()