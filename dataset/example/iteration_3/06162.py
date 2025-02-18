import matplotlib.pyplot as plt
import numpy as np

# Backstory and Data:
# Imagine humanity's journey in space colonization, focusing on settlements across different celestial bodies 
# over the years as technology and resources become available.

# Defining years of space exploration and colonization advancements
years = np.arange(2040, 2061)

# Number of settlements established over the years on different celestial bodies
moon = np.array([0, 2, 5, 7, 10, 14, 18, 21, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55])
mars = np.array([0, 0, 1, 3, 6, 10, 14, 17, 20, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 56, 60])
europa = np.array([0, 0, 0, 1, 3, 5, 8, 11, 14, 17, 20, 22, 24, 26, 30, 33, 35, 37, 40, 43, 45])
titan = np.array([0, 0, 0, 0, 1, 2, 3, 5, 7, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25])

# Securing the data for stackplot
data = np.vstack([moon, mars, europa, titan])

# Colors for celestial bodies
colors = ['#FFD700', '#FF4500', '#1E90FF', '#8A2BE2']

# Creating a stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
ax.stackplot(years, data, labels=['Moon', 'Mars', 'Europa', 'Titan'], colors=colors, alpha=0.85)

# Adding title and labels
ax.set_title("Evolution of Human Settlements Across Celestial Bodies (2040-2060)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Settlements", fontsize=12)
ax.legend(loc='upper left', title="Celestial Bodies", fontsize=10, title_fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations highlighting significant milestones
annotations = {2045: "First Mars Settlement", 2050: "Rapid Growth on Moon", 2055: "Europa Settlements Begin"}
for year, label in annotations.items():
    y_pos = data.sum(axis=0)[np.where(years == year)[0]][0] + 5  # Position annotations above the cumulative sum
    ax.annotate(label, xy=(year, y_pos), xytext=(year + 1, y_pos + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Add secondary plot: Percentage of total settlements
total_settlements = moon + mars + europa + titan
perc_moon = 100 * moon / total_settlements
perc_mars = 100 * mars / total_settlements
perc_europa = 100 * europa / total_settlements
perc_titan = 100 * titan / total_settlements

ax2 = ax.twinx()
ax2.plot(years, perc_moon, 'o--', color='#FFD700', label='Moon (%)')
ax2.plot(years, perc_mars, 'o--', color='#FF4500', label='Mars (%)')
ax2.plot(years, perc_europa, 'o--', color='#1E90FF', label='Europa (%)')
ax2.plot(years, perc_titan, 'o--', color='#8A2BE2', label='Titan (%)')
ax2.set_ylabel("Percentage of Total Settlements (%)", fontsize=12)
ax2.set_ylim(0, 100)

# Legend for secondary plot
ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(0.95, 0.85), title="Settlement Proportions (%)", title_fontsize=12)

# Use tight layout to prevent clipping of labels and adjust overlaps
plt.tight_layout()

# Display the plot
plt.show()