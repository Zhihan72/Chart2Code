import matplotlib.pyplot as plt
import numpy as np

# Only plant growth data
plant_growth_height = np.array([10, 13, 21, 25, 33, 35, 38, 45, 50, 58])

plt.figure(figsize=(10, 6))
plt.plot(plant_growth_height, color='forestgreen', linewidth=2, label='Plant Growth Height', linestyle='-')

plt.title("Plant Growth\nAnalysis in the Greenbelt Zone", fontsize=16, fontweight='bold')
plt.xlabel("Index", fontsize=12)
plt.ylabel("Plant Growth (Height in cm)", fontsize=12)

plt.legend(title='Legend', fontsize=10, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()