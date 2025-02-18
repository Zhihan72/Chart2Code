import matplotlib.pyplot as plt
import numpy as np

# Data and backstory:
# Chart Type: Bar Chart
# Title: "Urbanization and Green Spaces: Balancing Development with Nature"
# Backstory: Over the past decade, urbanization in Portville has seen a rapid increase. To ensure a sustainable environment, the municipal government has balanced new construction projects with the development and preservation of green spaces. This chart shows the number of new constructions and the increase in green spaces each year.


# Data
years = np.arange(2010, 2021)
new_constructions = np.array([2, 4, 5, 8, 7, 10, 12, 15, 18, 20, 25])
green_spaces = np.array([1, 1, 2, 3, 5, 7, 8, 9, 12, 15, 17])

# Create a figure with a width longer than height to accommodate subplots
fig, ax1 = plt.subplots(figsize=(14, 7))

# Create bars for new constructions and green spaces
bar_width = 0.3
index = np.arange(len(years))

# Bar for new constructions
bars1 = ax1.bar(index, new_constructions, bar_width, color='skyblue', edgecolor='gray', label='New Constructions')

# Bar for green spaces
bars2 = ax1.bar(index + bar_width, green_spaces, bar_width, color='lightgreen', edgecolor='gray', label='Green Spaces')

# Auxiliary information for the chart
ax1.set_title("Urbanization and Green Spaces: Balancing Development with Nature\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Count", fontsize=12)
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate each bar with the count values
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', fontsize=10, color='darkslategray')

# Add a subtitle for additional explanation
plt.suptitle("Portville: Sustainable Development Initiatives", fontsize=14, y=0.97)

# Automatically adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Display the plot
plt.show()