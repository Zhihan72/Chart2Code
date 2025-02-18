import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart visualizes the "Energy Usage in a Smart Home" for different appliances over a week.
# The data represents artificial energy consumption (in kWh) values for various home appliances.

# Define the days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
num_days = len(days)

# Artificial energy usage data for different appliances
heating = [20, 22, 19, 21, 20, 23, 25]
cooling = [10, 12, 9, 11, 10, 8, 7]
lighting = [3, 3, 3, 3, 4, 5, 5]
appliances = [8, 7, 6, 7, 8, 10, 11]
entertainment = [5, 4, 5, 6, 7, 8, 10]

# Stack the data to create cumulative energy usage values
energy_stack = np.row_stack((heating, cooling, lighting, appliances, entertainment))

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(days, energy_stack, labels=['Heating', 'Cooling', 'Lighting', 'Appliances', 'Entertainment'],
             colors=['#D98880', '#76D7C4', '#F7DC6F', '#A569BD', '#85C1E9'], alpha=0.8)

# Set the title and labels with line breaks and appropriate formatting
ax.set_title('Energy Usage in a Smart Home\nOver a Week', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Energy Usage (kWh)', fontsize=14)

# Add a legend outside the plot area for clarity
ax.legend(loc='upper right', fontsize=12, bbox_to_anchor=(1.15, 1))

# Customize the grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Rotate x-axis labels slightly for better fit
plt.xticks(rotation=45)

# Enhance layout for better visualization
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()