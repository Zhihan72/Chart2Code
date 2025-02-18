import matplotlib.pyplot as plt
import numpy as np

# Time (in months)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Temperature data (in degrees Celsius) for Springfield and Laketown
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature data
ax.plot(months, springfield_temps, marker='o', linestyle='-', color='b', label='Springfield')
ax.plot(months, laketown_temps, marker='o', linestyle='-.', color='r', label='Laketown')

# Set titles and labels
ax.set_title('Annual Temperature Variations\nin Springfield and Laketown', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Add legend
ax.legend(title='Cities', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

# Annotate specific points for better emphasis
for i in range(len(months)):
    ax.annotate(f"{springfield_temps[i]}°C", (months[i], springfield_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')
    ax.annotate(f"{laketown_temps[i]}°C", (months[i], laketown_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()