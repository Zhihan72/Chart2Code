import matplotlib.pyplot as plt
import numpy as np

# Define the backstory and data:
# Imaginary scenario: Studying the diversity in the flavor profile of different chocolate brands over several years.
chocolate_brands = ["CocoaHeaven", "ChocoDelight", "SweetCocoa", "DarkFantasy", "ChocoTwist"]
years = ["2015", "2016", "2017", "2018", "2019"]

# Constructing data without random values
chocolate_data = {
    "CocoaHeaven": [75, 80, 78, 85, 82],
    "ChocoDelight": [70, 75, 72, 78, 79],
    "SweetCocoa": [68, 72, 70, 74, 69],
    "DarkFantasy": [80, 85, 83, 88, 86],
    "ChocoTwist": [65, 67, 66, 70, 68],
}

# Box plot data preparation, transposing for correct orientation
box_data = [list(year_data) for year_data in zip(*chocolate_data.values())]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the boxplot
bplot = ax.boxplot(box_data, vert=True, patch_artist=True, notch=False,
                   boxprops=dict(facecolor='lightyellow', color='brown'),
                   whiskerprops=dict(color='brown'),
                   capprops=dict(color='brown'),
                   medianprops=dict(color='darkred', linewidth=2),
                   flierprops=dict(markerfacecolor='blue', marker='o', markersize=8, linestyle='none'))

# Color each box differently
colors = ['#FFD700', '#FF6347', '#8B0000', '#3CB371', '#4682B4']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Setting axis labels and title
ax.set_xticklabels(years)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Flavor Score', fontsize=12)
ax.set_title('Flavor Diversity Across Different Chocolate Brands\n(2015-2019)', fontsize=14, fontweight='bold')

# Customize other elements
ax.set_ylim(60, 90)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding legend
patches = [plt.plot([],[], marker="s", ms=10, ls="", mec=None, color=colors[i], 
            label="{:s}".format(chocolate_brands[i]))[0] for i in range(len(chocolate_brands))]
ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title="Chocolate Brands")

# Enhance layout for better visual fit
plt.tight_layout()

# Display the plot
plt.show()