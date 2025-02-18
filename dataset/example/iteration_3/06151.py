import matplotlib.pyplot as plt
import numpy as np

# Backstory: City Green Initiative
# The city has been tracking the annual number of trees planted in different districts as part of a green initiative to improve urban greenery. 

# Define data: Years and number of trees planted in three different districts
years = np.arange(2015, 2021)
districtA_trees = np.array([500, 550, 620, 700, 750, 800])
districtB_trees = np.array([600, 620, 640, 680, 720, 760])
districtC_trees = np.array([450, 480, 520, 560, 590, 620])

# Define the bar width and positions
bar_width = 0.25
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the figure and ax (the subplot)
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data for each district
ax.bar(r1, districtA_trees, color='blue', width=bar_width, edgecolor='grey', label='District A')
ax.bar(r2, districtB_trees, color='green', width=bar_width, edgecolor='grey', label='District B')
ax.bar(r3, districtC_trees, color='red', width=bar_width, edgecolor='grey', label='District C')

# Add titles and labels
ax.set_xlabel('Year', fontweight='bold', fontsize=12)
ax.set_ylabel('Number of Trees Planted', fontweight='bold', fontsize=12)
ax.set_title('Annual Number of Trees Planted\nDifferent Districts (2015-2020)', fontweight='bold', fontsize=14)
ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels(years)

# Add legend
ax.legend()

# Customize the grid and layout
ax.grid(True, linestyle='--', alpha=0.6, axis='y')
plt.tight_layout()

# Highlight significant years
ax.annotate('Green Milestone Reached', xy=(4, 750), xytext=(2, 820),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Ensure layout is tidy
plt.tight_layout()

# Display the plot
plt.show()