import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Fictional Data Story: Analyzing Productivity of Various Teams Over Years in "Tech Innovations Inc."
teams = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta"]
years = np.arange(2015, 2022) # Data from 2015 to 2021

# Monthly productivity data (each entry represents the average monthly productivity score for a particular year and team)
productivity_data = np.array([
    [65, 70, 75, 80, 78, 82, 87],   # Alpha
    [68, 73, 72, 76, 79, 83, 88],   # Beta
    [70, 75, 78, 82, 84, 86, 90],   # Gamma
    [72, 78, 81, 85, 88, 90, 93],   # Delta
    [65, 68, 72, 75, 79, 82, 85],   # Epsilon
    [68, 72, 76, 80, 83, 86, 88],   # Zeta
    [67, 70, 74, 78, 81, 83, 87],   # Eta
    [66, 70, 73, 76, 79, 81, 84]    # Theta
]).T  # Transpose to align years with rows for the heatmap

# Calculate average productivity for a separate subplot
average_productivity = np.mean(productivity_data, axis=0)

# Create the figure and axes using gridspec for better layout control
fig = plt.figure(figsize=(18, 10))
gs = gridspec.GridSpec(2, 2, height_ratios=[4, 1], width_ratios=[4, 1])

# Main heatmap plot
ax1 = plt.subplot(gs[:, 0])
heatmap1 = ax1.imshow(productivity_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')

# Add title and labels
ax1.set_title("Team Productivity Over the Years at Tech Innovations Inc.", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Teams', fontsize=12)
ax1.set_ylabel('Year', fontsize=12)
ax1.set_xticks(np.arange(len(teams)))
ax1.set_xticklabels(teams, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(years)))
ax1.set_yticklabels(years)

# Add a color bar for heatmap
cbar1 = plt.colorbar(heatmap1, ax=ax1, orientation='vertical')
cbar1.set_label('Monthly Productivity Score', fontsize=12)

# Annotate heatmap
for i in range(len(years)):
    for j in range(len(teams)):
        ax1.text(j, i, productivity_data[i, j], ha='center', va='center', color='black', fontsize=8)

# Subplot for the average productivity bar chart
ax2 = plt.subplot(gs[1, 1])
bar_chart = ax2.barh(teams, average_productivity, color='skyblue', edgecolor='black')
ax2.set_title('Average Productivity Score per Team (2015-2021)', fontsize=12, pad=10)
ax2.set_xlabel('Average Productivity Score', fontsize=10)
ax2.set_xlim(60, 95) # Setting the limit to ensure consistency in view

# Annotate bars
for bar in bar_chart:
    width = bar.get_width()
    ax2.text(width - 4, bar.get_y() + bar.get_height() / 2, f'{width:.1f}', va='center', ha='center', color='black', fontsize=10)

# Additional heatmap for productivity improvement trend
yearly_trend = np.diff(productivity_data, axis=0)
ax3 = plt.subplot(gs[0, 1])
heatmap2 = ax3.imshow(yearly_trend, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Add title and labels
ax3.set_title("Year-over-Year Productivity Change", fontsize=12, pad=10)
ax3.set_xlabel('Teams', fontsize=10)
ax3.set_ylabel('Year Difference', fontsize=10)
ax3.set_xticks(np.arange(len(teams)))
ax3.set_xticklabels(teams, rotation=45, ha='right')
ax3.set_yticks(np.arange(1, len(years)))
ax3.set_yticklabels([f'{years[i-1]}-{years[i]}' for i in range(1, len(years))])

# Add a color bar for heatmap
cbar2 = plt.colorbar(heatmap2, ax=ax3, orientation='vertical')
cbar2.set_label('Change in Productivity Score', fontsize=10)

# Annotate heatmap with changes
for i in range(len(yearly_trend)):
    for j in range(len(teams)):
        ax3.text(j, i, f'{yearly_trend[i, j]:+.1f}', ha='center', va='center', color='black', fontsize=8)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()