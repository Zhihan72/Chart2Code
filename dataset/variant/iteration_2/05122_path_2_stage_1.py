import matplotlib.pyplot as plt
import numpy as np

# Cities in Rainfall Land
cities = ['Oceanview', 'Mountain Peak', 'Sunnyvale', 'Lake Town', 'Desert Hues']

# Average monthly rainfall data (in mm) for each city (January to December)
rainfall_data = [
    [85, 78, 92, 110, 125, 140, 155, 145, 130, 115, 100, 90],  # Oceanview
    [95, 88, 102, 120, 135, 150, 165, 155, 140, 125, 110, 100],  # Mountain Peak
    [45, 40, 52, 60, 75, 80, 85, 75, 65, 55, 50, 45],  # Sunnyvale
    [75, 68, 82, 90, 105, 120, 135, 125, 110, 95, 80, 70],  # Lake Town
    [15, 10, 22, 30, 35, 40, 45, 35, 25, 20, 15, 10],  # Desert Hues
]

# Months of the year
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Convert data to NumPy array for convenience
rainfall_data = np.array(rainfall_data)

# Setting up the subplot figure with 1 row and 2 columns
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Bar plot for each city's average monthly rainfall
bar_width = 0.15
x = np.arange(len(months))

for i, city in enumerate(cities):
    bars = axs[0].bar(x + i * bar_width, rainfall_data[i], bar_width, label=city)
    for bar in bars:
        axs[0].annotate(f'{bar.get_height()}',
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom', fontsize=9)

# Setting labels, title, and legend for the bar plot
axs[0].set_xlabel('Months', fontsize=12)
axs[0].set_ylabel('Average Monthly Rainfall (mm)', fontsize=12)
axs[0].set_title('Rainfall Land: Average Monthly Rainfall by City (2023)', fontsize=14, fontweight='bold')
axs[0].set_xticks(x + bar_width * (len(cities) / 2 - 0.5))
axs[0].set_xticklabels(months, fontsize=10)
axs[0].legend(title='City', fontsize=10)
axs[0].yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Line plot for yearly rainfall trend over months for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
markers = ['o', 's', 'D', '^', 'v']

for i, city in enumerate(cities):
    axs[1].plot(months, rainfall_data[i], marker=markers[i], color=colors[i], label=city)

# Adding labels, title, and legend for the line plot
axs[1].set_xlabel('Months', fontsize=12)
axs[1].set_ylabel('Average Monthly Rainfall (mm)', fontsize=12)
axs[1].set_title('Yearly Rainfall Trend by City (2023)', fontsize=14, fontweight='bold')
axs[1].legend(title='City', fontsize=10)
axs[1].yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Ensure the layout fits well and display the plot
plt.tight_layout()
plt.show()