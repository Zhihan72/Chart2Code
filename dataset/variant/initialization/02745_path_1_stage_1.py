import matplotlib.pyplot as plt
import numpy as np

centuries = np.array([-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30])
cuneiform_influence = np.array([40, 42, 44, 35, 30, 20, 10, 5, 0, 0, 0, 0, 0])
hieroglyphics_influence = np.array([10, 15, 20, 25, 30, 40, 35, 30, 25, 20, 15, 10, 5])
phoenician_alphabet_influence = np.array([0, 0, 0, 0, 5, 20, 35, 45, 55, 60, 65, 70, 75])

plt.figure(figsize=(12, 8))

plt.plot(centuries, cuneiform_influence, color='brown', marker='o', linestyle='--', linewidth=2)
plt.plot(centuries, hieroglyphics_influence, color='darkgreen', marker='s', linestyle='-', linewidth=2)
plt.plot(centuries, phoenician_alphabet_influence, color='navy', marker='^', linestyle='-.', linewidth=2)

plt.title("Evolution of Ancient Writing Systems\nOver Centuries (BC to AD)", fontsize=16, fontweight='bold')
plt.xlabel("Century (BC/AD)", fontsize=13)
plt.ylabel("Global Influence (%)", fontsize=13)

plt.xticks(centuries, rotation=45)
plt.tight_layout()

plt.show()