import numpy as np
import matplotlib.pyplot as plt

# Define the categories of the radar chart
categories = ['Temperature', 'Humidity', 'Visibility', 'Air Quality', 'Traffic']

# Define the data for each mode of transportation
bike = [8, 5, 7, 6, 8]
bus = [7, 6, 5, 7, 5]
car = [9, 4, 8, 5, 9]

# Title and backstory:
# This radar chart compares the daily commuting conditions for different modes of transportation in a metropolitan area. Each mode is evaluated based on Temperature, Humidity, Visibility, Air Quality, and Traffic.

# Number of variables we're plotting
num_vars = len(categories)

# Compute angle for each axis and close the radar chart loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
bike += bike[:1]
bus += bus[:1]
car += car[:1]
angles += angles[:1]

# Start the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each commuting mode's data on the radar chart
ax.fill(angles, bike, color='blue', alpha=0.25, label='Bike')
ax.fill(angles, bus, color='green', alpha=0.25, label='Bus')
ax.fill(angles, car, color='red', alpha=0.25, label='Car')

# Connect the data points with lines
ax.plot(angles, bike, color='blue', linewidth=2)
ax.plot(angles, bus, color='green', linewidth=2)
ax.plot(angles, car, color='red', linewidth=2)

# Remove radial labels for a cleaner look
ax.set_yticklabels([])

# Define and style category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, ha='center')

# Add a descriptive title
plt.title('Commuting Conditions Analysis\nAcross Different Modes of Transportation', size=15, y=1.1)

# Add a legend to clarify which color represents which mode of transportation
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the radar chart
plt.show()