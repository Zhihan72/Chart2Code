import matplotlib.pyplot as plt
import numpy as np

vitamin_intake = np.array([55, 75, 85, 95, 110, 130, 150, 165, 180, 200, 220, 240, 260, 280, 300])
energy_levels = np.array([3, 4, 4, 5, 6, 5, 7, 6, 8, 7, 8, 9, 8, 9, 10])

fig, ax = plt.subplots(figsize=(7, 6))

ax.scatter(vitamin_intake, energy_levels, color='purple', s=100, alpha=0.75, edgecolor='black', label='Data')
ax.set_title("Vitamin vs Energy", fontsize=14, pad=20)
ax.set_xlabel("Vitamin (mg)", fontsize=12)
ax.set_ylabel("Energy Level", fontsize=12)
ax.set_xlim(min(vitamin_intake) - 10, max(vitamin_intake) + 10)
ax.set_ylim(min(energy_levels) - 1, max(energy_levels) + 1)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=10)
ax.annotate('Higher energy', xy=(250, 9), xytext=(230, 9.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

plt.tight_layout()
plt.show()