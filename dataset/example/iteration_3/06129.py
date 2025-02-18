import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking Energy Consumption and Savings in a Smart Home
# This chart will visualize the energy consumption and savings over a year for different 
# categories in a smart home: Heating, Cooling, Lighting, and Appliances.

# Create data for 12 months
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Energy consumption (in kWh) for each category over the year
heating = np.array([350, 310, 280, 220, 180, 140, 130, 140, 200, 270, 310, 340])
cooling = np.array([50, 60, 100, 200, 300, 370, 400, 380, 290, 170, 80, 60])
lighting = np.array([100, 90, 80, 90, 100, 110, 120, 110, 100, 90, 80, 100])
appliances = np.array([120, 110, 105, 115, 120, 125, 130, 128, 122, 115, 108, 112])

# Calculate the overall consumption and savings
overall_consumption = heating + cooling + lighting + appliances
monthly_savings = 0.1 * overall_consumption  # Assuming 10% savings each month

# Setup the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data
ax.plot(months, heating, marker='o', linestyle='-', color='r', linewidth=2, label='Heating')
ax.plot(months, cooling, marker='s', linestyle='--', color='b', linewidth=2, label='Cooling')
ax.plot(months, lighting, marker='^', linestyle='-.', color='g', linewidth=2, label='Lighting')
ax.plot(months, appliances, marker='d', linestyle=':', color='m', linewidth=2, label='Appliances')
ax.plot(months, monthly_savings, marker='*', linestyle='-', color='c', linewidth=2, label='Savings')

# Annotations for highlighting significant data points
annotations = [
    ('Jan', heating[0], 'Start of year,\nhigh heating demand'),
    ('Jul', cooling[6], 'Peak cooling usage'),
    ('Dec', lighting[11], 'Increased lighting\nrequirement')
]
for (month, value, text) in annotations:
    ax.annotate(text, xy=(month, value), xytext=(5, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

# Title and labels
ax.set_title('Monthly Energy Consumption and Savings in a Smart Home', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Energy (kWh)', fontsize=12)

# Add a legend
ax.legend(title='Energy Categories', loc='upper left', fontsize=10)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()