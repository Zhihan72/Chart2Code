import matplotlib.pyplot as plt
import numpy as np

centuries = np.array([-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30])
cuneiform_influence = np.array([44, 35, 42, 20, 40, 0, 30, 5, 10, 0, 0, 25, 0])
hieroglyphics_influence = np.array([25, 10, 30, 20, 15, 40, 35, 5, 30, 15, 20, 25, 10])
phoenician_alphabet_influence = np.array([60, 35, 75, 5, 55, 0, 20, 70, 65, 0, 0, 45, 10])

plt.figure(figsize=(12, 8))

# Applied single color 'blue' consistently across all data groups
plt.plot(centuries, cuneiform_influence, color='blue', marker='o', linestyle='--', linewidth=2)
plt.plot(centuries, hieroglyphics_influence, color='blue', marker='s', linestyle='-', linewidth=2)
plt.plot(centuries, phoenician_alphabet_influence, color='blue', marker='^', linestyle='-.', linewidth=2)

plt.xticks(centuries, rotation=45)
plt.tight_layout()

plt.show()