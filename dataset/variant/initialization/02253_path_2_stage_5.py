import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(2100, 2210, 10)
robotics = [5, 12, 30, 60, 100, 150, 220, 300, 380, 480, 600]
quantum_computing = [4, 10, 18, 30, 50, 80, 130, 190, 270, 350, 450]
data = np.array([robotics, quantum_computing])

colors = ['#1E90FF', '#FF4500']  # Reversed original colors

total_innovations = np.sum(data, axis=0)

fig, ax = plt.subplots(figsize=(9, 8))
ax.stackplot(decades, data, colors=colors, alpha=0.9)  # Changed alpha for more opacity
ax.plot(decades, total_innovations, color='purple', linestyle='-.', marker='x', linewidth=3)  # Changed color, line style, marker, and line width
ax.grid(True, linestyle=':', alpha=0.7)  # Changed grid line style and opacity
ax.spines['top'].set_visible(False)  # Removed top border to alter the appearance
ax.spines['right'].set_visible(False)  # Removed right border to alter the appearance

plt.legend(['Robotics', 'Quantum Computing', 'Total Innovations'], loc='upper left', fontsize=10)  # Added and styled legend
plt.tight_layout()
plt.show()