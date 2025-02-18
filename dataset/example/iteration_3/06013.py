import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory: The chart illustrates the moon's temperature variations at different Apollo landing sites.
# Apollo missions landed at several distinct locations on the moon, each with unique temperature data recorded during the missions.
# Temperatures are shown for daytime high and nighttime low.

# Data Construction
missions = ['Apollo 11', 'Apollo 12', 'Apollo 14', 'Apollo 15', 'Apollo 16', 'Apollo 17']
daytime_highs = np.array([127, 123, 130, 125, 127, 128])  # in degree Celsius
nighttime_lows = np.array([-153, -155, -150, -157, -155, -156])  # in degree Celsius

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Bar Width
width = 0.4

# Scatter plot of Highs and Lows
x_pos = np.arange(len(missions))  # the label locations

# Plotting the daytime high temperatures
bars_day = ax.bar(x_pos - width/2, daytime_highs, width, label='Daytime Highs', color='orange', edgecolor='black')
# Plotting the nighttime low temperatures
bars_night = ax.bar(x_pos + width/2, nighttime_lows, width, label='Nighttime Lows', color='blue', edgecolor='black')

# Labeling the chart
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_title('Lunar Temperature Variations at Apollo Landing Sites', fontsize=16, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(missions, fontsize=10)
ax.legend()

# Adding the data labels
def add_bar_labels(bars, color='black'):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}°C', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', color=color, fontsize=10, fontweight='bold')

add_bar_labels(bars_day)
add_bar_labels(bars_night, color='white')  # White color for visibility on blue bars

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjusting layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()