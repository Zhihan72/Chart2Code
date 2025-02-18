import matplotlib.pyplot as plt
import numpy as np

centuries = np.array([
    -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30
])

cuneiform_influence = np.array([40, 42, 44, 35, 30, 20, 10, 5, 0, 0, 0, 0, 0])
phoenician_alphabet_influence = np.array([0, 0, 0, 0, 5, 20, 35, 45, 55, 60, 65, 70, 75])

plt.figure(figsize=(12, 8))

# Randomly altered stylistic elements.
plt.plot(centuries, cuneiform_influence, label='Cuneiform', color='blue', marker='s', linestyle='-', linewidth=3)
plt.plot(centuries, phoenician_alphabet_influence, label='Phoenician', color='red', marker='x', linestyle=':', linewidth=1.5)

plt.title("Writing Systems (BC/AD)", fontsize=16, fontweight='bold')
plt.xlabel("Century", fontsize=13)
plt.ylabel("Influence (%)", fontsize=13)

# Modified grid style.
plt.grid(True, linestyle='-.', alpha=0.75)

# Changed legend position and appearance.
plt.legend(title="Systems", loc='lower right', fontsize=11)

plt.annotate('Cuneiform Peak', xy=(-20, 44), xytext=(-15, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Phoenician Rise', xy=(5, 45), xytext=(10, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# No rotation in xticks.
plt.xticks(centuries)

plt.tight_layout()

plt.show()