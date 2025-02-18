import matplotlib.pyplot as plt
import numpy as np

# Data: Average Noise Levels in Decibels (dB) for Residential, Commercial, and Industrial areas during Day and Night
residential_day = np.array([45, 50, 55, 47, 52, 53, 48, 50, 51, 49])
residential_night = np.array([35, 38, 40, 36, 39, 37, 34, 36, 38, 37])
commercial_day = np.array([65, 68, 70, 66, 69, 67, 70, 71, 68, 66])
commercial_night = np.array([55, 58, 60, 56, 59, 57, 54, 59, 60, 58])
industrial_day = np.array([75, 80, 85, 78, 82, 81, 79, 77, 80, 78])
industrial_night = np.array([65, 68, 70, 66, 69, 68, 67, 66, 68, 67])

# Aggregate data for plotting
data_violin = [residential_day, residential_night, commercial_day, commercial_night, industrial_day, industrial_night]
scenarios = ['Residential Day', 'Residential Night', 'Commercial Day', 'Commercial Night', 'Industrial Day', 'Industrial Night']

# Create figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Violin plot with additional enhancements (horizontal)
vparts = ax.violinplot(data_violin, vert=False, showmedians=True, showmeans=True, showextrema=True, widths=0.7)

# Set color palette
colors = ['#FF8C00', '#FFA500', '#5F9EA0', '#7FFFD4', '#8B0000', '#CD5C5C']

# Customize violin plot appearances
for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.6)
    
# Customize median, mean and quartiles
for partname in ('cbars', 'cmeans', 'cmedians'):
    vparts[partname].set_edgecolor('black')
    vparts[partname].set_linewidth(1.5)

# Title and labels
ax.set_title("Noise Pollution Levels in Different Urban Scenarios\nDuring Day and Night", fontsize=18, fontweight='bold')
ax.set_xlabel("Noise Levels (dB)", fontsize=14)
ax.set_ylabel("Urban Scenario", fontsize=14)
ax.set_yticks(np.arange(1, len(scenarios) + 1))
ax.set_yticklabels(scenarios, fontsize=12)

# Grid and layout adjustments
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Shared legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(handles, scenarios, title="Scenarios", loc='upper right', fontsize=12, title_fontsize='13')

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Display the chart
plt.show()