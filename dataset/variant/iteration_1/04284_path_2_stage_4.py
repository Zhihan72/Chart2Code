import matplotlib.pyplot as plt
import numpy as np

technologies = ['Solar Panels', 'Fusion Power', 'Geothermal', 'Wind Turbines', 'Hydrogen Fuel Cells', 'Nuclear Fusion']
power_distribution = [25, 20, 15, 10, 10, 20]
sorted_tech = sorted(zip(technologies, power_distribution), key=lambda x: x[1], reverse=True)
sorted_technologies, sorted_power_distribution = zip(*sorted_tech)

tech_comparison = ['Solar Panels', 'Fusion Power']
efficiency = [85, 92]
sorted_efficiency = sorted(zip(tech_comparison, efficiency), key=lambda x: x[1], reverse=True)
sorted_tech_comparison, sorted_eff = zip(*sorted_efficiency)

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8))

single_color = '#4682B4'

bars1 = ax1.bar(sorted_technologies, sorted_power_distribution, color=single_color)
ax1.set_ylim(0, max(sorted_power_distribution)*1.1)
ax1.grid(True, axis='y', linestyle='--', alpha=0.5)
for bar, value in zip(bars1, sorted_power_distribution):
    ax1.text(bar.get_x() + bar.get_width() / 2, value + 1, f"{value}%", ha='center', va='bottom', fontsize=12)

bars2 = ax2.bar(sorted_tech_comparison, sorted_eff, color=single_color)
ax2.set_ylim(0, 100)
ax2.grid(True, axis='y', linestyle='--', alpha=0.5)
for bar, eff in zip(bars2, sorted_eff):
    ax2.text(bar.get_x() + bar.get_width() / 2, eff + 2, f"{eff}%", ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()