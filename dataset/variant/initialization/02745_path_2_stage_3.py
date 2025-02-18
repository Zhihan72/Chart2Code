import matplotlib.pyplot as plt
import numpy as np

centuries = np.array([
    -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30
])

cuneiform_influence = np.array([40, 42, 44, 35, 30, 20, 10, 5, 0, 0, 0, 0, 0])
phoenician_alphabet_influence = np.array([0, 0, 0, 0, 5, 20, 35, 45, 55, 60, 65, 70, 75])

plt.figure(figsize=(12, 8))

# Apply single color 'green' consistently across all data groups
plt.plot(centuries, cuneiform_influence, label='Cuneiform', color='green', marker='o', linestyle='--', linewidth=2)
plt.plot(centuries, phoenician_alphabet_influence, label='Phoenician', color='green', marker='^', linestyle='-.', linewidth=2)

plt.title("Writing Systems (BC/AD)", fontsize=16, fontweight='bold')
plt.xlabel("Century", fontsize=13)
plt.ylabel("Influence (%)", fontsize=13)

plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(title="Systems", loc='upper left', fontsize=10)

plt.annotate('Cuneiform Peak', xy=(-20, 44), xytext=(-15, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Phoenician Rise', xy=(5, 45), xytext=(10, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.xticks(centuries, rotation=45)

plt.tight_layout()

plt.show()