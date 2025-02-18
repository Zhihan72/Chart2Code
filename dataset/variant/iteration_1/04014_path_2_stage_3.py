import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)
auto_vehicles = np.array([30, 50, 80, 120, 170, 220, 280, 350, 420, 500, 600])
hyperloop_pods = np.array([1, 5, 12, 30, 50, 80, 110, 150, 200, 270, 350])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Use a single color 'teal' across all data groups
ax1.plot(years, auto_vehicles, color='teal', marker='o', linestyle='-', linewidth=2, markersize=8)
ax1.plot(years, hyperloop_pods, color='teal', marker='^', linestyle='-', linewidth=2, markersize=8)

ax1.set_title('Technological Advancements in Sci-Fi Cities (2025-2035)', fontsize=18, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Units Deployed', fontsize=14)

ax1.annotate('First major Hyperloop system', xy=(2033, hyperloop_pods[8]), xytext=(2030, 300),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=12, color='navy')

plt.tight_layout()

plt.show()