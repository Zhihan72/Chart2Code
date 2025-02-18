import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

region_data = {
    'Sunny': np.array([45, 50, 60, 65, 35, 40, 20, 22, 25, 30, 125, 140, 160, 70, 280, 200, 180, 95, 110, 240, 260]),
    'Breezy': np.array([35, 40, 22, 28, 10, 12, 15, 18, 80, 65, 100, 110, 125, 140, 90, 55, 80, 170, 185, 200, 220]),
    'Rivers': np.array([85, 52, 54, 55, 130, 60, 90, 65, 50, 70, 80, 95, 100, 105, 110, 115, 120, 125, 58, 135, 140]),
    'Earth Heat': np.array([7, 5, 6, 75, 60, 10, 8, 15, 18, 22, 28, 35, 38, 5, 50, 55, 12, 60, 65, 42, 70]),
    'Forest': np.array([68, 72, 100, 90, 15, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 78, 80, 85, 95])
}

total_energy = sum(region_data.values())

plt.figure(figsize=(9, 8))
plt.plot(years, total_energy, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)
plt.title('Sum of Energy Use Over Time', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Time (Years)', fontsize=12)
plt.ylabel('Sum Energy Use\n(Mock Units)', fontsize=12)

plt.tight_layout()
plt.show()