import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart details the monthly average temperature variations for three major cities over a year, 
# reflecting how these cities experience the seasons differently across the months. 
# The cities included in this study are New York, Los Angeles, and Chicago.

# Data preparation: Monthly average temperatures (in °C) for the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
new_york_temps = np.array([-1, 0, 6, 13, 18, 23, 26, 25, 21, 14, 8, 2])
los_angeles_temps = np.array([14, 15, 16, 18, 19, 21, 24, 24, 23, 20, 17, 14])
chicago_temps = np.array([-5, -2, 4, 11, 17, 22, 25, 24, 20, 13, 6, -1])

# Creating the plot with subplots
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the data for each city with different styles
ax.plot(months, new_york_temps, marker='o', linestyle='-', color='tab:blue', label='New York')
ax.plot(months, los_angeles_temps, marker='^', linestyle='--', color='tab:orange', label='Los Angeles')
ax.plot(months, chicago_temps, marker='s', linestyle='-.', color='tab:green', label='Chicago')

# Adding titles and labels
ax.set_title("Monthly Average Temperature Variations\nAcross Three Major Cities in 2023", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Average Temperature (°C)", fontsize=12)

# Customizing the legend
ax.legend(loc='upper right', fontsize=10, title='Cities', title_fontsize='12')

# Enhancing grid and background
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f9f9f9')

# Adding annotations for the highest and lowest points for each city
highlight_style = dict(size=10, color='b', weight='bold')
ax.annotate('Highest', xy=(6, 26), xytext=(7, 27),
            arrowprops=dict(facecolor='blue', shrink=0.1), **highlight_style)
ax.annotate('Lowest', xy=(0, -1), xytext=(1, -6),
            arrowprops=dict(facecolor='blue', shrink=0.1), **highlight_style)
ax.annotate('Highest', xy=(5, 24), xytext=(6, 25),
            arrowprops=dict(facecolor='orange', shrink=0.1), **highlight_style)
ax.annotate('Lowest', xy=(0, 14), xytext=(1, 10),
            arrowprops=dict(facecolor='orange', shrink=0.1), **highlight_style)
ax.annotate('Highest', xy=(6, 25), xytext=(7, 26),
            arrowprops=dict(facecolor='green', shrink=0.1), **highlight_style)
ax.annotate('Lowest', xy=(0, -5), xytext=(1, -10),
            arrowprops=dict(facecolor='green', shrink=0.1), **highlight_style)

# Adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()