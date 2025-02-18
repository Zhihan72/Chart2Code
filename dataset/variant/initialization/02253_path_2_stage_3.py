import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(2100, 2210, 10)
robotics = [5, 12, 30, 60, 100, 150, 220, 300, 380, 480, 600]
space_travel = [60, 90, 120, 150, 160, 170, 180, 190, 195, 200, 210]
quantum_computing = [4, 10, 18, 30, 50, 80, 130, 190, 270, 350, 450]
cybernetics = [25, 40, 70, 90, 115, 130, 160, 210, 260, 320, 380]
data = np.array([robotics, space_travel, quantum_computing, cybernetics])
# New set of colors
colors = ['#FF4500', '#2E8B57', '#1E90FF', '#9370DB']

total_innovations = np.sum(data, axis=0)

fig, ax = plt.subplots(figsize=(9, 8))
ax.stackplot(decades, data, colors=colors, alpha=0.8)
ax.plot(decades, total_innovations, color='black', linestyle='--', marker='o', linewidth=2)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()