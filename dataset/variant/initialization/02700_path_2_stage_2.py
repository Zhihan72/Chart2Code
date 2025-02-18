import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

region_data = {
    'Solar': np.array([20, 22, 25, 30, 35, 40, 45, 50, 60, 70, 80, 95, 110, 125, 140, 160, 180, 200, 220, 240, 260]),
    'Wind': np.array([10, 12, 15, 18, 22, 28, 35, 40, 50, 65, 80, 90, 100, 110, 125, 140, 155, 170, 185, 200, 220]),
    'Hydro': np.array([50, 52, 54, 55, 58, 60, 65, 70, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140]),
    'Geothermal': np.array([5, 5, 6, 7, 8, 10, 12, 15, 18, 22, 28, 35, 38, 42, 45, 50, 55, 60, 65, 70, 75]),
    'Biomass': np.array([15, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 68, 72, 78, 80, 85, 90, 95, 100])
}

total_energy = sum(region_data.values())

fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Manually shuffled the colors assigned to each category
axes[0].stackplot(years, region_data.values(),
                  colors=['#87CEEB', '#8B4513', '#FFD700', '#32CD32', '#FF6347'], alpha=0.8)
axes[0].set_title('Renewable Energy Adoption Over Time\n(Imaginary Regions, 2000-2020)', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Energy Consumption\n(Hypothetical Units)', fontsize=12)

axes[1].plot(years, total_energy, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)
axes[1].set_title('Total Energy Consumption Over Time', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Total Energy Consumption\n(Hypothetical Units)', fontsize=12)

plt.tight_layout()
plt.show()