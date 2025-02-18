import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solaria_energy = [20, 35, 25, 70, 55, 100, 45, 85, 135, 120, 150]
windlandia_energy = [30, 15, 65, 80, 50, 95, 110, 150, 130, 170, 200]
hydrovia_energy = [60, 50, 55, 63, 54, 68, 52, 65, 70, 75, 78]
geothermalia_energy = [14, 5, 19, 25, 10, 32, 7, 40, 49, 59, 70]
biomassia_energy = [22, 15, 10, 40, 30, 65, 50, 80, 100, 125, 150]

energy_sources = np.array([solaria_energy, windlandia_energy, hydrovia_energy, geothermalia_energy, biomassia_energy])
total_energy_per_year = energy_sources.sum(axis=0)
percentage_contributions = (energy_sources / total_energy_per_year) * 100

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

axes[0].plot(years, percentage_contributions[0], color='steelblue', linestyle='--', marker='o', linewidth=1.5)
axes[0].plot(years, percentage_contributions[1], color='steelblue', linestyle='--', marker='o', linewidth=1.5)
axes[0].plot(years, percentage_contributions[2], color='steelblue', linestyle='--', marker='o', linewidth=1.5)
axes[0].plot(years, percentage_contributions[3], color='steelblue', linestyle='--', marker='o', linewidth=1.5)
axes[0].plot(years, percentage_contributions[4], color='steelblue', linestyle='--', marker='o', linewidth=1.5)
axes[0].set_title("Source Shares Out of Total Energy (2020-2030)", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Timeline", fontsize=12)
axes[0].set_ylabel("Share (%)", fontsize=12)

axes[1].stackplot(years, energy_sources, colors=['steelblue', 'steelblue', 'steelblue', 'steelblue', 'steelblue'], alpha=0.8)
axes[1].set_title("Energy Output in Mixed Regions (2020-2030)", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Timeline", fontsize=12)
axes[1].set_ylabel("Produced Energy (GWh)", fontsize=12)

plt.tight_layout()
plt.show()