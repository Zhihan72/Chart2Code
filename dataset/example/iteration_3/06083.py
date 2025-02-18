import matplotlib.pyplot as plt
import numpy as np

# Backstory: A Comparative Study of Average Daily Temperatures in Three Cities Over a Week
# The cities are New York, Los Angeles, and Chicago, famous for their distinct climate patterns.

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Average daily temperatures for each city (in degrees Fahrenheit)
temperatures_ny = [30, 32, 35, 33, 30, 31, 29]
temperatures_la = [55, 57, 56, 58, 60, 61, 63]
temperatures_chicago = [20, 22, 25, 24, 22, 21, 19]

# Create the figure and the axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
ax.plot(days, temperatures_ny, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6, label='New York')
ax.plot(days, temperatures_la, marker='s', linestyle='--', color='green', linewidth=2, markersize=6, label='Los Angeles')
ax.plot(days, temperatures_chicago, marker='^', linestyle='-.', color='red', linewidth=2, markersize=6, label='Chicago')

# Annotating each point
for i in range(len(days)):
    ax.text(i, temperatures_ny[i] + 1, f'{temperatures_ny[i]}°F', ha='center', va='bottom', fontsize=10, color='blue')
    ax.text(i, temperatures_la[i] + 1, f'{temperatures_la[i]}°F', ha='center', va='bottom', fontsize=10, color='green')
    ax.text(i, temperatures_chicago[i] + 1, f'{temperatures_chicago[i]}°F', ha='center', va='bottom', fontsize=10, color='red')

# Titles and labels
ax.set_title('Average Daily Temperatures in a Week\nfor New York, Los Angeles, and Chicago', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Days of the Week', fontsize=14)
ax.set_ylabel('Temperature (°F)', fontsize=14)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Set x-axis tick labels
ax.set_xticks(np.arange(len(days)))
ax.set_xticklabels(days, fontsize=12, rotation=30, ha='right')

# Add legend
ax.legend(title='Cities', loc='upper left', fontsize=12, title_fontsize='13')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()