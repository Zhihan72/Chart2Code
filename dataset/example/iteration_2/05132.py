import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the average temperatures of five cities over a year
# Cities: "San Francisco", "New York", "Tokyo", "Paris", "Sydney"
# Topic: Monthly average temperatures for the year 2022

# Months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Temperatures in Celsius
san_francisco_temps = np.array([11, 12, 13, 14, 16, 17, 18, 18, 17, 15, 12, 11])
new_york_temps = np.array([0, 2, 7, 13, 18, 24, 27, 26, 22, 16, 10, 4])
tokyo_temps = np.array([5, 6, 10, 15, 19, 22, 26, 27, 24, 19, 14, 9])
paris_temps = np.array([5, 6, 9, 12, 16, 19, 22, 21, 18, 14, 9, 6])
sydney_temps = np.array([23, 23, 22, 19, 16, 14, 13, 14, 16, 18, 20, 22])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each city's data
ax.plot(months, san_francisco_temps, label='San Francisco', color='tab:blue', marker='o', linestyle='-')
ax.plot(months, new_york_temps, label='New York', color='tab:orange', marker='o', linestyle='-')
ax.plot(months, tokyo_temps, label='Tokyo', color='tab:green', marker='o', linestyle='-')
ax.plot(months, paris_temps, label='Paris', color='tab:red', marker='o', linestyle='-')
ax.plot(months, sydney_temps, label='Sydney', color='tab:purple', marker='o', linestyle='-')

# Title and labels
ax.set_title('Average Monthly Temperatures for Five Major Cities in 2022', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Add a legend
ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper right')

# Customize grid
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate specific points for clarity
for (month, temp_san_francisco) in zip(months, san_francisco_temps):
    if temp_san_francisco in [11, 18]:
        ax.annotate(f'{temp_san_francisco}°C', xy=(month, temp_san_francisco), xytext=(5, -15), 
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()