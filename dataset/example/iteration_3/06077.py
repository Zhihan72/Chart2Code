import matplotlib.pyplot as plt
import numpy as np

# Backstory: Studying the Accelerating Growth of Urban Green Spaces
# Over the decades, urban areas have been increasingly adopting green spaces to combat pollution and enhance well-being.
# We will analyze the growth in three major types of green spaces: Urban Parks, Roof Gardens, and Green Walls from 2000 to 2050.

# Years for the x-axis
years = np.arange(2000, 2051)

# Data: Growth in square kilometers (sq km) for each type of green space
urban_parks = np.linspace(50, 500, len(years))  # Linear growth
roof_gardens = 20 + 10 * np.log1p(years - 2000)  # Logarithmic growth
green_walls = 5 + (years - 2000) ** 1.5  # Polynomial growth

# Creating a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Main line chart for the growth of each green space type
ax1.plot(years, urban_parks, label='Urban Parks', color='#63A375', linewidth=2, marker='o')
ax1.plot(years, roof_gardens, label='Roof Gardens', color='#E6B655', linewidth=2, marker='s')
ax1.plot(years, green_walls, label='Green Walls', color='#A44A3F', linewidth=2, marker='^')

# Adding titles and labels with line breaks for clarity
ax1.set_title('Growth of Urban Green Spaces (2000-2050)\nFostering Sustainable Urbanization', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Area (sq km)', fontsize=14)
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)

# Adding annotations for notable years
ax1.annotate('Significant Uptake Post-2025', xy=(2025, 150), xytext=(2030, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Histogram data: Frequency of expansion projects by type
expansion_projects_urban_parks = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
expansion_projects_roof_gardens = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
expansion_projects_green_walls = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Binning the years into half of decade
decades = np.arange(2000, 2060, 5)

# Secondary plot: Stacked bar chart of expansion projects by type
width = 8  # width of the bars
ax2.bar(decades - width, expansion_projects_urban_parks, width, label='Urban Parks', color='#63A375')
ax2.bar(decades, expansion_projects_roof_gardens, width, label='Roof Gardens', color='#E6B655')
ax2.bar(decades + width, expansion_projects_green_walls, width, label='Green Walls', color='#A44A3F')

# Adding titles and labels with line breaks for clarity
ax2.set_title('Number of Expansion Projects by Decade\n(2000-2050)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Decade', fontsize=14)
ax2.set_ylabel('Number of Projects', fontsize=14)
ax2.set_xticks(decades)
ax2.legend(loc='upper left', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()