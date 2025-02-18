import matplotlib.pyplot as plt
import numpy as np

household_types = [
    "Shared Apartment", "Large Family", "Single Occupant", "Small Family", "Retirement Home"
]
energy_consumption = [
    350, 600, 300, 450, 400
]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.bar(household_types, energy_consumption, color=['#ffcc99','#99ff99','#ff9999','#66b3ff','#c2c2f0'], edgecolor='black', alpha=0.85)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} kWh', ha='center', va='bottom', fontsize=12)

ax.set_title('Energy Consumption by Household Type\nin Energio, 2023', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Household Type', fontsize=14)
ax.set_ylabel('Average Monthly Energy Consumption (kWh)', fontsize=14)

plt.tight_layout()

plt.show()