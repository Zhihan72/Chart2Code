import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A coastal town called "Wave Harbor" tracks the seasonal beach lifeguard rescues over five years. Each rescue is categorized by type:
# - Swimmer Assist
# - Minor Injuries
# - Major Injuries
# - Rescues in Rough Seas
# - Crowd Control

# Define the years of data collection
years = np.arange(2018, 2023)

# Manually constructed data representing the number of each rescue type
swimmer_assist = np.array([50, 45, 60, 55, 65])
minor_injuries = np.array([20, 25, 15, 18, 22])
major_injuries = np.array([5, 4, 6, 7, 6])
rough_seas = np.array([15, 13, 18, 20, 17])
crowd_control = np.array([10, 9, 14, 13, 11])

# Stack the data for plotting
rescue_data = np.vstack([swimmer_assist, minor_injuries, major_injuries, rough_seas, crowd_control])

# Plot the area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, rescue_data, labels=['Swimmer Assist', 'Minor Injuries', 'Major Injuries', 
                                         'Rescues in Rough Seas', 'Crowd Control'], 
             colors=['#1E90FF', '#32CD32', '#FFA500', '#B22222', '#9370DB'], alpha=0.75)

# Customize the chart with title and labels
ax.set_title('Seasonal Beach Lifeguard Rescues in Wave Harbor (2018-2022)', fontsize=16, weight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12, weight='bold')
ax.set_ylabel('Number of Rescues', fontsize=12, weight='bold')

# Highlight specific years or events with vertical lines
highlight_years = [2020]
for year in highlight_years:
    ax.axvline(x=year, color='black', linestyle='--', linewidth=1)

# Annotate significant points or trends
ax.annotate('Increment in Rough Seas Rescues\npossibly due to weather patterns', xy=(2020, 105), xytext=(2018.5, 130),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Adding grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Rotate x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Position the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Rescue Types', fontsize=11, shadow=True)

# Add data points markers for clarity
for y, color in zip(rescue_data, ['#1E90FF', '#32CD32', '#FFA500', '#B22222', '#9370DB']):
    ax.plot(years, y, marker='o', markersize=6, color=color, linestyle='None', alpha=0.9)

# Tight layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()