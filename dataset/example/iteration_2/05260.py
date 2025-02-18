import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# "In 2023, the Global Culinary Association conducted an extensive survey to rank different regions by their consumption of various popular cuisines. The regions evaluated include North America, Europe, Asia, South America, and Africa. This chart showcases the popularity of different cuisines across these regions."

# Data preparation
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
italian_cuisine = [80, 85, 70, 60, 50]
chinese_cuisine = [75, 70, 90, 55, 60]
mexican_cuisine = [65, 60, 50, 80, 40]
indian_cuisine = [55, 65, 85, 50, 70]

# Create a map of data for easy plotting
cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian']
data = [italian_cuisine, chinese_cuisine, mexican_cuisine, indian_cuisine]
colors = ['#FF4500', '#228B22', '#4169E1', '#FFD700']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Width of a single bar segment
bar_width = 0.2

# Create bar positions
positions = np.arange(len(regions))

# Plot the bars for each cuisine
for i, (cuisine, popularity) in enumerate(zip(cuisines, data)):
    ax.bar(positions + i * bar_width, popularity, width=bar_width, color=colors[i], edgecolor='grey', label=cuisine, alpha=0.8)

# Titles and labels
ax.set_title("Cuisine Popularity Across Regions in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Regions", fontsize=14)
ax.set_ylabel("Popularity Score", fontsize=14)

# Customizing ticks on the x-axis
ax.set_xticks(positions + bar_width * 1.5)
ax.set_xticklabels(regions, fontsize=12)

# Customizing y-axis grid and ticks
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.yaxis.set_ticks(np.arange(0, 101, 10))

# Add legend with a horizontal layout to avoid overlap
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1.01, 1), borderaxespad=0.)

# Automatically adjust layout to prevent text cutoff
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()