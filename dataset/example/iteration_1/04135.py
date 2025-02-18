import matplotlib.pyplot as plt
import numpy as np

# Backstory: Charting the Evolution of Time Spent on Different Leisure Activities
# This bar chart will visualize how the average time spent on various leisure activities has evolved over three decades: the 1980s, 2000s, and 2020s.

# Define activities and time spent in minutes per day for each decade
activities = ['Reading', 'TV Watching', 'Video Games', 'Socializing', 'Physical Activity', 'Travel for Leisure']
time_1980s = [45, 120, 15, 60, 30, 10]
time_2000s = [25, 150, 45, 80, 40, 25]
time_2020s = [35, 100, 70, 50, 60, 30]

# Combine data into a single array for plotting
time_data = np.array([time_1980s, time_2000s, time_2020s])
decades = ['1980s', '2000s', '2020s']

# Define the width of each bar
bar_width = 0.25

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Set position of bar on X axis for each decade
positions_1980s = np.arange(len(activities))
positions_2000s = [x + bar_width for x in positions_1980s]
positions_2020s = [x + bar_width for x in positions_2000s]

# Make the bar plots
bars_1980s = ax.bar(positions_1980s, time_1980s, width=bar_width, color='#1f77b4', edgecolor='grey', label='1980s')
bars_2000s = ax.bar(positions_2000s, time_2000s, width=bar_width, color='#ff7f0e', edgecolor='grey', label='2000s')
bars_2020s = ax.bar(positions_2020s, time_2020s, width=bar_width, color='#2ca02c', edgecolor='grey', label='2020s')

# Add titles and labels
ax.set_title('Evolution of Leisure Time Over Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activities', fontsize=14, labelpad=15)
ax.set_ylabel('Average Time Spent (minutes per day)', fontsize=14, labelpad=15)
ax.set_xticks([r + bar_width for r in range(len(activities))])
ax.set_xticklabels(activities, rotation=45, ha='right', fontsize=12)

# Add data labels on top of each bar
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

add_labels(bars_1980s)
add_labels(bars_2000s)
add_labels(bars_2020s)

# Add a legend for context
ax.legend(title='Decades', loc='upper left', fontsize=10, title_fontsize=12)

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Layout adjustment to avoid text overlap
plt.tight_layout()

# Show the plot
plt.show()