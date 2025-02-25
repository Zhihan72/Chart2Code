import matplotlib.pyplot as plt
import numpy as np

# Months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Randomly altered temperatures in Celsius for plot variation
san_francisco_temps = np.array([18, 13, 17, 11, 16, 14, 12, 18, 15, 12, 17, 11])
new_york_temps = np.array([10, 27, 4, 0, 24, 13, 2, 22, 18, 7, 16, 26])
tokyo_temps = np.array([19, 26, 15, 14, 22, 27, 10, 6, 9, 5, 24, 19])
paris_temps = np.array([22, 5, 12, 9, 16, 21, 14, 19, 9, 18, 6, 6])
sydney_temps = np.array([14, 23, 22, 19, 20, 16, 18, 13, 14, 16, 23, 22])

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
    if temp_san_francisco in [14, 22]:
        ax.annotate(f'{temp_san_francisco}°C', xy=(month, temp_san_francisco), xytext=(5, -15), 
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()