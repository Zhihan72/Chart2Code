import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking temperature changes across different US cities over one year

# Define the months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Construct temperature data for different cities (in Fahrenheit)
new_york = np.array([30, 32, 45, 55, 65, 75, 80, 78, 70, 60, 50, 35])
los_angeles = np.array([55, 58, 60, 65, 70, 75, 80, 82, 78, 70, 62, 58])
chicago = np.array([25, 28, 40, 50, 60, 70, 75, 73, 65, 55, 45, 30])
houston = np.array([50, 55, 60, 70, 80, 85, 90, 92, 85, 75, 65, 55])

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data for each city
ax.plot(months, new_york, marker='o', linestyle='-', markersize=6, linewidth=2, label='New York', color='blue')
ax.plot(months, los_angeles, marker='s', linestyle='--', markersize=6, linewidth=2, label='Los Angeles', color='orange')
ax.plot(months, chicago, marker='^', linestyle='-', markersize=6, linewidth=2, label='Chicago', color='green')
ax.plot(months, houston, marker='D', linestyle=':', markersize=6, linewidth=2, label='Houston', color='red')

# Set the title, labels, and legend with appropriate customization
ax.set_title("Temperature Trends in Major US Cities Over One Year", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°F)', fontsize=14)
ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper left')

# Enhance the grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Set ticks and their font size for better readability
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Annotate specific points
annotations = {
    'New York': [0, 3],   # coldest, warmest months (indices)
    'Los Angeles': [0, 7],
    'Chicago': [0, 6],
    'Houston': [0, 7]
}

for city, data in zip(['New York', 'Los Angeles', 'Chicago', 'Houston'], [new_york, los_angeles, chicago, houston]):
    for idx in annotations[city]:
        ax.annotate(f"{data[idx]}°F", 
                    (months[idx], data[idx]), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    arrowprops=dict(arrowstyle='->', linestyle='-', color='black'))

# Enable tight layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()