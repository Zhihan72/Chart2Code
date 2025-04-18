import matplotlib.pyplot as plt
import numpy as np

# Data Setup
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
bike_rentals = np.array([12, 15, 18, 22, 25, 30, 35, 33, 28, 24, 20, 18])
scooter_rentals = np.array([7, 9, 11, 15, 18, 28, 34, 31, 24, 19, 17, 13])  # New data series

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the lines for Bike Rentals and Scooter Rentals
ax.plot(months, bike_rentals, marker='o', linestyle='-', color='darkgreen', linewidth=2, label='Bike Rentals')
ax.plot(months, scooter_rentals, marker='s', linestyle='--', color='darkblue', linewidth=2, label='Scooter Rentals')  # New line plot

# Annotate significant events for Bike Rentals
annotations_bikes = {
    'Mar': ('Spring Promo', 18),
    'Jun': ('Bike Fest', 30),
    'Sep': ('Back to School', 28),
}

for month, (text, value) in annotations_bikes.items():
    ax.annotate(
        text,
        xy=(month, value),
        xytext=(0, 10),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='darkgreen'),
        fontsize=10,
        color='darkgreen'
    )

# Titles and labels
ax.set_title('Cycle City: Urban Transportation Trends\nin Greenford - 2022', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Rentals (in thousands)', fontsize=12)

# Set y-axis limits and enable grid
ax.set_ylim(0, 40)
ax.grid(True, linestyle='--', alpha=0.5)

# Customize x-ticks to ensure space and readability
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, fontsize=10)

# Display the legend
ax.legend(loc='upper left', fontsize=10)

# Adjust the layout for clarity
plt.tight_layout()

# Show the plot
plt.show()