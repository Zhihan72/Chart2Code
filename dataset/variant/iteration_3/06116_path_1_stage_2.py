import matplotlib.pyplot as plt
import numpy as np

# Define the superheroes and their missions
superheroes = ["Captain Plasma", "Mighty Wasp", "Red Cyclone", "Shadow Panther"]
years = ["2018", "2019", "2020", "2021", "2022"]

# Success metrics for each superhero over the years
rescues = np.array([
    [120, 130, 150, 140, 170],
    [90, 100, 110, 105, 120],
    [80, 85, 95, 100, 110],
    [110, 115, 120, 130, 135]
])
battles = np.array([
    [80, 95, 105, 100, 110],
    [60, 70, 80, 75, 85],
    [75, 80, 90, 85, 95],
    [90, 100, 110, 105, 115]
])
community = np.array([
    [30, 40, 50, 45, 55],
    [20, 25, 30, 35, 40],
    [25, 30, 35, 40, 45],
    [35, 40, 45, 50, 55]
])

# Create figure and axes
fig, axs = plt.subplots(figsize=(14, 8))
width = 0.3  # Bar width
x = np.arange(len(years))

# Plotting the diverging bar chart stacks
for i, hero in enumerate(superheroes):
    axs.bar(x, rescues[i], width, label=f'{hero} - Rescues', color='#3498DB', edgecolor='black', bottom=battles[i]+community[i])
    axs.bar(x, battles[i], width, label=f'{hero} - Battles', color='#FF5733', edgecolor='black', bottom=community[i])
    axs.bar(x, community[i], width, label=f'{hero} - Community Engagements', color='#DAF7A6', edgecolor='black')
    x = x + width  # Shift x position for the next superhero

# Add titles and labels
axs.set_title('Diverging Bar Chart for Superheroes (2018-2022)', fontsize=16, fontweight='bold', pad=20)
axs.set_xlabel('Years', fontsize=12)
axs.set_ylabel('Number of Missions', fontsize=12)

# Set x-axis ticks and labels
axs.set_xticks(np.arange(len(years)) + 1.5 * width)
axs.set_xticklabels(years, rotation=45)

# Add a legend
axs.legend(title='Mission Type', loc='upper left', bbox_to_anchor=(1,1), frameon=True, fontsize=10)

# Add a grid
axs.yaxis.grid(True, linestyle='--', alpha=0.7)

# Customize spines
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)

# Adjust the layout
plt.tight_layout()

# Show plot
plt.show()