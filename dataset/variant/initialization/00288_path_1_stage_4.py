import matplotlib.pyplot as plt
import numpy as np

# Plant growth data
plant_height = np.array([10, 13, 21, 25, 33, 35, 38, 45, 50, 58])

plt.figure(figsize=(10, 6))
plt.plot(plant_height, color='forestgreen', linewidth=2, linestyle='-')

plt.title("Growth Analysis", fontsize=16, fontweight='bold')
plt.xlabel("Idx", fontsize=12)
plt.ylabel("Height (cm)", fontsize=12)

plt.tight_layout()

plt.show()