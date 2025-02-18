import matplotlib.pyplot as plt
import numpy as np

# Fictional data for monthly average temperature (degrees Celsius) in four cities over a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# City names
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']

# Average monthly temperatures for each city
temp_data = np.array([
    [3, 5, 10, 15, 21, 26, 30, 29, 24, 18, 11, 6],   # New York
    [15, 16, 17, 18, 20, 22, 24, 24, 23, 20, 17, 15], # Los Angeles
    [-1, 1, 5, 11, 17, 23, 27, 26, 21, 14, 7, 2],     # Chicago
    [12, 14, 19, 23, 27, 30, 32, 32, 29, 24, 18, 13]  # Houston
])

# Set up figure and grid layout
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Choose bar width and positions
bar_width = 0.2
x_positions = np.arange(len(months))

# Colors for each city
colors = ['skyblue', 'lightgreen', 'coral', 'gold']

# Plot the data for each city
for i, city in enumerate(cities):
    ax1.bar(x_positions + i * bar_width, temp_data[i], width=bar_width, label=city, color=colors[i])

# Title and labels for the bar chart
ax1.set_title('Average Monthly Temperatures in Four Major Cities (°C)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14)

# Set position and label for x-axis
ax1.set_xticks(x_positions + bar_width * 1.5)
ax1.set_xticklabels(months, fontsize=12)

# Add temperature labels above bars
for i in range(len(months)):
    for j in range(len(cities)):
        ax1.text(i + j * bar_width, temp_data[j][i] + 0.5, str(temp_data[j][i]), ha='center', va='bottom', fontsize=10)

# Add a legend to the bar chart
ax1.legend(title='Cities', fontsize=12)

# Make grid lines more visible
ax1.grid(True, linestyle='--', alpha=0.7, axis='y')

# Create a subplot for plotting temperature variability
variances = np.var(temp_data, axis=1)
ax2.barh(cities, variances, color=colors, edgecolor='black')

# Title and labels for the horizontal bar chart (variability)
ax2.set_title('Temperature Variability Over the Year by City', fontsize=14, fontweight='bold')
ax2.set_xlabel('Temperature Variability (°C²)', fontsize=12)
ax2.set_ylabel('Cities', fontsize=12)

# Add value labels for horizontal bars
for i in range(len(cities)):
    ax2.text(variances[i] + 0.1, i, f'{variances[i]:.2f}', va='center', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()