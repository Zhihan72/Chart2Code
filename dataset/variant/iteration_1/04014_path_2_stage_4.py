import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)
auto_vehicles = np.array([30, 50, 80, 120, 170, 220, 280, 350, 420, 500, 600])
hyperloop_pods = np.array([1, 5, 12, 30, 50, 80, 110, 150, 200, 270, 350])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, auto_vehicles, color='teal', marker='o', linestyle='-', linewidth=2, markersize=8)
ax1.plot(years, hyperloop_pods, color='teal', marker='^', linestyle='-', linewidth=2, markersize=8)

plt.tight_layout()

plt.show()