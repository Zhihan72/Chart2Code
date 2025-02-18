import matplotlib.pyplot as plt
import numpy as np

household_types = ["Single", "Small F.", "Large F.", "Shared Apt."]
energy_consumption = [300, 450, 600, 350]

sorted_indices = np.argsort(energy_consumption)
household_types_sorted = [household_types[i] for i in sorted_indices]
energy_consumption_sorted = [energy_consumption[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.bar(household_types_sorted, energy_consumption_sorted, color=['#f28e2b', '#76b7b2', '#59a14f', '#edc948'], edgecolor='black', alpha=0.85)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} kWh', ha='center', va='bottom', fontsize=12)

city_average = np.mean(energy_consumption_sorted)
ax.axhline(city_average, color='red', linestyle='--', linewidth=1.5)

ax.set_title('Energy Usage by Household\nin Energio, 2023', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Household', fontsize=14)
ax.set_ylabel('Avg Monthly Energy (kWh)', fontsize=14)

ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

plt.tight_layout()
plt.show()