import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)

panel_A = [50, 52, 48, 47, 49, 51, 53, 55, 54, 52, 53, 57, 59, 61, 60, 58, 57, 55, 56, 58, 60, 62, 64, 66, 65, 63, 62, 64, 65, 67]
panel_B = [45, 46, 44, 43, 45, 46, 47, 49, 50, 48, 49, 50, 51, 53, 54, 52, 51, 50, 52, 53, 55, 56, 58, 57, 56, 55, 54, 56, 57, 59]
panel_C = [40, 41, 39, 37, 38, 39, 42, 44, 45, 43, 41, 42, 43, 45, 44, 43, 41, 42, 44, 46, 47, 49, 50, 52, 51, 49, 48, 49, 50, 51]
panel_D = [35, 36, 34, 33, 34, 36, 38, 39, 40, 38, 37, 38, 39, 41, 40, 39, 38, 37, 39, 41, 42, 43, 45, 47, 46, 44, 43, 45, 47, 49]
panel_E = [30, 31, 29, 28, 29, 30, 32, 33, 34, 32, 31, 32, 33, 34, 32, 31, 30, 32, 34, 35, 36, 37, 39, 40, 39, 37, 36, 37, 39, 40]
panel_F = [25, 26, 24, 23, 24, 25, 27, 28, 29, 27, 26, 27, 28, 30, 29, 27, 26, 27, 28, 30, 31, 32, 34, 35, 34, 32, 31, 32, 34, 36]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(days, panel_A, color='blue', marker='o', linestyle='-', linewidth=2, label='Panel A')
ax1.plot(days, panel_B, color='green', marker='s', linestyle='--', linewidth=2, label='Panel B')
ax1.plot(days, panel_C, color='red', marker='^', linestyle='-.', linewidth=2, label='Panel C')
ax1.plot(days, panel_D, color='purple', marker='D', linestyle=':', linewidth=2, label='Panel D')
ax1.plot(days, panel_E, color='orange', marker='>', linestyle='-', linewidth=2, label='Panel E')
ax1.plot(days, panel_F, color='brown', marker='<', linestyle='--', linewidth=2, label='Panel F')

plt.title('ISS Solar Panel Energy (Monthly)', fontsize=16, fontweight='bold')
plt.xlabel('Days', fontsize=14)
plt.ylabel('Energy (kWh)', fontsize=14)
plt.legend(fontsize=12)

important_days = [10, 15, 20, 25]
annotations = [
    "Flare",
    "Maint.",
    "Radiation",
    "Adjust"
]

for day, annotation in zip(important_days, annotations):
    ax1.annotate(annotation, xy=(day, panel_A[day-1]), xytext=(day, panel_A[day-1] + 5),
                 arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3,rad=.2"),
                 fontsize=10)

plt.tight_layout()

plt.show()