import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart illustrates the annual performance of four fictional superheroes in a superhero organization. Their total successful missions are broken down into three categories: Rescues, Battles, and Community Engagements. The chart aims to give a comparative overview of each superhero's annual contributions.

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

# Bar width
width = 0.2

# X positions for groups
x = np.arange(len(years))

# Plotting bars for each superhero
axs.bar(x - 1.5 * width, rescues[0], width, label='Captain Plasma - Rescues', color='#FF5733', edgecolor='black')
axs.bar(x - 0.5 * width, battles[0], width, label='Captain Plasma - Battles', color='#DAF7A6', edgecolor='black')
axs.bar(x + 0.5 * width, community[0], width, label='Captain Plasma - Community Engagements', color='#3498DB', edgecolor='black')

axs.bar(x - 1.5 * width + 1 * len(years), rescues[1], width, label='Mighty Wasp - Rescues', color='#581845', edgecolor='black')
axs.bar(x - 0.5 * width + 1 * len(years), battles[1], width, label='Mighty Wasp - Battles', color='#FFC300', edgecolor='black')
axs.bar(x + 0.5 * width + 1 * len(years), community[1], width, label='Mighty Wasp - Community Engagements', color='#DA70D6', edgecolor='black')

axs.bar(x - 1.5 * width + 2 * len(years), rescues[2], width, label='Red Cyclone - Rescues', color='#17A589', edgecolor='black')
axs.bar(x - 0.5 * width + 2 * len(years), battles[2], width, label='Red Cyclone - Battles', color='#A569BD', edgecolor='black')
axs.bar(x + 0.5 * width + 2 * len(years), community[2], width, label='Red Cyclone - Community Engagements', color='#F39C12', edgecolor='black')

axs.bar(x - 1.5 * width + 3 * len(years), rescues[3], width, label='Shadow Panther - Rescues', color='#2980B9', edgecolor='black')
axs.bar(x - 0.5 * width + 3 * len(years), battles[3], width, label='Shadow Panther - Battles', color='#E74C3C', edgecolor='black')
axs.bar(x + 0.5 * width + 3 * len(years), community[3], width, label='Shadow Panther - Community Engagements', color='#8E44AD', edgecolor='black')

# Add titles and labels
axs.set_title('Annual Performance of Superheroes in the Superhero Organization (2018-2022)', fontsize=16, fontweight='bold', pad=20)
axs.set_xlabel('Years', fontsize=12)
axs.set_ylabel('Number of Successful Missions', fontsize=12)

# Set x-axis ticks and labels
axs.set_xticks(np.concatenate([x + offset * len(years) for offset in range(4)]))
axs.set_xticklabels(years * 4, rotation=45)

# Add a legend
axs.legend(title='Mission Type', loc='upper right', frameon=True, fontsize=10)

# Add a grid
axs.yaxis.grid(True, linestyle='--', alpha=0.7)

# Customize spines
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)

# Adjust the layout
plt.tight_layout()

# Show plot
plt.show()