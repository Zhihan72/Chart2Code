import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The fictional city of Energio conducted a survey on energy consumption by household types for the year 2023.
# The results show diverse consumption behaviors among different types of households.

# Data: Average monthly energy consumption (in kWh) by household type
household_types = [
    "Single Occupant", "Small Family", "Large Family", "Shared Apartment", "Retirement Home"
]
energy_consumption = [
    300, 450, 600, 350, 400
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create the bar chart
bars = ax.bar(household_types, energy_consumption, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'], edgecolor='black', alpha=0.85)

# Annotate each bar with the consumption values
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} kWh', ha='center', va='bottom', fontsize=12)

# Add a horizontal line for the city average energy consumption
city_average = np.mean(energy_consumption)
ax.axhline(city_average, color='red', linestyle='--', linewidth=1.5, label=f'City Avg: {city_average:.1f} kWh')

# Title and labels
ax.set_title('Energy Consumption by Household Type\nin Energio, 2023', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Household Type', fontsize=14)
ax.set_ylabel('Average Monthly Energy Consumption (kWh)', fontsize=14)
ax.legend()

# Customize grid and tick parameters for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()