import matplotlib.pyplot as plt
import numpy as np

# Backstory: Study of Temperature Variation Over the Course of a Year in Three Different Cities
# Cities: Springfield, Riverton, and Laketown

# Time (in months)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Temperature data (in degrees Celsius)
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
riverton_temps = np.array([0, 2, 6, 10, 15, 19, 22, 21, 16, 10, 5, 1])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature data
ax.plot(months, springfield_temps, marker='o', linestyle='-', color='b', label='Springfield')
ax.plot(months, riverton_temps, marker='o', linestyle='--', color='g', label='Riverton')
ax.plot(months, laketown_temps, marker='o', linestyle='-.', color='r', label='Laketown')

# Set titles and labels
ax.set_title('Annual Temperature Variations\nin Springfield, Riverton, and Laketown', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Add legend
ax.legend(title='Cities', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

# Annotate specific points for better emphasis
for i in range(len(months)):
    ax.annotate(f"{springfield_temps[i]}°C", (months[i], springfield_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')
    ax.annotate(f"{riverton_temps[i]}°C", (months[i], riverton_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='green')
    ax.annotate(f"{laketown_temps[i]}°C", (months[i], laketown_temps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()