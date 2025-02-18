import matplotlib.pyplot as plt
import numpy as np

# Backstory: A new fictional city, NeoMetropolis, has been founded in 2000. Over the last 20 years, the city has seen significant growth in various sectors. One way to track this growth is by looking at the population, the number of businesses, and average household incomes. This chart will visualize these trends from 2000 to 2020.

# Time period for the x-axis
years = np.arange(2000, 2021)

# Population data (in thousands)
population = np.array([
    150, 154, 158, 165, 170, 176, 183, 190, 198, 210,
    222, 235, 248, 260, 272, 285, 297, 310, 325, 340, 355
])

# Number of businesses data (in hundreds)
businesses = np.array([
    50, 55, 60, 65, 68, 72, 80, 87, 93, 100,
    108, 117, 125, 133, 142, 150, 158, 165, 175, 185, 195
])

# Average household income data (in thousands of dollars)
household_income = np.array([
    35, 36, 38, 40, 42, 45, 48, 50, 53, 56,
    60, 63, 67, 70, 74, 78, 82, 86, 90, 94, 98
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each data set
ax.plot(years, population, label="Population (in thousands)", color='blue', linestyle='-', marker='o', linewidth=2)
ax.plot(years, businesses, label="Number of Businesses (in hundreds)", color='green', linestyle='-', marker='s', linewidth=2)
ax.plot(years, household_income, label="Average Household Income (in thousands)", color='red', linestyle='-', marker='^', linewidth=2)

# Set chart title and labels
ax.set_title("Growth Trends in NeoMetropolis (2000-2020)\nPopulation, Number of Businesses, and Average Household Income", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Metrics", fontsize=14)

# Add legend and grid
ax.legend(loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

# Configure x-axis tick marks
ax.set_xticks(np.arange(2000, 2021, 2))

# Highlight significant milestones
milestones = [(2005, 'City Development Plan'), (2010, 'Major Business Investments'), (2015, 'Population Boom')]
for year, event in milestones:
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)
    ax.annotate(event, 
                xy=(year, ax.get_ylim()[1]), 
                xytext=(year, ax.get_ylim()[1] * 1.1),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                fontsize=10, 
                ha='center', 
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

# Ensure layout is not overlapping
plt.tight_layout()

# Display the plot
plt.show()