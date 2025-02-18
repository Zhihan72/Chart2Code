import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The Temperatures of Four Major Oceans
# This chart showcases the temperature distribution across four major oceans (Pacific, Atlantic, Indian, and Arctic)
# based on recorded temperatures in degrees Celsius over a given period.

# Constructing Data:
# Observed temperatures in degrees Celsius for different oceans
pacific_temps = [22, 24, 23, 23, 25, 26, 27, 24, 26, 28, 29, 30, 27, 25, 24, 28, 26, 23, 22, 29]
atlantic_temps = [20, 21, 22, 23, 22, 24, 25, 26, 23, 22, 21, 20, 22, 23, 24, 26, 27, 25, 23, 22]
indian_temps = [25, 27, 28, 29, 27, 26, 25, 24, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 26, 27]
arctic_temps = [1, 2, 3, 2, 1, 0, -1, 1, 2, 3, -1, -2, 1, 0, 2, 3, -1, 1, 2, 1]

# Combine the temperature data into a single list for the boxplot
temperature_data = [pacific_temps, atlantic_temps, indian_temps, arctic_temps]
ocean_names = ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean']

# Creating the boxplot
fig, ax = plt.subplots(figsize=(14, 8))

# Creating and customizing the boxplot
box = ax.boxplot(temperature_data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightblue', color='navy'),
                 whiskerprops=dict(color='navy', linestyle='--'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkred', linewidth=2),
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 meanline=True, showmeans=True, meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black', markersize=7))

# Customizing each box color
colors = ['#ADD8E6', '#90EE90', '#FFD700', '#FF6347']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding data points for enhanced detail
for i, data in enumerate(temperature_data):
    y = np.random.normal(i + 1, 0.04, size=len(data))
    ax.plot(data, y, 'o', alpha=0.3, color='gray')

# Adding axis labels and title
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(ocean_names)
ax.set_title('Temperature Distribution Across Major Oceans', fontsize=16, fontweight='bold', pad=20)

# Adding legend to identify mean
ax.legend([box["means"][0]], ['Mean Value'], loc='upper right', fontsize=10)

# Adding a grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Highlighting the Interquartile Range (IQR) with annotations
for i, data in enumerate(temperature_data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    IQR = q3 - q1
    ax.annotate(f'IQR = {IQR:.1f}', xy=(0.05, i + 1), xycoords=('axes fraction', 'data'),
                ha='center', va='center', fontsize=10, color='darkblue')

# Adjusting layout automatically to fit elements
plt.tight_layout()

# Displaying the plot
plt.show()