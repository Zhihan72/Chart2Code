import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart illustrates the evolution of renewable energy storage technologies in the fictional city of GreenValley over the span of 20 years.

# Define the years from 2020 to 2040
years = np.arange(2020, 2041)

# Data for different storage technologies (in megawatt-hours)
batteries = np.array([50, 75, 110, 150, 180, 210, 260, 300, 350, 400, 450, 520, 580, 650, 720, 800, 870, 950, 1050, 1150, 1250])
hydropumped = np.array([20, 22, 24, 26, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])
thermal = np.array([10, 15, 20, 28, 35, 45, 60, 75, 90, 105, 120, 135, 150, 170, 190, 210, 230, 250, 270, 290, 310])
flywheels = np.array([5, 7, 10, 13, 18, 25, 35, 48, 60, 75, 90, 110, 130, 150, 175, 200, 225, 250, 280, 310, 340])

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, batteries, hydropumped, thermal, flywheels,
             labels=['Batteries', 'Hydro-Pumped Storage', 'Thermal Storage', 'Flywheels'],
             colors=['#4C9F70', '#34495E', '#F39C12', '#8E44AD'], alpha=0.8)

# Set the title and labels, with line breaks in the title for clarity
ax.set_title('GreenValley Renewable Energy Storage Evolution (2020-2040)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Capacity (MWh)', fontsize=14)

# Add a legend to the plot
ax.legend(loc='upper left', title='Storage Technologies', fontsize=12)

# Enable grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate significant growth points
ax.annotate('Batteries surpass 500 MWh', xy=(2030, 520), xytext=(2025, 900),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Automatically adjust layout to prevent text overlap and clipping
plt.tight_layout()

# Display the plot
plt.show()