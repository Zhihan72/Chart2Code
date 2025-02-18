import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are plotting the temperature variation in three different cities over a year, 
# focusing particularly on seasonal changes.

# Data for the chart
months = np.arange(1, 13)
city1_temps = [-1, 0, 4, 10, 16, 20, 22, 21, 17, 10, 5, 1]  # Temperatures in City A in Celsius
city2_temps = [8, 9, 12, 16, 20, 24, 27, 27, 23, 18, 12, 9]  # Temperatures in City B in Celsius
city3_temps = [12, 13, 15, 19, 22, 25, 28, 28, 26, 20, 15, 13]  # Temperatures in City C in Celsius

# Create the line plot
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city1_temps, marker='o', linestyle='-', color='darkblue', linewidth=2, 
        label='City A', alpha=0.9)
ax.plot(months, city2_temps, marker='s', linestyle='--', color='darkgreen', linewidth=2, 
        label='City B', alpha=0.8)
ax.plot(months, city3_temps, marker='^', linestyle='-.', color='darkred', linewidth=2, 
        label='City C', alpha=0.7)

# Annotations for significant points
for i, temp in enumerate(city1_temps):
    if i % 3 == 0:  # Annotate every third month for City A
        ax.annotate(f'{temp}°C', (months[i], temp), textcoords="offset points", xytext=(0, 10),
                    ha='center', fontsize=10, color='darkblue')
        
for i, temp in enumerate(city2_temps):
    if i % 3 == 0:  # Annotate every third month for City B
        ax.annotate(f'{temp}°C', (months[i], temp), textcoords="offset points", xytext=(0, -15),
                    ha='center', fontsize=10, color='darkgreen')
        
for i, temp in enumerate(city3_temps):
    if i % 3 == 0:  # Annotate every third month for City C
        ax.annotate(f'{temp}°C', (months[i], temp), textcoords="offset points", xytext=(0, 10),
                    ha='center', fontsize=10, color='darkred')

# Title and labels with clear information
plt.title('Seasonal Temperature Variations in Three Cities Over a Year', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Customize x-ticks to represent months
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Add grid for readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend to identify each city's data
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()