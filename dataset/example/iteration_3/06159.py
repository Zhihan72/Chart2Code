import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the annual productivity of two different fruit farms (Farm A and Farm B) over a decade. 
# The data is fictional and crafted purely for demonstrating the trend analysis over time.

# Data Preparation: Productivity (in tons) of Farm A and Farm B over the years 2010 to 2020
years = np.arange(2010, 2021)
farm_a_productivity = np.array([35, 40, 42, 45, 50, 52, 55, 58, 60, 65, 70])
farm_b_productivity = np.array([30, 32, 35, 38, 42, 45, 50, 53, 55, 60, 65])

# Create subplots with different line types for different farms
fig, ax = plt.subplots(figsize=(14, 8))

# Plot Farm A productivity
ax.plot(years, farm_a_productivity, color='green', linestyle='-', linewidth=2, marker='o', label='Farm A')

# Plot Farm B productivity
ax.plot(years, farm_b_productivity, color='blue', linestyle='--', linewidth=2, marker='x', label='Farm B')

# Highlight specific year with annotations
highlight_year = 2015
highlight_a = farm_a_productivity[years.tolist().index(highlight_year)]
highlight_b = farm_b_productivity[years.tolist().index(highlight_year)]
ax.annotate(f"Farm A spike\nin {highlight_year}", xy=(highlight_year, highlight_a), xytext=(highlight_year, highlight_a + 10),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=12, ha='center', va='bottom', bbox=dict(boxstyle="round,pad=0.3", edgecolor='green', facecolor='white'))

ax.annotate(f"Farm B surge\nin {highlight_year}", xy=(highlight_year, highlight_b), xytext=(highlight_year + 1, highlight_b - 15),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=12, ha='center', va='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='blue', facecolor='white'))

# Setting the title, labels, and legend
ax.set_title("Decadal Productivity Trends of Fruit Farms (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, fontweight='bold')
ax.set_ylabel("Productivity (tons)", fontsize=12, fontweight='bold')

# Adding grid for better readability
ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

# Display the legend
ax.legend(title='Farms', title_fontsize=12, fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust plot params
plt.tight_layout()

# Show the plot
plt.show()