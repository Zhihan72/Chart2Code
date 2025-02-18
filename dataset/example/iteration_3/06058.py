import matplotlib.pyplot as plt
import numpy as np

# The backstory:
# This chart depicts the growth in flora diversity in a fictional ecosystem, "FloraLand," from the years 2000 to 2020.
# The three types of flora include Trees, Shrubs, and Wildflowers. The goal is to visualize how biodiversity has improved due to various conservation efforts.

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Flora diversity data (number of species)
# Manually creating data to show trends in increasing flora diversity.
trees = np.array([50, 52, 54, 58, 64, 70, 75, 80, 85, 87, 89, 90, 92, 94, 95, 97, 98, 100, 103, 107, 110])
shrubs = np.array([30, 32, 34, 36, 38, 40, 44, 48, 50, 53, 56, 58, 60, 64, 68, 72, 76, 78, 80, 82, 85])
wildflowers = np.array([20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180])

# Stack the data
flora_data = np.vstack([trees, shrubs, wildflowers])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 9))

# Create the stacked area plot
ax.stackplot(years, flora_data, labels=['Trees', 'Shrubs', 'Wildflowers'], 
             colors=['#228B22', '#8FBC8F', '#FFD700'], alpha=0.7)

# Adding chart details
ax.set_title("Flora Diversity in FloraLand (2000-2020):\nA Journey of Conservation and Growth", 
             fontsize=18, weight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Species", fontsize=14)
ax.set_xticks(years[::2])  # Show every other year for clarity
ax.set_xticklabels(years[::2], rotation=45)
ax.set_yticks(np.arange(0, 221, 20))
ax.legend(loc='upper left', fontsize=12, frameon=True)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add annotations for significant milestones
ax.annotate("Major Reforestation Efforts", xy=(2008, 90), xytext=(2005, 150),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='darkgreen'), fontsize=12, color='darkgreen')

ax.annotate("Shrubland Recovery Program", xy=(2014, 64), xytext=(2010, 180),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='olive'), fontsize=12, color='olive')

ax.annotate("Wildflower Meadow Initiative", xy=(2018, 150), xytext=(2015, 220),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='gold'), fontsize=12, color='gold')

# Automatically adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()