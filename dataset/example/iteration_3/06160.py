import matplotlib.pyplot as plt
import numpy as np

# Imagine we are tracking the temperature change in a hypothetical city over a year. 
# To emphasize the impact of seasons, we'll plot the average monthly temperature over three years: 2021, 2022, and 2023.

# Creating a backstory:
# The city of Climata, nestled in a valley, experiences significant seasonal variations,
# with temperatures showing notable trends as climate patterns exhibit year-to-year shifts.

# Monthly data for three years (in degrees Celsius)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temps_2021 = np.array([3, 5, 9, 14, 18, 22, 25, 24, 20, 14, 8, 4])
temps_2022 = np.array([2, 4, 8, 13, 17, 21, 24, 23, 19, 13, 7, 3])
temps_2023 = np.array([1, 3, 7, 12, 16, 20, 23, 22, 18, 12, 6, 2])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the temperature trends over the years
ax.plot(months, temps_2021, marker='o', linestyle='-', color='r', linewidth=2, label='2021')
ax.plot(months, temps_2022, marker='s', linestyle='--', color='g', linewidth=2, label='2022')
ax.plot(months, temps_2023, marker='d', linestyle='-.', color='b', linewidth=2, label='2023')

# Set titles and labels
ax.set_title('Monthly Temperature Trends in Climata (2021-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
ax.legend(loc='best', fontsize=11, title='Year')

# Add grid lines for better readability
ax.grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Add annotations to highlight temperature peaks for each year
annotate_points = [
    ('Peak Summer 2021', 'Jul', 25, 'top'),
    ('Peak Summer 2022', 'Jul', 24, 'top'),
    ('Peak Summer 2023', 'Jul', 23, 'top'),
]

for note, x_loc, y_loc, align in annotate_points:
    ax.annotate(
        note, 
        xy=(x_loc, y_loc), 
        xytext=(0, 10 if align == 'top' else -10),
        textcoords='offset points',
        ha='center',
        fontsize=10, 
        color='darkred',
        arrowprops=dict(facecolor='darkred', arrowstyle='->')
    )

# Annotate each data point with its temperature
for i, txt in enumerate(temps_2021):
    ax.annotate(f'{txt}°C', (months[i], temps_2021[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color='red')
for i, txt in enumerate(temps_2022):
    ax.annotate(f'{txt}°C', (months[i], temps_2022[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color='green')
for i, txt in enumerate(temps_2023):
    ax.annotate(f'{txt}°C', (months[i], temps_2023[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color='blue')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()