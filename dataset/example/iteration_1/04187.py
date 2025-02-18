import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# The chart depicts the Evolution of Screen Time Distribution in Different Age Groups Over the Decades.
# The overall screen time increases dramatically from the 1980s to 2020s due to the advent of new technology and social media.

# Define decades and age group categories
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
age_groups = ['0-12', '13-18', '19-35', '36-55', '56+']

# Screen time (hours per week) for each age group over the decades
screen_time_0_12 = [5, 8, 12, 18, 25]
screen_time_13_18 = [8, 12, 20, 35, 45]
screen_time_19_35 = [10, 15, 25, 40, 50]
screen_time_36_55 = [8, 10, 15, 25, 30]
screen_time_56_plus = [5, 7, 10, 15, 20]

# Stack the data
data = np.array([screen_time_0_12, screen_time_13_18, screen_time_19_35, screen_time_36_55, screen_time_56_plus])

# Define colors for each age group
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(decades, data, labels=age_groups, colors=colors, alpha=0.8)

# Add axis labels and title
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Screen Time (hours per week)', fontsize=12)
plt.title('Evolution of Screen Time Across Age Groups Over Decades', fontsize=16, fontweight='bold', pad=20)

# Add a legend to identify the layers
plt.legend(title='Age Groups', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Rotate x-tick labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()