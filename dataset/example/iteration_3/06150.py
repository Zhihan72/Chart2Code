import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart presents the progression of the average monthly bandwidth consumption in Mbps 
# for a typical household from 2010 to 2022. It reflects the increasing trend due to the rise in video 
# streaming, online gaming, and teleworking.

# Data inputs
years = np.arange(2010, 2024)
bandwidth = [5, 8, 12, 18, 28, 40, 55, 70, 85, 100, 120, 150, 170, 200]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Main line plot
ax.plot(years, bandwidth, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8, label='Monthly Bandwidth (Mbps)')

# Annotations for key milestones in the bandwidth consumption history
milestones = {
    2010: "Video Streaming\nBoom Begins",
    2015: "4K Streaming\nBecomes Common",
    2020: "Shift to\nTeleworking",
    2022: "Rise of\n8K Streaming"
}

# Annotate milestones
for year, event in milestones.items():
    annotation_x = year
    annotation_y = bandwidth[years.tolist().index(year)]
    ax.annotate(
        event,
        xy=(annotation_x, annotation_y), 
        xytext=(annotation_x - 2.5, annotation_y + 30), 
        textcoords='data',
        arrowprops=dict(arrowstyle="->", color='grey'),
        color='black', fontsize=9, ha='right', bbox=dict(boxstyle="round,pad=0.3", edgecolor='grey', facecolor='lightyellow')
    )

# Customizing plot appearance
ax.set_title("Monthly Bandwidth Consumption: 2010-2022\nImpact of Streaming, Gaming, and Teleworking", fontsize=16, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Average Monthly Bandwidth (Mbps)", fontsize=12)

ax.set_xticks(years)
ax.set_xlim(2009, 2023)
ax.set_ylim(0, 220)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', frameon=False)

# Ensure layout fits all elements and text
plt.tight_layout()

# Display the plot
plt.show()