import matplotlib.pyplot as plt
import numpy as np

# Time (in months)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Temperature data (in degrees Celsius)
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
riverton_temps = np.array([0, 2, 6, 10, 15, 19, 22, 21, 16, 10, 5, 1])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature data
ax.plot(months, springfield_temps, marker='s', linestyle='-', color='c', label='Springfield-studied', linewidth=2.5)
ax.plot(months, riverton_temps, marker='^', linestyle='--', color='m', label='Riverton-detailed', linewidth=2.5)
ax.plot(months, laketown_temps, marker='d', linestyle=':', color='y', label='Laketown-examined', linewidth=2.5)

# Set titles and labels
ax.set_title('Temperature Variation over a Year', fontsize=18, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Add legend with altered position
ax.legend(title='Examined Cities', fontsize=12, loc='lower left')

# Change grid style for aesthetic
ax.grid(True, linestyle=':', which='both', color='lightgrey', alpha=0.5)

# Alter border visibility
for spine in ax.spines.values():
    spine.set_visible(False)

# Annotate specific points for better emphasis
for i in range(len(months)):
    ax.annotate(f"{springfield_temps[i]}°C", (months[i], springfield_temps[i]), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8, color='c')
    ax.annotate(f"{riverton_temps[i]}°C", (months[i], riverton_temps[i]), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8, color='m')
    ax.annotate(f"{laketown_temps[i]}°C", (months[i], laketown_temps[i]), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8, color='y')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()