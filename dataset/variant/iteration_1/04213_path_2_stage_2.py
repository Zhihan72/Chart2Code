import matplotlib.pyplot as plt
import numpy as np

household_types = [
    "Large Family", "Small Family", "Retirement Home", "Shared Apartment", "Single Occupant"
]
energy_consumption = [
    600, 450, 400, 350, 300
]

fig, ax = plt.subplots(figsize=(12, 8))

# Create the bar chart without stylistic elements
bars = ax.bar(household_types, energy_consumption, color=['#99ff99','#66b3ff','#c2c2f0','#ffcc99','#ff9999'], edgecolor='black', alpha=0.85)

# Annotate each bar with the consumption values
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} kWh', ha='center', va='bottom', fontsize=12)

# Title and labels
ax.set_title('Energy Consumption by Household Type\nin Energio, 2023', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Household Type', fontsize=14)
ax.set_ylabel('Average Monthly Energy Consumption (kWh)', fontsize=14)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()