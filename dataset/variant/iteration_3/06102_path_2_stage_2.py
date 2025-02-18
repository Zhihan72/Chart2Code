import matplotlib.pyplot as plt
import numpy as np

# Define months for the data
months = np.arange(1, 13)

# Data for average daily temperatures in degrees Celsius
city_a_temps = [5, 7, 10, 15, 20, 25, 28, 27, 23, 17, 10, 6]
city_c_temps = [12, 12, 15, 18, 22, 25, 30, 31, 28, 24, 20, 15]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the line chart for each city
ax.plot(months, city_a_temps, marker='o', linestyle='-', color='teal', linewidth=2, label='City A')
ax.plot(months, city_c_temps, marker='^', linestyle='-', color='orange', linewidth=2, label='City C')

# Setting title and labels
ax.set_title('Yearly Temperature Trends in Fictional Cities', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Daily Temperature (°C)', fontsize=12)

# Adding a legend to identify cities
ax.legend(loc='upper right', fontsize=10, title='Cities', title_fontsize=12)

# Enable grid for easier value estimation
ax.grid(True, linestyle='--', alpha=0.7)

# Annotating key seasonal points in the data
ax.annotate('Winter Start', xy=(12, 6), xytext=(10, -5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkblue')

# Set x-ticks to month names for readability
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(months, month_names, fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()