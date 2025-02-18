import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tree Planting Campaign Progress Over a Year
# A hypothetical NGO "GreenEarth Guardians" conducts a tree-planting campaign across different locations
# throughout the year. The plot will show the number of trees planted each month in three different 
# regions: North, South, and Central.

# Defining the locations and months
locations = ['North Region', 'South Region', 'Central Region']
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Number of trees planted (in thousands)
north_trees = [15, 18, 22, 25, 28, 30, 32, 31, 29, 27, 26, 24]
south_trees = [10, 13, 18, 22, 27, 29, 33, 35, 34, 32, 30, 25]
central_trees = [8, 11, 15, 19, 24, 28, 30, 32, 33, 35, 34, 31]

# Define the positions of the bars on the x-axis
x = np.arange(len(months))
width = 0.25  # width of the bars

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each region's tree planting figures
bars1 = ax.bar(x - width, north_trees, width, label='North Region', color='forestgreen')
bars2 = ax.bar(x, south_trees, width, label='South Region', color='limegreen')
bars3 = ax.bar(x + width, central_trees, width, label='Central Region', color='mediumseagreen')

# Adding titles and labels
ax.set_title('GreenEarth Guardians: Annual Tree Planting Campaign\nNumber of Trees Planted in 2023 (in thousands)', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Number of Trees Planted (in thousands)', fontsize=14)

# Set the x-ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=12, rotation=45, ha='right')

# Annotate the bars with their respective values
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height), 
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')
        
annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

# Adding gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Adding a legend
ax.legend(title='Regions', title_fontsize='13', fontsize='12', loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()